import csv
import os

def load_csv(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"CSV file '{filename}' not found")

    with open(filename, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
