// contracts/OurToken.sol
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract OurToken is ERC20 {
    // wei
    string _tokenName = "JOMAMA COIN";
    string _tokenSymbol = "MAMA";

    constructor(uint256 initialSupply) ERC20(_tokenName, _tokenSymbol) {
        _mint(msg.sender, initialSupply);
    }
}
