import csv
import json
from urllib.parse import urlparse

def csv_to_json(csv_file_path, json_file_path):
    # Read CSV and convert to JSON
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        data = []
        for row in csv_reader:
            source = row["source"]
            relative_source = urlparse(source).path

            new_row = {
                "source": relative_source,
                "target": row["destination"]
            }
            data.append(new_row)

    # Write JSON to file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)

    print(f"JSON data has been written to {json_file_path}")

def main():
    filename = input("Enter the name of the input CSV file (e.g., input.csv): ")
    input_csv = f"{filename}.csv"
    output_json = f"{filename}_output.json"
    csv_to_json(input_csv, output_json)

if __name__ == "__main__":
    main()

