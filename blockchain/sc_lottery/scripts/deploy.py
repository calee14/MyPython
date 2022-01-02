from brownie import Lottery, config, network
from scripts.utils import get_account, get_contract

def deploy_lottery():
    account = get_account()

    lottery = Lottery.deploy(
        get_contract('eth_usd_price_feed').address,
        get_contract('vrf_coordinator').address,
        '0x01BE23585060835E02B77ef475b0Cc51aA1e0709', # link token address
        
    )

def main():
    deploy_lottery()