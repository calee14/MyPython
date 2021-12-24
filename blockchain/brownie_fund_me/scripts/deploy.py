from brownie import FundMe, config, network, MockV3Aggregator
from brownie_fund_me.scripts.utils import deploy_mocks
from scripts.utils import get_account

def deploy_fund_me():
    account = get_account()
    # if we're on rinkeby use the rinkeby aggregator address oracle
    if network.show_active() != 'development':
        price_feed_address = config['networks'][network.show_active()][
            'eth_usd_price_feed'
        ]
    else:
        print(f'The active network is {network.show_active()}')
        print('deploying mocks')
        deploy_mocks()
        # get the most recently deployed MockV3Aggregator
        price_feed_address = MockV3Aggregator[-1].address
    

    fund_me = FundMe.deploy(
        price_feed_address, 
        {'from': account}, 
        publish_source=config['networks'][network.show_active()]['verify']
    )
    print(f'Contract deployed to {fund_me.address}')
    
def main():
    deploy_fund_me()