pragma solidity >=0.5.0 <0.6.0;

import "./zombiefeeding.sol";

contract ZombieHelper is ZombieFeeding {

    modifier aboveLevel(uint256 _level, uint256 _zombieId) {
        require(zombies[_zombieId].level >= _level);
        _;
    }

    /**
    changeName - changes the dna of an existing zombie, 
                uses the modifier to make sure the zombie
                has a level above 2
    params:
        - uint256 - id of zombie 
        - string calldata - string of the new zombie name 'calldata' for func with modifier
    returns:
        void - makes sure that the msg sender owns zombie
    */
    function changeName(uint256 _zombieId, string calldata _newName)
        external
        aboveLevel(2, _zombieId)
    {
        require(msg.sender == zombieToOwner[_zombieId]);
        zombies[_zombieId].name = _newName;
    }

    /**
    changeDna - changes the dna of an existing zombie
    params:
        - uint256 - id of zombie 
        - uin256 - 16 digit number of zombies' dna
    returns:
        void - makes sure that the msg sender owns zombie
    */
    function changeDna(uint256 _zombieId, uint256 _newDna)
        external
        aboveLevel(20, _zombieId)
    {
        require(msg.sender == zombieToOwner[_zombieId]);
        zombies[_zombieId].dna = _newDna;
    }

    /**
    getZombiesByOwner - external view = meaning 0 gas fees. func can only be 
                        called outside eth network.
    params:
        address - address of owner of zombie
    returns:
        uint[] - ids of all zombies owned by owner
    */
    function getZombiesByOwner(address _owner) external view returns (uint[] memory) {
        uint[] memory result = new uint[](ownerZombieCount[_owner]);
        uint counter = 0;
        for (uint i = 0; i < zombies.length; i++) {
            if (zombieToOwner[i] == _owner) {
                result[counter] = i;
                counter++;
            }
        }
        return result;
    }
}
