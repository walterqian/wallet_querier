# Argus Implementation Interview

The goal of this interview is to expand on this flask app by adding functionality to existing wallet queriering.  It's a collaborative exercise so let's work together and of course feel free to use Google or any other resources at your disposal. Treat me as your teammate.

## Getting started.

In the project directory, you can run:

### `poetry install`

Install the packages required for this app (flask + pytest).

### `poetry run -- flask --app app run --debug`

Runs the app in the development mode.\
Open [http://localhost:5000](http://localhost:5000) to view it in your browser.

Check out [http://localhost:5000/transactions/0x539C92186f7C6CC4CbF443F26eF84C595baBBcA1](http://localhost:5000/transactions/0x539C92186f7C6CC4CbF443F26eF84C595baBBcA1) to see an example of the transactions endpoint.

## Implementation

For the next few items focus on functionality first.

### Rate Limiting
Add rate limiting so we don't hit an error from etherscan.

### Existing Bug
There's currently a bug when querying transactions that doesn't have to do with typing. Let's fix this first.

### Testing
Let's add some unit tests for this endpoint in `tests/test_transactions.py`.

Tests can be run with `pytest`

### Transaction Typing
Currently our transaction types are unrecognized. We'll do a simple version of typing where we want to categorize these transactions into BUY/SELL/GAS or gas transactions.

### Multi-Wallet Support
Often times we query multiple wallets at once. How can we change the endpoint to support that.

As we add more wallets we also have to consider our resources. How can we update the logic to improve performance and prevent spam or bad requests?
