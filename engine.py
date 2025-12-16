def apply_where(rows, where):
    if not where:
        return rows

    col, op, val = where.values()
    result = []

    for row in rows:
        if col not in row:
            raise ValueError(f"Column '{col}' does not exist")

        cell = row[col]
        try:
            cell = int(cell)
        except:
            pass

        if (
            (op == "=" and cell == val) or
            (op == "!=" and cell != val) or
            (op == ">" and cell > val) or
            (op == "<" and cell < val) or
            (op == ">=" and cell >= val) or
            (op == "<=" and cell <= val)
        ):
            result.append(row)

    return result


def apply_select(rows, select):
    if select == "*":
        return rows

    output = []
    for row in rows:
        projected = {}
        for col in select:
            if col not in row:
                raise ValueError(f"Column '{col}' does not exist")
            projected[col] = row[col]
        output.append(projected)
    return output


def apply_count(rows, target):
    if target == "*":
        return len(rows)
    return sum(1 for r in rows if r.get(target))


def execute_query(data, parsed):
    rows = apply_where(data, parsed["where"])

    if isinstance(parsed["select"], dict):
        return apply_count(rows, parsed["select"]["count"])

    return apply_select(rows, parsed["select"])
