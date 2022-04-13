pragma solidity >=0.5.0 <0.6.0;

import "./zombieFactory.sol";

/**
KittyInterface - interact with the CryptoKitties smart contract
  - we know it's a contract bc of the fucntion declaration and no
  func definitions in between {}
 */
contract KittyInterface {
    function getKitty(uint256 _id)
        external
        view
        returns (
            bool isGestating,
            bool isReady,
            uint256 cooldownIndex,
            uint256 nextActionAt,
            uint256 siringWithId,
            uint256 birthTime,
            uint256 matronId,
            uint256 sireId,
            uint256 generation,
            uint256 genes
        );
}

contract ZombieFeeding is ZombieFactory {
    KittyInterface kittyContract;

	modifier ownerOf(uint _zombieId) {
		require(msg.sender == zombieToOwner[_zombieId]);
		_;
	}

	/**
	setKittyContractAddress 
		- only allowed by owner
	 */
	function setKittyContractAddress(address _address) external onlyOwner {
		kittyContract = KittyInterface(_address);
	}

	function _triggerCooldown(Zombie storage _zombie) internal {
		_zombie.readyTime = uint32(now + cooldownTime);
	}

	function _isReady(Zombie storage _zombie) internal view returns (bool) {
		return (_zombie.readyTime <= now);
	}

    function feedAndMultiply(uint _zombieId, uint _targetDna, string memory _species) internal ownerOf(_zombieId) {
		Zombie storage myZombie = zombies[_zombieId];
		require(_isReady(myZombie));
		_targetDna = _targetDna % dnaModulus;
		uint newDna = (myZombie.dna + _targetDna) / 2;
		if (keccak256(abi.encodePacked(_species)) == keccak256(abi.encodePacked("kitty"))) {
		newDna = newDna - newDna % 100 + 99;
		}
		_createZombie("NoName", newDna);
		_triggerCooldown(myZombie);
	}

	function feedOnKitty(uint _zombieId, uint _kittyId) public {
		uint kittyDna;
		(,,,,,,,,,kittyDna) = kittyContract.getKitty(_kittyId);
		// And modify function call here:
		feedAndMultiply(_zombieId, kittyDna, "kitty");
	}
}
