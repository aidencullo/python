from test_string_filter import test_filter_strs
from test_number_filter import test_filter_divisible_by_three

def main():
    """Main function to run all filter tests"""
    print("Running filter tests...")
    test_filter_strs()
    test_filter_divisible_by_three()
    print("All tests completed!")

if __name__ == "__main__":
    main()
