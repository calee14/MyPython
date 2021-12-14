# Intro to blockchain
## Blockchain definitions
- some dude took the blockchain system/program that ran bitcoin and made etheruem with it which uses smart contracts.
- smart contracts are agreements that don't require a third party to be written
    - smart contracts are written in code that will be executed
    - smart contracts need real world data
        - __blockchain oracles__ help bring in real world data into to the blockchain or run external computation 
        - __hybrid smart contracts__ blockchain is decentralized and off-chain data such as computations and real world data need to be decentralized.
        - chainlink = decentralized oracle network that bring real world data and computations off-chain
        - Dapp = smart contract = decentralized app 
            - smart contract platforms = blockchains
            - hybrid smart contract = smart contract with some off-chain component like real world data and computation

## Blockchain properties
- decentralized = no single entity controls the whole network
    - data on the blockchain is immutable, meaning it can't be changed
    - similarly hacking the blockchain is nearly impossible, thus assets and data are protected on the blockchain
- based on math-based agreements aka trust-mimized agreements
    - agreements based on agreements not human interaction or people
    - opposite of political trust-based agreements
- decentralization gives freedom
- DAOs = decentralized autonomous organizations
    - applications or orgs the live on the blockchian

## MetaMask and Eth Wallets
- make accounts and wallets to the eth blockchain on MetaMask
    - can make many accounts in the MetaMask Wallet
        - those accounts are protected by a private key which gives access to funds in the eth account
            - private key = access to one account
            - public address = no access to accounts
- etherscan.io for viewing the eth blockchain
    - Testnet are blockchains that help test smart contracts but money isn't real on that network
    - can also view the test networks. not working with real money

## Making transactions on the blockchain
-  Gas = unit of computational measurement. the more computations for a transaction the more gas you have to pay.
- every transaction that happens __on-the-chain__ pays a "gas fee" to node operators
- When making a transaction to send eth need to pay a "gas fee"
- transaction has a fee = gas used * gas price
    - set a higher gas price means that the node will likely include your transaction in the block
    - 1 GWEI = 0.000000000771 ETH

## How A Blockchain works (Blockchain 101)
- https://andersbrownworth.com/blockchain/
- __hash__ = unique __fixed__ length of string meant to identify a piece of data. created by placing the data into a "hash function"
    - SHA-3 is used by eth and SHA-256 is used by Bitcoin
- __block__: (important example in code)
```js
{
    block: Number,
    nonce: Number, // number that is set so that the hash value starts with a cerrtain number of leading zeros
    data: String, 
    hash: String, // fixed length according to the hash function. if the hash starts with a certin number of certain zeros then we have signed the block
}
```
- __blockchain__:
```js
{ // block 0
    block: Number,
    nonce: Number, // number that is set so that the hash value starts with a cerrtain number of leading zeros
    data: String, 
    prev: String, // hash of the previous block, unless first block then full of zeros
    hash: String, // fixed length according to the hash function. if the hash starts with a certin number of certain zeros then we have signed the block
}

{ // block 1
    block: Number,
    nonce: Number, // number that is set so that the hash value starts with a cerrtain number of leading zeros
    data: String, 
    prev: String, // since the block, nonce, data, and prev string all go into the hash, changing one data entry to the hash func will affect all of the following blocks in the chain
    hash: String, // fixed length according to the hash function. if the hash starts with a certin number of certain zeros then we have signed the block
}

{ // block 3
    block: Number,
    nonce: Number, // number that is set so that the hash value starts with a cerrtain number of leading zeros
    data: String, 
    prev: String,
    hash: String, // fixed length according to the hash function. if the hash starts with a certin number of certain zeros then we have signed the block
}
```
    - In a blockchain, the block, nonce, data, and prev_hash values all go into making the hash. Thus, changing one data entry to the hash func will affect the block's hash and then all of the following blocks in the chain
- __distributed blockchain__ = many peers have a copy of the blockchain.