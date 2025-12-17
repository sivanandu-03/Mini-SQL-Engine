from storage import load_csv


def execute_query(parsed_query):
    rows = load_csv(parsed_query["table"] + ".csv")

    if parsed_query["where"]:
        rows = apply_where(rows, parsed_query["where"])

    if parsed_query["type"] == "count":
        return execute_count(rows, parsed_query["column"])

    return execute_select(rows, parsed_query["columns"])


def apply_where(rows, where):
    col = where["column"]
    op = where["operator"]
    val = where["value"]

    if col not in rows[0]:
        raise ValueError(f"Column '{col}' does not exist")

    result = []

    for row in rows:
        cell = row[col]

        try:
            cell_val = float(cell)
            val_cmp = float(val)
        except ValueError:
            cell_val = cell
            val_cmp = val

        if compare(cell_val, val_cmp, op):
            result.append(row)

    return result


def compare(a, b, op):
    if op == "=":
        return a == b
    if op == "!=":
        return a != b
    if op == ">":
        return a > b
    if op == "<":
        return a < b
    if op == ">=":
        return a >= b
    if op == "<=":
        return a <= b
    return False


def execute_select(rows, columns):
    if columns == ["*"]:
        return rows

    for col in columns:
        if col not in rows[0]:
            raise ValueError(f"Column '{col}' does not exist")

    return [{col: row[col] for col in columns} for row in rows]


def execute_count(rows, column):
    if column == "*":
        return len(rows)

    if column not in rows[0]:
        raise ValueError(f"Column '{column}' does not exist for COUNT")

    return sum(1 for row in rows if row[column] not in ("", None))
