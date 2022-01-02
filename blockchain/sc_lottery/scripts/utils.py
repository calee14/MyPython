from brownie import network, config, accounts, MockV3Aggregator, Contract, VRFCoordinatorMock, LinkTokenInterface
from toolz.itertoolz import get
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ['mainnet-forked']
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development', 'ganache-local']

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
        
    return accounts.add(config["wallets"]["from_key"])

DECIMALS = 8
STARTING_PRICE = 200000000000

def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        mock_aggregator = MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {'from': get_account() }
        )
    if len(VRFCoordinatorMock) <= 0:
        mock_vrf_coordinator = VRFCoordinatorMock.deploy(
            DECIMALS, STARTING_PRICE, {'from': get_account() }
        )

contract_to_mock = {
    'eth_usd_price_feed': MockV3Aggregator,
    'vrf_coordinator': VRFCoordinatorMock,
}

def get_contract(contract_name):
    """This function will grab the contract addresses from the brownie config
    if defined, otherwise, it will deploy a mock of the contract and return
    that contract.
    
    Args:
        contract_name: String
    Returns:
        brownie.network.contract.ProjectContract: the most recent deployed version
        of the contract (MockV3Aggregator[-1])
    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # check the contract obj for the number of deployed contracts
        if len(contract_type) <= 0: 
            deploy_mocks()
        # MockV3Aggregator[-1]
        contract = contract_type[-1]
    else:
        contract_address = config['networks'][network.show_active()][contract_name]
        # address
        # ABI
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract
        