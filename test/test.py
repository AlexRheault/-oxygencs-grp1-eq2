import os
import sys
import time
import psycopg2

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.main import App

TOTAL = 0


def setup():
    global start, passed, TOTAL
    passed = 0
    start = time.time()


def teardown():
    end = time.time()
    print(f"Time: {end-start}s")
    print(f"Test passed : {passed}/{TOTAL}")


def run():
    setup()
    test_save_event_to_database()
    delete_test_event_to_database()
    teardown()


def test_save_event_to_database():
    global passed, TOTAL

    app = App()
    app.save_event_to_database("2024-03-12 20:09:22", 9999.9)

    TOTAL += 1
    database_url = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(database_url)
    cur = conn.cursor()
    cur.execute('SELECT * FROM "Oxygene" WHERE temperature=9999.9;')
    fetch = cur.fetchall()
    if len(fetch) > 0:
        passed += 1


def delete_test_event_to_database():
    global passed, TOTAL

    database_url = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(database_url)

    cur = conn.cursor()

    cur.execute("""DELETE FROM "Oxygene" WHERE temperature=9999.9""")
    print("Data deleted successfully!")
    conn.commit()

    TOTAL += 1
    cur.execute('SELECT * FROM "Oxygene" WHERE temperature=9999.9;')
    fetch = cur.fetchall()
    if len(fetch) == 0:
        passed += 1


run()
