import time
import sys
import os
import psycopg2

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import App

total = 0


def setup():
    global start, passed, total
    passed = 0
    start = time.time()


def teardown():
    end = time.time()
    print(f"Time: {end-start}s")
    print(f"Test passed : {passed}/{total}")


def run():
    setup()
    test_save_event_to_database()
    delete_test_event_to_database()
    teardown()


def test_save_event_to_database():
    global passed, total

    app = App()
    app.save_event_to_database("2024-03-12 20:09:22", 9999.9)

    total += 1
    DATABASE_URL = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('SELECT * FROM "Oxygene" WHERE temperature=9999.9;')
    fetch = cur.fetchall()
    if len(fetch) > 0:
        passed += 1


def delete_test_event_to_database():
    global passed, total

    DATABASE_URL = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(DATABASE_URL)

    cur = conn.cursor()

    cur.execute("""DELETE FROM "Oxygene" WHERE temperature=9999.9""")
    print("Data deleted successfully!")
    conn.commit()

    total += 1
    cur.execute('SELECT * FROM "Oxygene" WHERE temperature=9999.9;')
    fetch = cur.fetchall()
    if len(fetch) == 0:
        passed += 1


run()
