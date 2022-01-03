from scripts.utils import get_account
from brownie import config, network, interface

def main():
    get_weth()

def get_weth():
    '''
    Mints WETH by depositing ETH.
    '''
    # We need ABI and Address of the converter contract
    # which is called IWeth and it follows the ERC20 protocol
    account = get_account()
    weth = interface.IWeth(config['networks'][network.show_active()]['weth_token'])
    tx = weth.deposit({'from': account, 'value': 0.1 * 10 ** 18})
    tx.wait(1) # 1 means that the program will wait for the program to finish before continue
    print(f'Received 0.1 WETH')
    return tx