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
- https://www.youtube.com/watch?v=_160oMzblY8
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

{ // block 2
    block: Number,
    nonce: Number, // number that is set so that the hash value starts with a cerrtain number of leading zeros
    data: String, 
    prev: String,
    hash: String, // fixed length according to the hash function. if the hash starts with a certin number of certain zeros then we have signed the block
}
```
- Code explaination: 
    - In a blockchain, the block, nonce, data, and prev_hash values all go into making the hash. Thus, changing one data entry to the hash func will affect the block's hash and then all of the following blocks in the chain will no longer be correctly signed.
- __distributed blockchain__ = many peers have a copy of the blockchain.
    - even if all hashes in the blockchain start with certain number of zeros, meaning correctly signed, an different hash at the last block in the chain will indicate if there was a incorrect mining process.
        - a democractic process will decide which chain is the accurate one.
- __tokens__ = currency for transactions
- __coincbase__ = where the currency is created, given as reward
```js
{ // block 0
    block: Number,
    nonce: Number, // number that is set so that the hash value starts with a cerrtain number of leading zeros
    coinbase: {value: Number, to: String }, // where money is generated and paid to an account
    transactions: { }, // no transactions in the first block
    prev: String, // hash of the previous block, unless first block then full of zeros
    hash: String, // fixed length according to the hash function. if the hash starts with a certin number of certain zeros then we have signed the block
}

{ // block 1
    block: Number,
    nonce: Number, // number that is set so that the hash value starts with a cerrtain number of leading zeros
    transactions: {
        [{value: Number, from: String, to: String},
        {value: Number, from: String, to: String},
        {value: Number, from: String, to: String}
        ]
    }, 
    prev: String, // since the block, nonce, data, and prev string all go into the hash, changing one data entry to the hash func will affect all of the following blocks in the chain
    hash: String, // fixed length according to the hash function. if the hash starts with a certin number of certain zeros then we have signed the block
}

{ // block 3
    block: Number,
    nonce: Number, // number that is set so that the hash value starts with a cerrtain number of leading zeros
    transactions: {
        [{value: Number, from: String, to: String},
        {value: Number, from: String, to: String},
        {value: Number, from: String, to: String},
        {value: Number, from: String, to: String},
        ]
    }, 
    prev: String,
    hash: String, // fixed length according to the hash function. if the hash starts with a certin number of certain zeros then we have signed the block
}
```
- __public and private key pairs__ = way to securely make transactions on the blockchain
    - not harmful to put the public key in the public because one cannot derive the private key based off the public key
- __private key__ = a hash/key that is used to generate a public key, which is another string made up of __numbers__
- __signature__ = use message or data and private key to sign hash and make a signature. This signature can also be reached by encrypting/hashing the same data and public key to reach the signature produced by the private key.
    - this ensures that we know that the data was correctly signed by the private key
- __transaction__ = 
    { 
        value: 10, 
        from: payer_public_key, 
        to: receiver_public_key 
    }
    private_key: a string full of numbers \
    => used to sign/encrypt/generate a signature = another string generated based off the transaction data \
    => then send out signature to the blockchain where the data of the transaction must sign to the correct signature
- beauty of blockchain is that you generate a number which will be your private key and then a public key, which will allow you to pay and receive money. 
- the person wanting to make a transaction can only sign it

## Actual implementation
- for each blockchain each hash algo is diff but the fundamental ideas stay the same
    - blockchains run on many different independent nodes, which are the individual servers
- __consensus__ = mechanism used to agree on the state of the blockchain 
    - __chain selection rule__ = longest chain rule, which ever blockchain in the node has the longest chain is the one that is the most that the system goes with
        - __confirmations__ = appears in our transaction and means the amount of blocks that appear after the block our transformation was in
    - __sybil resistance algo__ = __proof of work__, way to defend against malicious hackers from creating a lot of nodes to take the rewards
        - __proof of work__ = verifible way to identify the block author
- in proof of work every node is competing against each other. so the first node to compute the block will get the transaction fee (derived form the gas price set by the person making the transactions) and block reward where the blockchain awards the miner
- __sybil attack__ = where user creates a lot of accounts to influence the blockchain in mining.
- __51%__ = where one single entity can control the entire blockchain by having the longest chain as long as 51% of other nodes match them
- proof of stake is more env friendly
    - proof of stake nodes put up __collateral__ to say that they will behave honestly
    - if they behave badly they'll lose their stake
    - in this POS the nodes are chosen randomly and the other nodes are now validators to make sure that the chosen node validated correctly
- blockchains cannot take scale if there is an influx in people who want to use blockchains
    - eth 2.0 will implement __sharding__ where there will be several blockchains that will increase the number of transactions that can happen at a time. these blockchains will connect with the main one
-  
