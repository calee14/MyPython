# Uniswap
## Finance behind Uniwap
- There is a liquidity pool where lenders will give their ether or ERC20 token to the pool (the pool takes the form of a smart contract prop.)
    - In exchange for the eth or ERC20, the lender gets a Liquidity Pool (LP) token
        - The lender can exchange the token for the eth or ERC20 back at any time
- A trader will send eth or whatever ERC20 token in exchange for another ERC20 token. There will be a transaction fee from the liquidity pool providfer (uniswap)
## Factory
- A factory smart contract is used to create the exchange smart contract
    - These contracts that are created from factory are the exchanges for tokens
        - EX: ETH/DAI, etc.
- Need a Uniswap Factory Interface to interact with the smart contract
    - call functions to swap tokens