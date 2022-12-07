from brownie import APNFT, config, network
from web3 import Web3


def check_nft_balance():
    if len(APNFT) == 0:
        print("NFT has not been deployed yet!")
        return

    nft = APNFT[-1]

    print("Getting token balance.....")
    tokenBalance = Web3.fromWei(nft.checkTokenBalance(), "ether")
    print(f" The token balance is: {tokenBalance}")


def main():
    check_nft_balance()
