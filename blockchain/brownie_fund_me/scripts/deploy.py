from brownie import FundMe, config, network, MockV3Aggregator
from scripts.utils import deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.utils import get_account

def deploy_fund_me():
    account = get_account()
    # if we're on rinkeby or local blockchain use the rinkeby aggregator address oracle
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config['networks'][network.show_active()][
            'eth_usd_price_feed'
        ]
    else:
        # deploy mock aggregator to the network
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

    return fund_me
    
def main():
    deploy_fund_me()