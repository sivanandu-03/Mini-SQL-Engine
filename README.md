# Mini SQL Database Engine (Python)

## Overview
This project is a simple, in-memory SQL database engine implemented using Python.  
It demonstrates how basic SQL queries are parsed and executed internally without using any database system.

The engine loads data from a CSV file into memory and allows users to execute a limited set of SQL queries through a command-line interface (CLI).  
This project is intentionally kept simple to focus on core data processing and SQL execution concepts.

---

## Features Supported
This engine supports a limited subset of SQL:

- `SELECT *`
- `SELECT column1, column2`
- `FROM <table>`
- `WHERE` clause with **one condition**
- Supported operators: `=`, `!=`, `>`, `<`, `>=`, `<=`
- Aggregation functions:
  - `COUNT(*)`
  - `COUNT(column_name)`

## Features Not Supported
The following SQL features are **intentionally not implemented**:

- INSERT, UPDATE, DELETE
- JOIN
- GROUP BY
- ORDER BY
- HAVING
- Multiple WHERE conditions (`AND`, `OR`)
- Other aggregate functions (`SUM`, `AVG`, etc.)

---

## Project Structure
```text
Mini-SQL-Engine/
│
├── cli.py                   # Command-line interface (entry point)
├── parser.py                # SQL parsing logic
├── engine.py                # Query execution logic
├── storage.py               # CSV loading logic
├── students_marks_wide.csv  # Sample dataset (10 students)
└── README.md
````

-----

## Sample Dataset

The file `students_marks_wide.csv` contains data of **10 students**, where:

  - Each student occupies **one row**
  - Each row contains marks for **5 subjects**

### Columns

  - `id`
  - `name`
  - `maths`
  - `science`
  - `english`
  - `social`
  - `computer`

-----

## How to Run the Application

### Step 1: Prerequisites

Ensure Python is installed (Python 3.8 or higher is recommended).

Check Python version:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone [https://github.com/sivanandu-03/Mini-SQL-Engine](https://github.com/sivanandu-03/Mini-SQL-Engine)
cd Mini-SQL-Engine
```

### Step 3: Run the Application

```bash
python cli.py
```

### Step 4: Load the CSV File

When prompted:

```text
Enter CSV file name:
```

Enter:

```text
students_marks_wide.csv
```

### Step 5: Execute SQL Queries

You will see the SQL prompt:

```text
sql>
```

**Example Queries**

```sql
SELECT * FROM students_marks_wide;
SELECT name, maths FROM students_marks_wide WHERE maths > 80;
SELECT COUNT(*) FROM students_marks_wide;
SELECT COUNT(science) FROM students_marks_wide;
```

### Step 6: Exit the Application

```text
exit
```

or

```text
quit
```

-----

## Error Handling

The engine provides clear error messages for:

  - Invalid SQL syntax
  - Unsupported SQL commands
  - Non-existent columns
  - Incorrect WHERE clause
  - Missing CSV file

**Example:**

```text
Error: Column 'salary' does not exist
```

-----

## Implementation Details

  - **Storage:** Data is stored in memory as a list of dictionaries.
  - **Parsing:** SQL parsing is done using basic string operations and regular expressions.
  - **Query execution flow:**
    1.  Load data from CSV
    2.  Apply WHERE filtering
    3.  Apply COUNT aggregation (if used)
    4.  Apply SELECT projection
  - **Interface:** A simple REPL (Read–Eval–Print Loop) is used for interaction.

## Limitations

  - Only one table (CSV file) is supported.
  - Only one WHERE condition is allowed.
  - No advanced SQL functionality.

*These limitations are intentional and aligned with beginner-level task requirements.*

## Learning Outcomes

  - Understanding how SQL queries are parsed internally.
  - Implementing in-memory data processing.
  - Writing a simple query execution engine.
  - Building a CLI-based Python application.
  - Handling user input and errors gracefully.

<!-- end list -->

```
```