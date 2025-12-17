def parse_sql(query):
    """
    Parses a simplified SQL query.
    Supports SELECT, FROM, WHERE, and COUNT.
    """

    query = query.strip().rstrip(";")
    tokens = query.lower().split()

    if not query.lower().startswith("select"):
        raise ValueError("Syntax error: Query must start with SELECT")

    if "from" not in tokens:
        raise ValueError("Syntax error: FROM clause missing")

    select_part = query[query.lower().find("select") + 6: query.lower().find("from")].strip()
    from_part = query[query.lower().find("from") + 4:].strip()

    where_clause = None
    if "where" in from_part.lower():
        from_part, where_part = from_part.lower().split("where", 1)
        where_clause = where_part.strip()

    table_name = from_part.strip()

    # Handle COUNT
    if select_part.lower().startswith("count"):
        col = select_part[select_part.find("(") + 1: select_part.find(")")].strip()
        return {
            "type": "count",
            "column": col,
            "table": table_name,
            "where": parse_where(where_clause) if where_clause else None
        }

    # Handle SELECT columns
    if select_part == "*":
        columns = ["*"]
    else:
        columns = [c.strip() for c in select_part.split(",")]

    return {
        "type": "select",
        "columns": columns,
        "table": table_name,
        "where": parse_where(where_clause) if where_clause else None
    }


def parse_where(where_str):
    """
    Parses a single WHERE condition.
    """
    operators = ["<=", ">=", "!=", "=", "<", ">"]

    for op in operators:
        if op in where_str:
            col, val = where_str.split(op, 1)
            return {
                "column": col.strip(),
                "operator": op,
                "value": val.strip().strip("'")
            }

    raise ValueError("Syntax error: Invalid WHERE condition")
