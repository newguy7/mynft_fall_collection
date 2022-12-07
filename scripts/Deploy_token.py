from brownie import FitcoinToken, config, network
from scripts.util import get_account


def deploy_token():
    account = get_account()

    fitcoin = FitcoinToken.deploy(
        10_000_000 * (10**18),
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )


def main():
    deploy_token()
