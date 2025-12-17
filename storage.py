import csv
import os


def load_csv(file_path):
    """
    Loads a CSV file into memory as a list of dictionaries.
    Each dictionary represents a row.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file '{file_path}' not found")

    with open(file_path, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV file is empty")

    return rows
