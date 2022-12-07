from brownie import APNFT, FitcoinToken, config, network
from scripts.util import get_account


def transfer_token_nft():
    account = get_account()

    if len(FitcoinToken) == 0:
        print("Token has not been deployed!")
        return

    token = FitcoinToken[-1]
    amount = 1000 * (10 ** token.decimals())

    if len(APNFT) == 0:
        print("NFT not deployed!")
        return

    nft = APNFT[-1]

    print(
        f"Transferring {token.symbol} at address: {token.address} to NFT at address {nft.address}'''''"
    )

    token.transfer(nft.address, amount, {"from": account})
    print("Token transferred!")


def main():
    transfer_token_nft()
