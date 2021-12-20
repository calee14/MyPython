// SPDX-License-Identifier: MIT

pragma solidity >0.6.0;

contract SimpleStorage {
    
    // uint = unsigned int
    // uin256 = unsigned int with a max size of 256 bits
    // favNum var will get initialized to zero
    // variables are automatically internal
    uint256 favNum;

    // allow us to create new data objects
    struct People {
        uint256 favNum;
        string name;
    }

    // define an array of struct People
    // this is a dynamic array but it can be fixed if we put
    // a number in the array
    People[] public people;
    mapping(string => uint256) public nameToFavNum;
    
    // other type of variables
    // bool favBool = false;
    // string favString = "kylo";
    // int256 favInt = -69;
    // address favAddress = 0x4673D9cbC00fFa7a0Aa648ee6AF870E31F8075B5;
    // bytes32 favoriteBytes = "cat";

    // public functions are methods that can be run by anything even var
    // external functions are methods that can only be called by external contracts
    //  not by the same one
    // internal functions can only be called by functions in the same contract
    //  and by contracts derived by this contract
    // private methods can only be accessed by within the defined contract and no where else
    function store(uint256 _favNum) public {
        favNum = _favNum;
        // same scope as store and that's it
        // uint256 test = 4;
    }

    // view and pure are non transaction based methods
    // meaning that we're just reading off the blockchain; no state change
    // pure functions are something that does some pure math
    function retrieve() public view returns(uint256) {
        return favNum;
    }

    /* whenever a function is called a transaction is made to change the state of the blockchain
    that's storing the data in the network
    */

    // addPerson will append to the array
    // the `memory` keyword in the param means that the var will persist
    //  for only the duration of the function and delete itself
    //    since strings are obj/array of char then it needs to be deleted
    // `storage` will keep the variabel and persist in storage
    function addPerson(string memory _name, uint256 _favNum) public {
        people.push(People({favNum: _favNum, name: _name}));
        nameToFavNum[_name] = _favNum;
    }
    // when deploying from remix eth I'm using meta mask as my web3 which is called
    // injected web3. metamask is acting as my node on the blockchain network
    // when we deploy we're making a transaction to make a contract on the blockchain

    // EVM = ethereum virtual machine
    // code is compiled to the EVM so that the code can be run
}