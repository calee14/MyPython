from solcx import compile_standard, install_solc
import json
from secret import RPC_URL, CHAIN_ID, ADDRESS, PRIVATE_KEY

from web3 import Web3

with open('./SimpleStorage.sol', 'r') as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)

# we add these two lines that we forgot from the video!
print("Installing Solidity...")
install_solc("0.6.0")

# compile our solidity file
# generates bytecode/low level code for the EVM to run
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": { "SimpleStorage.sol": { "content": simple_storage_file }},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                }
            }
        },
    },
    solc_version="0.6.0"
)

with open('compiled_code.json', 'w') as file:
    json.dump(compiled_sol, file)

# get bytecode in the compiled json obj
bytecode = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']

# get abi
abi = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']

# connect to the blockchain network (rinkeby)
w3 = Web3(Web3.HTTPProvider(RPC_URL))
# the chain_id aka network id
chain_id = CHAIN_ID
# our address that will be used to very our transaction 
# and identify us on the blockchain
my_address = ADDRESS
# private key for signing our transactions
private_key = PRIVATE_KEY

# create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# get latest transaction
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)

# 1. build a transaction
# 2. sign a transaction
# 3. send a transaction

# all contracts have a constructor whether inherited or modified
# in this case nonce is used to identify the users transaction
# incase the transaction details are all the same and so on
# create transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)
print(transaction)

# sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

print('Deploying contract!')

# send the transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

# wait for the transaction to finish
print('Waiting for transaction to finish...')
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Done! Contract deployed to {tx_receipt.contractAddress}")

# working with the contract
# must have the contract abi
# and must have the contract address
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# to invoke the functions of the contract there are two ways
# call -> make a call to the blockchain to get a value
# transact -> make a state change in the blockchain

# call function to get the intial value in the contract
print(simple_storage.functions.retrieve().call())
store_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "chainId": chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce + 1
    }
)

# same process create, sign, send
signed_store_txn = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
transaction_hash = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
print("Updating stored value...")
tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

print(simple_storage.functions.retrieve().call())