import re

def parse_sql(query):
    query = query.strip().rstrip(";")

    query_upper = query.upper()

    if not query_upper.startswith("SELECT"):
        raise ValueError("Only SELECT queries are supported")

    parsed = {}

    # -------- SELECT PART --------
    select_match = re.search(r"SELECT\s+(.*?)\s+FROM", query_upper)
    if not select_match:
        raise ValueError("Invalid SELECT syntax")

    select_part = select_match.group(1).strip()

    if select_part.startswith("COUNT"):
        inside = select_part[6:-1].strip()
        parsed["select"] = {"count": inside.lower()}
    elif select_part == "*":
        parsed["select"] = "*"
    else:
        parsed["select"] = [c.strip().lower() for c in select_part.split(",")]

    # -------- FROM PART --------
    from_match = re.search(r"FROM\s+(\w+)", query_upper)
    if not from_match:
        raise ValueError("Invalid FROM clause")

    parsed["from"] = from_match.group(1).lower()

    # -------- WHERE PART --------
    where_match = re.search(r"WHERE\s+(.*)", query, re.IGNORECASE)
    if where_match:
        condition = where_match.group(1).strip()
        match = re.match(r"(\w+)\s*(=|!=|>=|<=|>|<)\s*(.+)", condition)
        if not match:
            raise ValueError("Invalid WHERE clause")

        col, op, val = match.groups()
        val = val.strip().strip("'\"")

        if val.isdigit():
            val = int(val)

        parsed["where"] = {
            "column": col.lower(),
            "operator": op,
            "value": val
        }
    else:
        parsed["where"] = None

    return parsed
