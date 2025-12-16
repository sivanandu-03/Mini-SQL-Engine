from storage import load_csv
from parser import parse_sql
from engine import execute_query

def print_result(result):
    if isinstance(result, int):
        print("\nCOUNT")
        print("-----")
        print(result)
        return

    if not result:
        print("No rows found")
        return

    headers = result[0].keys()
    print("\t".join(headers))
    for row in result:
        print("\t".join(row.values()))


def main():
    filename = input("Enter CSV file name: ")
    data = load_csv(filename)

    print("Mini SQL Engine (type 'exit' to quit)")
    while True:
        try:
            query = input("sql> ")
            if query.lower() in ("exit", "quit"):
                break

            parsed = parse_sql(query)
            result = execute_query(data, parsed)
            print_result(result)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
