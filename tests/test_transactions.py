def test_get_transactions(client):
    response = client.get("/transactions/0x539C92186f7C6CC4CbF443F26eF84C595baBBcA1")
    print(response)
