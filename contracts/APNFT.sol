//SPDX-License-Identifier: MIT

pragma solidity 0.7.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "./FitcoinToken.sol";

contract APNFT is ERC721 {
    FitcoinToken fitcointoken;
    uint256 public tokenCounter;
    uint256 public tokenFee;
    uint256 public maxImages = 5;

    enum Image {
        APNFT_1,
        APNFT_2,
        APNFT_3,
        APNFT_4,
        APNFT_5
    }

    mapping(uint256 => address) public tokenIdToImage;
    mapping(uint256 => address) public requestIdToSender;

    event requestedImage(uint256 indexed requestId, address requester);
    event imageAssigned(uint256 indexed tokenId, Image image);

    constructor(address _fitcointokenAddress) ERC721("My NFT", "APNFT") {
        fitcointoken = FitcoinToken(_fitcointokenAddress);
        uint8 tokenDecimals = fitcointoken.decimals();
        tokenFee = 1000 * (10**tokenDecimals);
        tokenCounter = 0;
    }

    function checkTokenBalance() public view returns (uint256) {
        return fitcointoken.balanceOf(address(this));
    }

    function createImageNFT(string memory _tokenURI) public returns (bytes32) {
        require(
            tokenCounter <= maxImages,
            "Maximum quantity of Images emitted"
        );
        require(tokenFee <= fitcointoken.balanceOf(address(this)));

        uint256 newTokenID = tokenCounter;

        requestIdToSender[newTokenID] = msg.sender;
        emit requestedImage(newTokenID, msg.sender);

        Image image = Image(newTokenID);
        emit imageAssigned(newTokenID, image);

        _safeMint(msg.sender, newTokenID);
        _setTokenURI(newTokenID, _tokenURI);
        tokenCounter += 1;
    }
}
