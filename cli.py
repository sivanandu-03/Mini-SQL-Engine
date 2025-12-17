from parser import parse_sql
from engine import execute_query


def print_table(result):
    """
    Prints query results in a table format.
    """
    if isinstance(result, int):
        print(result)
        return

    if not result:
        print("No rows found")
        return

    headers = result[0].keys()
    rows = [list(row.values()) for row in result]

    # Calculate column widths
    col_widths = [
        max(len(str(item)) for item in [header] + [row[i] for row in rows])
        for i, header in enumerate(headers)
    ]

    # Print header
    header_row = " | ".join(
        header.ljust(col_widths[i]) for i, header in enumerate(headers)
    )
    separator = "-+-".join("-" * col_widths[i] for i in range(len(headers)))

    print(header_row)
    print(separator)

    # Print rows
    for row in rows:
        print(" | ".join(str(row[i]).ljust(col_widths[i]) for i in range(len(row))))


def main():
    print("Mini SQL Engine")
    print("Type 'exit' or 'quit' to leave")

    while True:
        query = input("sql> ").strip()

        if query.lower() in ("exit", "quit"):
            print("Exiting...")
            break

        try:
            parsed = parse_sql(query)
            result = execute_query(parsed)
            print_table(result)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
