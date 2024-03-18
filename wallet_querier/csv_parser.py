import csv


def parse_csv():
    FILE_NAME = "./ETH_USD.csv"

    res = []
    with open(FILE_NAME) as file:
        reader = csv.DictReader(file)
        for row in reader:
            res.append({
                "date": row["Date"],
                "price": row["Close"],
            })

    return res
