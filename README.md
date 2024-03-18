# Argus Implementation Interview

The goal of this interview is to expand on this flask app by adding functionality to existing wallet queriering.  It's a collaborative exercise so let's work together and of course feel free to use Google or any other resources at your disposal. Treat me as your teammate.

## Getting started.

In the project directory, you can run:

### `poetry install`

Install the packages required for this app (flask + pytest).

### `poetry run -- flask --app app run --debug`

Runs the app in the development mode.\
Open [http://localhost:5000](http://localhost:5000) to view it in your browser.

Check out [http://localhost:5000/transactions/0xb9d9b12f036a4e5e34ab74b0e6fcfc6dd76a66ba](http://localhost:5000/transactions/0xb9d9b12f036a4e5e34ab74b0e6fcfc6dd76a66ba) to see an example of the transactions endpoint.

## Implementation

For the next few items focus on functionality first.

### Existing Bug
There's currently a bug when querying transactions. Let's fix this first.

### Transaction Typing
Currently our transaction types are unrecognized. We'll do a simple version of typing where we want to categorize these transactions into BUY/SELL/GAS or gas transactions.

Here's a simple example of a raw transaction returned from Etherscan:
```
{'blockNumber': '18427409', 'timeStamp': '1698238847', 'hash': '0x380304d5934e579dc23ff9d99857a620468b991e6678e671a70d34ad66753d14', 'nonce': '7', 'blockHash': '0x07e846ed42652d8ad501f5527934dd21f48524899af89228bcbd8d7286352860', 'transactionIndex': '127', 'from': '0x460bfb7dbd4aeae3bdbd6f4f3d4e4b7b09e5838c', 'to': '0xb9d9b12f036a4e5e34ab74b0e6fcfc6dd76a66ba', 'value': '200000000000000000', 'gas': '21000', 'gasPrice': '21140183866', 'isError': '0', 'txreceipt_status': '1', 'input': '0x', 'contractAddress': '', 'cumulativeGasUsed': '9747167', 'gasUsed': '21000', 'confirmations': '1035355', 'methodId': '0x', 'functionName': ''}
```

We would want to convert this into a BUY transaction and a GAS transaction of
0.00044394386 volume (gas * gasPrice).
 
### Testing
Let's add some unit tests for this endpoint in `tests/test_transactions.py`.

Tests can be run with `pytest`

### Multi-Wallet Support
Often times we query multiple wallets at once. How can we change the endpoint to support that.

As we add more wallets we also have to consider our resources. How can we update the logic to improve performance and prevent spam or bad requests?
