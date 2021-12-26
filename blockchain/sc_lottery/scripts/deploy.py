from brownie import Lottery, config, network
from scripts.utils import get_account, get_contract

def deploy_lottery():
    account = get_account()

    lottery = Lottery.deploy(
        get_contract('eth_usd_price_feed')
    )

def main():
    deploy_lottery()