from warnings import simplefilter
from brownie import SimpleStorage, accounts, config

def read_contract():
    # prints the address the deployed contract
    print(SimpleStorage[0])

    # gets the last deployment
    simple_storage = SimpleStorage[-1]

    # need the abi and address but brownie know that it's stored 
    # in the deployment/compiled file
    print(simple_storage.retrieve())


def main():
    read_contract()