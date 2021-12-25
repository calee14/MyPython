from brownie import Lottery, accounts, MockV3Aggregator
from web3 import Web3
from scripts.utils import deploy_mocks

def test_get_entrance_fee():
    account = accounts[0]
    
    deploy_mocks()

    lottery = Lottery.deploy(MockV3Aggregator[-1].address, {
        'from': account
        }
    )

    assert lottery.getEntranceFee() > Web3.toWei(0.018, 'ether')
    assert lottery.getEntranceFee() < Web3.toWei(0.027, 'ether')
