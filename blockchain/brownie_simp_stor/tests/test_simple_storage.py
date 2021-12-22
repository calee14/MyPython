from brownie import SimpleStorage, accounts, config

def test_deploy():
    # arrange
    account = accounts.add(config['wallets']['from_key'])

    # act
    simple_storage = SimpleStorage.deploy({'from': account})
    starting_value = simple_storage.retrieve()
    expected = 0

    # Assert
    assert starting_value == expected

def test_updating_storage():
    # arrange
    account = accounts.add(config['wallets']['from_key'])
    simple_storage = SimpleStorage.deploy({'from': account})

    # act
    expected = 15
    simple_storage.store(expected, {'from': account})

    # assert
    assert expected == simple_storage.retrieve()