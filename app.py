from datetime import datetime

from flask import Flask

from wallet_querier.etherscan_client import EtherscanClient
from wallet_querier.types import Transaction, TransactionType

app = Flask(__name__)


@app.route("/transactions/<address>", methods=["GET"])
def get_transactions(address):
    etherscan_client = EtherscanClient()

    transactions = etherscan_client.get_account_transactions(address)
    usd_price = float(etherscan_client.get_eth_price())

    res = []
    for transaction in transactions:
        volume = int(transaction["value"]) / (10**15)
        res.append(
            Transaction(
                volume=volume,
                hash=transaction["hash"],
                datetime=datetime.fromtimestamp(int(transaction["timeStamp"])),
                price=usd_price,
                total_value=volume * usd_price,
                type=TransactionType.UNRECOGNIZED,
            )
        )
    return res
