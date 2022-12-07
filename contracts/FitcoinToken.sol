// SPDX-License-Identifier: MIT

pragma solidity 0.7.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract FitcoinToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("Fitcoin Token", "FC") {
        _mint(msg.sender, initialSupply);
    }
}
