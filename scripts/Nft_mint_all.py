from brownie import APNFT, config, network
from scripts.util import get_account
from scripts.create_metadata import create_metadata
from web3 import Web3

# need to create upload_to_pinata.py
# need to create create_metadata.py

sample_token_uri = "https://ipfs.io/ipfs/{}?filename={}"


def mint_nft_all():
    account = get_account()

    if len(APNFT) == 0:
        print("NFT has not been deployed yet!")
        return

    apnft = APNFT[-1]

    print(apnft.address)

    if apnft.checkTokenBalance() == 0:
        print("No fund in the token")
        return

    tokenBalance = Web3.fromWei(apnft.checkTokenBalance(), "ether")
    print(f"The token balance is: {tokenBalance}")

    metadatas = create_metadata()

    for metadata in metadatas:
        token_uri = sample_token_uri.format(metadata["CID"], metadata["filename"])
        tx = apnft.createImageNFT(token_uri, {"from": account})
        tx.wait(1)

        print("New token has been created!")


def main():
    mint_nft_all()
