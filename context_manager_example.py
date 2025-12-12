class Connection:
    def __enter__(self):
        print("ENTER: starting transaction")
        print("BEGIN")
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            print("EXIT: no exception -> COMMIT")
            print("COMMIT")
        else:
            print(f"EXIT: exception -> ROLLBACK ({exc_type.__name__}: {exc})")
            print("ROLLBACK")
        print("EXIT COMPLETE")
        return False  # re-raise exceptions if any

    def execute(self, sql):
        print(f"EXECUTE: {sql}")


# Normal flow
print("=== NORMAL CASE ===")
try:
    with Connection() as conn:
        conn.execute("INSERT INTO users VALUES (1, 'ok')")
        print("BODY: finished work")
except Exception:
    pass


# Exceptional flow
print("\n=== EXCEPTION CASE ===")
try:
    with Connection() as conn:
        conn.execute("INSERT INTO users VALUES (2, 'fail')")
        print("BODY: raising error")
        raise ValueError("boom")
except Exception as e:
    print(f"EXCEPTION PROPAGATED: {e}")
