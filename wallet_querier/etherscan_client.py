import requests
import os


class EtherscanClient:
    def __init__(self):
        self.api_key = os.environ.get("ETHERSCAN_API_KEY")
        self.base_url = "https://api.etherscan.io/api"

    def get_account_transactions(self, address):
        response = requests.get(
            url=self.base_url,
            params={
                "module": "account",
                "action": "txlist",
                "address": address,
                "startblock": 0,
                "endblock": 99999999,
                "apikey": self.api_key,
                "sort": "desc",
            }
        )

        return response.json()['result']

    def get_eth_price(self):
        response = requests.get(
            url=self.base_url,
            params={
                "module": "stats",
                "action": "ethprice",
                "apikey": self.api_key,
            }
        )

        return response.json()['result']["ethusd"]
