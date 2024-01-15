"""Command line tool for building csv files via user input
"""

import csv
from argparse import ArgumentParser

def build_csv(filename:str, columns:list):
    """
    :param filename: name of csv file to be created
    :param columns: list of column names
    """
    with open(f"data/{filename}.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        try:
            while True:
                row = [input(f"{column}: ") for column in columns]
                writer.writerow(row)
        except KeyboardInterrupt:
            print("Done")

if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("--filename", help="name of csv file to be created")
    p.add_argument("columns", nargs="+", help="list of column names")
    args = p.parse_args()
    build_csv(args.filename, args.columns)