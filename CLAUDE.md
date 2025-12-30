# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running Tests

This repository uses Python's `unittest` framework with a specific configuration.

### Run all tests
```bash
python test_database.py
```

### Run tests from within database.py
```bash
python database.py
```
The database.py file has a `__main__` block that imports and runs tests from test_database.py with `failfast=True` and `verbosity=2`.

### Run other test files
```bash
python test_number_filter.py
python test_string_filter.py
```

## Architecture

### database.py - In-Memory Database

The main component is a lightweight in-memory database (`Database` class) that implements SQL-like operations:

- **Storage**: Uses `defaultdict(dict)` to store multiple tables, where each table is a dict keyed by record ID
- **Insert**: Records are stored/updated by their `id` field (upsert behavior)
- **Select**: Projects specific columns from a table, returning `None` for missing fields
- **Select Where**: Filters records using a predicate function (e.g., `lambda record: int(record["id"]) > 0`)

Key design decisions:
- All records must have an `id` field (used as primary key)
- Missing fields in records return `None` when selected
- Inserting a record with an existing ID updates the record (not a duplicate)
- Tables are created automatically on first insert
