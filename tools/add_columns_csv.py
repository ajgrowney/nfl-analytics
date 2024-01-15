
import csv
from argparse import ArgumentParser

def add_columns(csv_file, column_names, display_col:str):

    # Read the CSV file and get the current rows
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    # Add the new column header if it doesn't exist
    fieldnames = reader.fieldnames + column_names
    for column_name in column_names:
        if column_name not in reader.fieldnames:
            rows[0][column_name] = column_name
    
    # Add data to the corresponding rows
    for row in rows:  # Skip the header row
        for column_name in column_names:
            data = input(f"{row[display_col]} {column_name}: ")
            row[column_name] = data
    
    # Write the updated rows back to the CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("--filename", help="name of csv file to be appended")
    p.add_argument("--display", help="row data to display")
    p.add_argument("columns", nargs="+", help="list of column names")
    args = p.parse_args()
    add_columns(f"data/{args.filename}", args.columns, args.display)
