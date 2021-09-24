from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()
    # Pass the price feed  address to our contract
    if network.show_active() not in LOCAL_BLOCKCAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth/usd"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print("Contract deployed to " + fund_me.address)
    return fund_me


def main():
    deploy_fund_me()
