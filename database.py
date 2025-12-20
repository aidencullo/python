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
        self.tables = defaultdict(list)
    
    def insert(self, table_name, record):

        table = self.tables[table_name]

        record_id = record["id"]
        for row in table:
            id = row["id"]
            if id == record_id:
                for attr in record:
                    row[attr] = record[attr]
                return
        table.append(record)


    def select(self, table_name, target_column_names):
        if table_name not in self.tables:
            return []   

        table = self.tables[table_name]
        results = []

        for row in table:
            row_result = {}
            for target_column_name in target_column_names:
                row_result[target_column_name] = None

            for target_column_name in target_column_names:
                for column_name in row:
                    if column_name == target_column_name:
                        row_result[target_column_name] = row[column_name]
            results.append(row_result)

        return results

    def select_where(self, table_name, predicate):
        if table_name not in self.tables:
            return []   

        table = self.tables[table_name]
        return [row for row in table if predicate(row)]

db = Database()
# db.insert("employees", {"id": "0", "name": "Andrew Wang", "email": "andrew.wang@email.com"})
# db.select("employees", ["name"])

assert db.select("employees", "name") == []
db.insert("employees", {"id": "0", "name": "Andrew Wang", "email": "andrew.wang@email.com"})
db.insert("employees", {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"})
db.insert("employees", {"id": "2", "email": "help@email.com"})
db.insert("employees", {"id": "2", "email": "support@email.com"})
# assert db.select("employees", ["name", "email"]) == [{"name": "Andrew Wang"}, {"name": "Jon Hsu"}, {"name": None}]

assert db.select("employees", ["name", "email"]) == [{'name': 'Andrew Wang', 'email': 'andrew.wang@email.com'}, {'name': 'Jon Hsu', 'email': 'jon.hsu@email.com'}, {'name': None, 'email': 'support@email.com'}]


# support WHERE clauses
#   `SELECT name FROM employees WHERE email = 'jon.hsu@email.com' AND id > '0'`


def test_predicate(record):
    return record["email"] == "jon.hsu@email.com" and int(record["id"]) > 0

assert db.select_where("employees", test_predicate) == [{"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"}]
# print(db.select_where("employees", test_predicate))