import csv


def parse_csv():
    FILE_NAME = "./ETH_1H.csv"

    res = []
    with open(FILE_NAME) as file:
        reader = csv.DictReader(file)
        for row in reader:
            res.append({
                "timestamp": row["Unix Timestamp"],
                "date": row["Date"],
                "price": row["Open"],
            })

    return res
