from brownie import APNFT, config, network
from scripts.util import get_account


sample_token_uri = "https://ipfs.io/ipfs/{}?filename={}"


def mint_nft():
    account = get_account()

    if len(APNFT) == 0:
        print("NFT has not been deployed yet!")
        return

    apnft = APNFT[-1]

    if apnft.tokenBalance == 0:
        print("No fund in the token")
        return

    tx = apnft.createImageNFT(sample_token_uri, {"from": account})
    tx.wait(1)


def main():
    mint_nft()
