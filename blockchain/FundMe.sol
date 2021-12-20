// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;

// Interfaces compile => ABI's are application binary interfaces
// It tells how solidity should interact with the contract and it's functions
// the interface also describes how a smart contract will function
//  in terms of the function params, returns
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
// smart contract for safe math calc because of int overflow
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

contract FundMe {
    using SafeMathChainlink for uint256;

    // store payments
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    address public owner;

    // whoever creates this contract is the owner
    // the constructor is run when contract is created
    // the contract is created in a transaction so the message
    // will have a sender member
    constructor() public {
        // set the owner to whoever created the contract
        owner = msg.sender;
    }

    // payable says that we would like to make a payment on the eth blockchain
    function fund() public payable {
        
        // $50 = 50 * 10^18 which adds 18 digits/decimal spaces
        uint256 minUSD = 50 * 10 ** 18;
        // let there be a requirement
        // 1gwei < $50 so it should return an error
        require(getConversionRate(msg.value) >= minUSD, "You need to spend more ETH!");

        addressToAmountFunded[msg.sender] += msg.value;
        // what the ETH -> USD conversion rate

        // oracles are unable to connect to outside real world data.
        // oracles need to be only on the blockchain
        // blockchains can't be making api calls
        // centralized oracles are a point of failure because it is the one 
        //  source of real world data
        // Chainlink is a decentralized oracle network to get data from the real world
        // 

        funders.push(msg.sender);
    }

    function getVersion() public view returns (uint256) {
        // find the contract address for the aggregator contract
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        // find the smart contract interface again
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        // expand the tuple variable and omit the ones we don't use
        // the price is given in gwei
        (,int256 answer,,,) = priceFeed.latestRoundData();
        // need to convert from eth to wei
        return uint256(answer * 10000000000);
    }

    function getConversionRate(uint256 ethAmount) public view returns (uint256) {
        uint256 ethPrice = getPrice();
        // conver the gwei amount to wei to eth
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }

    modifier onlyOwner {
        // only want the owner to be able to run this func
        // this code will run before calling the modified func
        require(msg.sender == owner);
        // the underscore will be replaced by the original function
        // which the modifier is modifying
        _;
    }

    function withdraw() payable onlyOwner public {
        // who ever intiated the message/transaction, the contract will transfer
        // the sender the balance of this contract
        msg.sender.transfer(address(this).balance);

        // reset funder tracking funding
        for(uint256 funderIndex=0; funderIndex < funders.length; funderIndex++) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }

        funders = new address[](0);
    }
}