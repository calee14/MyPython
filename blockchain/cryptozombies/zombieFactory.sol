pragma solidity >=0.5.0 <0.6.0;

import "./ownable.sol";

contract ZombieFactory is Ownable {

    event NewZombie(uint zombieId, string name, uint dna);

    uint dnaDigits = 16;
    uint dnaModulus = 10 ** dnaDigits;
    uint cooldownTime = 1 days; // time in solidity 

    /**
    use struct to define object props
    struct packing can help reudce gas costs
     */
    struct Zombie {
        string name;
        uint dna;
        uint32 level;
        uint32 readyTime;
    }


    Zombie[] public zombies;

    /**
    make contract maps/dictionaries
     */
    mapping (uint => address) public zombieToOwner;
    mapping (address => uint) ownerZombieCount;

    /**
    _createZombie - internal func, private accessible by child class
    params: 
        string memory _name, passed by pointer
        uint _dna, 16 digit value
    returns:
        void - makes a new zombie
     */
    function _createZombie(string memory _name, uint _dna) internal {
        uint id = zombies.push(Zombie(_name, _dna)) - 1;
        zombieToOwner[id] = msg.sender;
        ownerZombieCount[msg.sender]++;
        emit NewZombie(id, _name, _dna);
    }

    /**
    _generateRandomDna - private, getter func
    params:
        string memory _str - random string passed in
    returns:
        uint - new dna a 16 digit value
     */
    function _generateRandomDna(string memory _str) private view returns (uint) {
        uint rand = uint(keccak256(abi.encodePacked(_str)));
        return rand % dnaModulus;
    }

    function createRandomZombie(string memory _name) public {
        require(ownerZombieCount[msg.sender] == 0);
        uint randDna = _generateRandomDna(_name);
        randDna = randDna - randDna % 100;
        _createZombie(_name, randDna);
    }

}
