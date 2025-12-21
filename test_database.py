import unittest
from database import Database


class TestDatabase(unittest.TestCase):
    """Test suite for Database class"""
    
    def test_empty_database(self):
        """Test 1: Querying an empty database returns empty results"""
        db = Database()
        self.assertEqual(db.select("employees", ["name"]), [], 
                        "Expected empty list when querying empty database")
        self.assertEqual(db.select("employees", ["name", "email"]), [],
                        "Expected empty list when querying empty database with multiple columns")
        self.assertEqual(db.select("nonexistent_table", ["any_column"]), [],
                        "Expected empty list when querying nonexistent table")

    def test_add_single_employee(self):
        """Test 2: Adding and querying a single employee"""
        db = Database()
        db.insert("employees", {"id": "0", "name": "Alice Smith", "email": "alice@email.com"})
        
        result = db.select("employees", ["name"])
        expected = [{"name": "Alice Smith"}]
        self.assertEqual(result, expected, 
                        f"Expected {expected}, but got {result}")
        
        result = db.select("employees", ["name", "email"])
        expected = [{"name": "Alice Smith", "email": "alice@email.com"}]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
        
        result = db.select("employees", ["id", "name", "email"])
        expected = [{"id": "0", "name": "Alice Smith", "email": "alice@email.com"}]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")

    def test_add_multiple_employees(self):
        """Test 3: Adding multiple employees with different fields"""
        db = Database()
        db.insert("employees", {"id": "0", "name": "Andrew Wang", "email": "andrew.wang@email.com"})
        db.insert("employees", {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"})
        db.insert("employees", {"id": "2", "name": "Bob Johnson", "email": "bob@email.com", "department": "Engineering"})
        
        result = db.select("employees", ["name"])
        expected = [
            {"name": "Andrew Wang"},
            {"name": "Jon Hsu"},
            {"name": "Bob Johnson"}
        ]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
        
        result = db.select("employees", ["name", "email"])
        expected = [
            {"name": "Andrew Wang", "email": "andrew.wang@email.com"},
            {"name": "Jon Hsu", "email": "jon.hsu@email.com"},
            {"name": "Bob Johnson", "email": "bob@email.com"}
        ]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")

    def test_add_same_employee_twice(self):
        """Test 4: Adding the same employee ID twice should update the record"""
        db = Database()
        db.insert("employees", {"id": "2", "email": "help@email.com"})
        db.insert("employees", {"id": "2", "email": "support@email.com"})
        
        # The second insert should update the first one, not create a duplicate
        result = db.select("employees", ["id", "email"])
        self.assertEqual(len(result), 1,
                        f"Expected 1 record, but got {len(result)} records: {result}")
        expected = [{"id": "2", "email": "support@email.com"}]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
        
        # Test updating with additional fields
        db.insert("employees", {"id": "2", "email": "support@email.com", "name": "Support Team"})
        result = db.select("employees", ["id", "name", "email"])
        expected = [{"id": "2", "name": "Support Team", "email": "support@email.com"}]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")

    def test_employee_with_missing_fields(self):
        """Test 5: Employees with missing fields should return None for those fields"""
        db = Database()
        db.insert("employees", {"id": "0", "name": "Andrew Wang", "email": "andrew.wang@email.com"})
        db.insert("employees", {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"})
        db.insert("employees", {"id": "2", "email": "help@email.com"})  # Missing name
        
        result = db.select("employees", ["name", "email"])
        expected = [
            {"name": "Andrew Wang", "email": "andrew.wang@email.com"},
            {"name": "Jon Hsu", "email": "jon.hsu@email.com"},
            {"name": None, "email": "help@email.com"}
        ]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")

    def test_select_specific_columns(self):
        """Test 6: Selecting only specific columns from employees"""
        db = Database()
        db.insert("employees", {"id": "0", "name": "Alice", "email": "alice@email.com", "age": "30", "department": "Sales"})
        db.insert("employees", {"id": "1", "name": "Bob", "email": "bob@email.com", "age": "25"})
        db.insert("employees", {"id": "2", "name": "Charlie", "email": "charlie@email.com"})  # Missing age
        
        # Select only name
        result = db.select("employees", ["name"])
        expected = [{"name": "Alice"}, {"name": "Bob"}, {"name": "Charlie"}]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
        
        # Select only email
        result = db.select("employees", ["email"])
        expected = [{"email": "alice@email.com"}, {"email": "bob@email.com"}, {"email": "charlie@email.com"}]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
        
        # Select name and age (one employee missing age)
        result = db.select("employees", ["name", "age"])
        expected = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}, {"name": "Charlie", "age": None}]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")

    def test_select_where_basic(self):
        """Test 7: Basic select_where functionality"""
        db = Database()
        db.insert("employees", {"id": "0", "name": "Andrew Wang", "email": "andrew.wang@email.com"})
        db.insert("employees", {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"})
        db.insert("employees", {"id": "2", "name": "Bob", "email": "bob@email.com"})
        
        # Filter by email
        def email_predicate(record):
            return record["email"] == "jon.hsu@email.com"
        
        result = db.select_where("employees", email_predicate)
        expected = [{"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"}]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
        
        # Filter by id > 0
        def id_predicate(record):
            return int(record["id"]) > 0
        
        result = db.select_where("employees", id_predicate)
        self.assertEqual(len(result), 2,
                        f"Expected 2 records, but got {len(result)}: {result}")
        expected_record1 = {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"}
        expected_record2 = {"id": "2", "name": "Bob", "email": "bob@email.com"}
        self.assertIn(expected_record1, result,
                     f"Expected {expected_record1} to be in {result}")
        self.assertIn(expected_record2, result,
                     f"Expected {expected_record2} to be in {result}")

    def test_select_where_complex(self):
        """Test 8: Complex select_where with multiple conditions"""
        db = Database()
        db.insert("employees", {"id": "0", "name": "Andrew Wang", "email": "andrew.wang@email.com"})
        db.insert("employees", {"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"})
        db.insert("employees", {"id": "2", "name": "Bob", "email": "bob@email.com"})
        
        # Complex predicate: email matches AND id > 0
        def complex_predicate(record):
            return record["email"] == "jon.hsu@email.com" and int(record["id"]) > 0
        
        result = db.select_where("employees", complex_predicate)
        expected = [{"id": "1", "name": "Jon Hsu", "email": "jon.hsu@email.com"}]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
        
        # Predicate that matches nothing
        def no_match_predicate(record):
            return record["email"] == "nonexistent@email.com"
        
        result = db.select_where("employees", no_match_predicate)
        self.assertEqual(result, [],
                        f"Expected empty list, but got {result}")

    def test_multiple_tables(self):
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
        expected = [{"name": "Alice"}, {"name": "Bob"}]
        self.assertEqual(employees, expected,
                        f"Expected {expected}, but got {employees}")
        
        products = db.select("products", ["name", "price"])
        expected = [{"name": "Laptop", "price": "999"}, {"name": "Mouse", "price": "29"}]
        self.assertEqual(products, expected,
                        f"Expected {expected}, but got {products}")
        
        orders = db.select("orders", ["customer", "product"])
        expected = [{"customer": "Alice", "product": "Laptop"}]
        self.assertEqual(orders, expected,
                        f"Expected {expected}, but got {orders}")
        
        # Empty table should return empty
        result = db.select("customers", ["name"])
        self.assertEqual(result, [],
                        f"Expected empty list for nonexistent table, but got {result}")

    def test_edge_cases(self):
        """Test 10: Edge cases and boundary conditions"""
        db = Database()
        
        # Empty string id
        db.insert("employees", {"id": "", "name": "Empty ID", "email": "empty@email.com"})
        result = db.select("employees", ["name"])
        expected = [{"name": "Empty ID"}]
        self.assertEqual(result, expected,
                        f"Expected {expected}, but got {result}")
        
        # Very long id
        long_id = "a" * 100
        db.insert("employees", {"id": long_id, "name": "Long ID", "email": "long@email.com"})
        result = db.select("employees", ["name"])
        self.assertEqual(len(result), 2,
                        f"Expected 2 records, but got {len(result)}: {result}")
        
        # Update empty id record
        db.insert("employees", {"id": "", "name": "Updated Empty ID", "email": "updated@email.com"})
        result = db.select("employees", ["id", "name", "email"])
        expected_record = {"id": "", "name": "Updated Empty ID", "email": "updated@email.com"}
        self.assertIn(expected_record, result,
                     f"Expected {expected_record} to be in {result}")
        
        # Select non-existent columns
        result = db.select("employees", ["nonexistent_column"])
        self.assertTrue(all("nonexistent_column" in row and row["nonexistent_column"] is None for row in result),
                       f"Expected all rows to have 'nonexistent_column' as None, but got {result}")
        
        # select_where on empty table
        def any_predicate(record):
            return True
        result = db.select_where("empty_table", any_predicate)
        self.assertEqual(result, [],
                        f"Expected empty list for empty table, but got {result}")

    def test_large_dataset(self):
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
        self.assertEqual(len(result), 50,
                        f"Expected 50 records, but got {len(result)}")
        
        # Verify specific employees
        result = db.select("employees", ["name", "email"])
        expected_record1 = {"name": "Employee 0", "email": "employee0@email.com"}
        expected_record2 = {"name": "Employee 49", "email": "employee49@email.com"}
        self.assertIn(expected_record1, result,
                     f"Expected {expected_record1} to be in result")
        self.assertIn(expected_record2, result,
                     f"Expected {expected_record2} to be in result")
        
        # Use select_where to filter
        def engineering_predicate(record):
            return record.get("department") == "Engineering"
        
        engineering_employees = db.select_where("employees", engineering_predicate)
        self.assertEqual(len(engineering_employees), 25,
                        f"Expected 25 Engineering employees, but got {len(engineering_employees)}")


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestDatabase)
    runner = unittest.TextTestRunner(verbosity=2, failfast=True)
    runner.run(suite)

