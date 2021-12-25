// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract Lottery is VRFConsumerBase, Ownable {

    address payable[] public players;
    address payable public recentWinner;
    uint256 public randomness;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUsdPriceFeed;

    enum LOTTERY_STATE {
        OPEN,
        CLOSED,
        CALCULATING_WINNER
    }
    // Lottery states
    // 0
    // 1
    // 2

    LOTTERY_STATE public lottery_state;
    uint256 public fee;
    bytes32 public keyhash;
    // constructor get the aggregator address and inherit the consumerbase
    // constructor
    constructor(
        address _priceFeed, 
        address _vrfCoordinator, 
        address _link,
        uint256 _fee,
        bytes32 _keyhash
    ) public VRFConsumerBase(_vrfCoordinator, _link) {
        usdEntryFee = 50 * (10**18);
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeed);
        lottery_state = LOTTERY_STATE.CLOSED; // also can put 1 to represetn CLOSED
        fee= _fee;
        keyhash = _keyhash;
    }

    function enter() public payable {
        // $50 minimum
        require(lottery_state == LOTTERY_STATE.OPEN);
        require(msg.value >= getEntranceFee(), "Not enough ETH!");
        players.push(payable(msg.sender));
    }

    function getEntranceFee() public view returns (uint256) {
        // get entrance fee
        (,int256 price,,,) = ethUsdPriceFeed.latestRoundData();
        uint256 adjustedPrice = uint256(price) * 10**10; // conver to 18 decimals since we know the aggregator only returns up to 8 digits 

        // $50, $2,000 / ETH
        // 50/2,000
        // 50 * 100000 / 2000
        uint256 costToEnter = (usdEntryFee * 10**18) / adjustedPrice;
        return costToEnter;

    }

    function startLottery() public onlyOwner {
        require(lottery_state == LOTTERY_STATE.CLOSED, 
            "Can't start a new lottery yet!"
        );
        lottery_state = LOTTERY_STATE.OPEN;
    }

    function endLottery() public {
        // keccak is a hashing algo
        // which takes in a bunch of random data points
        // however, the vulnerability is that the hashing algo stays the same
        // so if you can guess the random data inputs then you know 
        // what the hash will output
        // uint(
        //     keccak256(
        //         abi.encodePacked(
        //             nonce, // nonce is predictable (aka, transaction number)
        //             msg.sender, // msg.sender is predictable
        //             block.difficulty, // difficulty can be manipulated
        //             block.timestamp // timestamp is predictable
        //         )
        //     )
        // ) % players.length;
        lottery_state = LOTTERY_STATE.CALCULATING_WINNER;
        // in the first transaction request a random number
        // then in the second transaction once the chainlink node has 
        // generated a random number, the contract will call a the
        // fufillRandomness function based on the parent contract
        bytes32 requestId = requestRandomness(keyhash, fee);
    }

    function fulfillRandomness(bytes32 _requestId, uint256 _randomness) 
        internal 
        override 
    {
        require(
            lottery_state == LOTTERY_STATE.CALCULATING_WINNER,
            "You aren't there yet!" 
        );
        require(_randomness > 0, "random-not-found");
        uint256 indexOfWinner = _randomness % players.length;
        recentWinner = players[indexOfWinner];

        recentWinner.transfer(address(this).balance);

        // Reset the lottery
        players = new address payable[](0);
        lottery_state = LOTTERY_STATE.CLOSED;
        randomness = _randomness;
    }
}