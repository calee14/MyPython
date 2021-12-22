from brownie import network, accounts, config
from dotenv import load_dotenv
import os

load_dotenv()

def deploy_contract():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print(account)

def main():
    deploy_contract()
    print('hello')