'''
We want to build a lightweight, in-memory database that supports basic table operations. 

We will start with inserting rows into tables. We should also be able to query specific columns from that table, similar to how SELECT works in SQL.
'''

# db = Database()
# db.insert("employees", {"id": "0", "name": "Andrew Wang", "email": "andrew.wang@email.com"})
# db.insert("employees", {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"})
# db.insert("employees", {"id": "2", "email": "help@email.com"})
# db.insert("employees", {"id": "2", "email": "support@email.com"})
# db.select("employees", ["name"])
# returns [{"name": "Andrew Wang"}, {"name": "Jon Hsu"}, {"name": None}]

# our select is effectively running `SELECT name FROM employees` against this database
# model and modify this class however you see fit

# support WHERE clauses
#   `SELECT name FROM employees WHERE email = 'jon.hsu@email.com' AND id > '0'`
# =, >, <

'''

WHERE id > '0'

def predicate(record):
    return int(record["id"]) > 0

db.select_where("employees", predicate)

def select_where(..., predicate):
    return [predicate(row) for row in table]

'''

from collections import defaultdict

class Database:

    def __init__(self):
        self.tables = defaultdict(dict)
    
    def insert(self, table_name, record):
        table = self.tables[table_name]
        id = record["id"]
        table[id] = record


    def select(self, table_name, target_column_names):
        table = self.tables[table_name]
        results = []

        for row in table.values():
            row_result = {key: row.get(key) for key in target_column_names}
            results.append(row_result)

        return results

    def select_where(self, table_name, predicate):
        table = self.tables[table_name]
        return [row for row in table.values() if predicate(row)]


if __name__ == "__main__":
    import unittest
    from test_database import TestDatabase
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestDatabase)
    runner = unittest.TextTestRunner(verbosity=2, failfast=True)
    runner.run(suite)
