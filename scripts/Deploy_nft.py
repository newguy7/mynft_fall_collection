from brownie import APNFT, FitcoinToken, config, network
from scripts.util import get_account


def deploy_nft():
    account = get_account()

    if len(FitcoinToken) == 0:
        print("FitcoinToken has not been deployed!")
        return
    fitcoin_address = FitcoinToken[-1].address

    apnft = APNFT.deploy(
        fitcoin_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )


def main():
    deploy_nft()
