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
        table = self.tables[table_name]
        return [row for row in table if predicate(row)]


def test_empty_database():
    """Test 1: Querying an empty database returns empty results"""
    db = Database()
    assert db.select("employees", ["name"]) == []
    assert db.select("employees", ["name", "email"]) == []
    assert db.select("nonexistent_table", ["any_column"]) == []
    print("✓ Test 1 passed: Empty database queries return empty results")


def test_add_single_employee():
    """Test 2: Adding and querying a single employee"""
    db = Database()
    db.insert("employees", {"id": "0", "name": "Alice Smith", "email": "alice@email.com"})
    
    result = db.select("employees", ["name"])
    assert result == [{"name": "Alice Smith"}]
    
    result = db.select("employees", ["name", "email"])
    assert result == [{"name": "Alice Smith", "email": "alice@email.com"}]
    
    result = db.select("employees", ["id", "name", "email"])
    assert result == [{"id": "0", "name": "Alice Smith", "email": "alice@email.com"}]
    print("✓ Test 2 passed: Single employee insertion and selection")


def test_add_multiple_employees():
    """Test 3: Adding multiple employees with different fields"""
    db = Database()
    db.insert("employees", {"id": "0", "name": "Andrew Wang", "email": "andrew.wang@email.com"})
    db.insert("employees", {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"})
    db.insert("employees", {"id": "2", "name": "Bob Johnson", "email": "bob@email.com", "department": "Engineering"})
    
    result = db.select("employees", ["name"])
    assert result == [
        {"name": "Andrew Wang"},
        {"name": "Jon Hsu"},
        {"name": "Bob Johnson"}
    ]
    
    result = db.select("employees", ["name", "email"])
    assert result == [
        {"name": "Andrew Wang", "email": "andrew.wang@email.com"},
        {"name": "Jon Hsu", "email": "jon.hsu@email.com"},
        {"name": "Bob Johnson", "email": "bob@email.com"}
    ]
    print("✓ Test 3 passed: Multiple employees insertion and selection")


def test_add_same_employee_twice():
    """Test 4: Adding the same employee ID twice should update the record"""
    db = Database()
    db.insert("employees", {"id": "2", "email": "help@email.com"})
    db.insert("employees", {"id": "2", "email": "support@email.com"})
    
    # The second insert should update the first one, not create a duplicate
    result = db.select("employees", ["id", "email"])
    assert len(result) == 1
    assert result == [{"id": "2", "email": "support@email.com"}]
    
    # Test updating with additional fields
    db.insert("employees", {"id": "2", "email": "support@email.com", "name": "Support Team"})
    result = db.select("employees", ["id", "name", "email"])
    assert result == [{"id": "2", "name": "Support Team", "email": "support@email.com"}]
    print("✓ Test 4 passed: Adding same employee twice updates the record")


def test_employee_with_missing_fields():
    """Test 5: Employees with missing fields should return None for those fields"""
    db = Database()
    db.insert("employees", {"id": "0", "name": "Andrew Wang", "email": "andrew.wang@email.com"})
    db.insert("employees", {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"})
    db.insert("employees", {"id": "2", "email": "help@email.com"})  # Missing name
    
    result = db.select("employees", ["name", "email"])
    assert result == [
        {"name": "Andrew Wang", "email": "andrew.wang@email.com"},
        {"name": "Jon Hsu", "email": "jon.hsu@email.com"},
        {"name": None, "email": "help@email.com"}
    ]
    print("✓ Test 5 passed: Missing fields return None")


def test_select_specific_columns():
    """Test 6: Selecting only specific columns from employees"""
    db = Database()
    db.insert("employees", {"id": "0", "name": "Alice", "email": "alice@email.com", "age": "30", "department": "Sales"})
    db.insert("employees", {"id": "1", "name": "Bob", "email": "bob@email.com", "age": "25"})
    db.insert("employees", {"id": "2", "name": "Charlie", "email": "charlie@email.com"})  # Missing age
    
    # Select only name
    result = db.select("employees", ["name"])
    assert result == [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
    
    # Select only email
    result = db.select("employees", ["email"])
    assert result == [{"email": "alice@email.com"}, {"email": "bob@email.com"}, {"email": "charlie@email.com"}]
    
    # Select name and age (one employee missing age)
    result = db.select("employees", ["name", "age"])
    assert result == [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}, {"name": "Charlie", "age": None}]
    print("✓ Test 6 passed: Selecting specific columns works correctly")


def test_select_where_basic():
    """Test 7: Basic select_where functionality"""
    db = Database()
    db.insert("employees", {"id": "0", "name": "Andrew Wang", "email": "andrew.wang@email.com"})
    db.insert("employees", {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"})
    db.insert("employees", {"id": "2", "name": "Bob", "email": "bob@email.com"})
    
    # Filter by email
    def email_predicate(record):
        return record["email"] == "jon.hsu@email.com"
    
    result = db.select_where("employees", email_predicate)
    assert result == [{"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"}]
    
    # Filter by id > 0
    def id_predicate(record):
        return int(record["id"]) > 0
    
    result = db.select_where("employees", id_predicate)
    assert len(result) == 2
    assert {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"} in result
    assert {"id": "2", "name": "Bob", "email": "bob@email.com"} in result
    print("✓ Test 7 passed: Basic select_where functionality")


def test_select_where_complex():
    """Test 8: Complex select_where with multiple conditions"""
    db = Database()
    db.insert("employees", {"id": "0", "name": "Andrew Wang", "email": "andrew.wang@email.com"})
    db.insert("employees", {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"})
    db.insert("employees", {"id": "2", "name": "Bob", "email": "bob@email.com"})
    
    # Complex predicate: email matches AND id > 0
    def complex_predicate(record):
        return record["email"] == "jon.hsu@email.com" and int(record["id"]) > 0
    
    result = db.select_where("employees", complex_predicate)
    assert result == [{"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"}]
    
    # Predicate that matches nothing
    def no_match_predicate(record):
        return record["email"] == "nonexistent@email.com"
    
    result = db.select_where("employees", no_match_predicate)
    assert result == []
    print("✓ Test 8 passed: Complex select_where conditions")


def test_multiple_tables():
    """Test 9: Database supports multiple different tables"""
    db = Database()
    
    # Insert into employees table
    db.insert("employees", {"id": "0", "name": "Alice", "email": "alice@email.com"})
    db.insert("employees", {"id": "1", "name": "Bob", "email": "bob@email.com"})
    
    # Insert into products table
    db.insert("products", {"id": "0", "name": "Laptop", "price": "999"})
    db.insert("products", {"id": "1", "name": "Mouse", "price": "29"})
    
    # Insert into orders table
    db.insert("orders", {"id": "0", "customer": "Alice", "product": "Laptop"})
    
    # Query each table independently
    employees = db.select("employees", ["name"])
    assert employees == [{"name": "Alice"}, {"name": "Bob"}]
    
    products = db.select("products", ["name", "price"])
    assert products == [{"name": "Laptop", "price": "999"}, {"name": "Mouse", "price": "29"}]
    
    orders = db.select("orders", ["customer", "product"])
    assert orders == [{"customer": "Alice", "product": "Laptop"}]
    
    # Empty table should return empty
    assert db.select("customers", ["name"]) == []
    print("✓ Test 9 passed: Multiple tables work independently")


def test_edge_cases():
    """Test 10: Edge cases and boundary conditions"""
    db = Database()
    
    # Empty string id
    db.insert("employees", {"id": "", "name": "Empty ID", "email": "empty@email.com"})
    result = db.select("employees", ["name"])
    assert result == [{"name": "Empty ID"}]
    
    # Very long id
    long_id = "a" * 100
    db.insert("employees", {"id": long_id, "name": "Long ID", "email": "long@email.com"})
    result = db.select("employees", ["name"])
    assert len(result) == 2
    
    # Update empty id record
    db.insert("employees", {"id": "", "name": "Updated Empty ID", "email": "updated@email.com"})
    result = db.select("employees", ["id", "name", "email"])
    assert {"id": "", "name": "Updated Empty ID", "email": "updated@email.com"} in result
    
    # Select non-existent columns
    result = db.select("employees", ["nonexistent_column"])
    assert all("nonexistent_column" in row and row["nonexistent_column"] is None for row in result)
    
    # select_where on empty table
    def any_predicate(record):
        return True
    result = db.select_where("empty_table", any_predicate)
    assert result == []
    print("✓ Test 10 passed: Edge cases handled correctly")


def test_large_dataset():
    """Test 11: Adding a bunch of employees (stress test)"""
    db = Database()
    
    # Add 50 employees
    for i in range(50):
        db.insert("employees", {
            "id": str(i),
            "name": f"Employee {i}",
            "email": f"employee{i}@email.com",
            "department": "Engineering" if i % 2 == 0 else "Sales"
        })
    
    # Verify all are inserted
    result = db.select("employees", ["id", "name"])
    assert len(result) == 50
    
    # Verify specific employees
    result = db.select("employees", ["name", "email"])
    assert {"name": "Employee 0", "email": "employee0@email.com"} in result
    assert {"name": "Employee 49", "email": "employee49@email.com"} in result
    
    # Use select_where to filter
    def engineering_predicate(record):
        return record.get("department") == "Engineering"
    
    engineering_employees = db.select_where("employees", engineering_predicate)
    assert len(engineering_employees) == 25  # Half should be Engineering
    
    print("✓ Test 11 passed: Large dataset insertion and querying")


def run_all_tests():
    """Run all test functions"""
    print("Running comprehensive database tests...\n")
    
    test_empty_database()
    test_add_single_employee()
    test_add_multiple_employees()
    test_add_same_employee_twice()
    test_employee_with_missing_fields()
    test_select_specific_columns()
    test_select_where_basic()
    test_select_where_complex()
    test_multiple_tables()
    test_edge_cases()
    test_large_dataset()
    
    print("\n✅ All tests passed!")


if __name__ == "__main__":
    run_all_tests()
