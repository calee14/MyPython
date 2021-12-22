from brownie import network, accounts, config, SimpleStorage
from dotenv import load_dotenv
import os

load_dotenv()

def deploy_simple_storage():
    account = get_account()
    # this deploy function will create, sign and send the transaction
    # it will also know if the transaction is a call or a transaction
    simple_storage = SimpleStorage.deploy({"from": account})

    # brownie knows that this retreive is a call 
    stored_value = simple_storage.retrieve()
    print(stored_value)
    
    # simple storage make a transaction to store signing with our account
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)

    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def get_account():
    if network.show_active() == "development":
        return accounts.add(config['wallets']['from_key'])
    else:
        return accounts.add(config['wallets']['from_key'])

def main():
    deploy_simple_storage()
    print('hello')