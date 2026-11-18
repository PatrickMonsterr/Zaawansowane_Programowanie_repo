import sqlite3
import sys

DB_FILE = "queue.db"

count = int(sys.argv[1]) if len(sys.argv) > 1 else 1

conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS jobs ("
    "id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "status TEXT NOT NULL)"
)
for _ in range(count):
    cur.execute("INSERT INTO jobs (status) VALUES ('pending')")
conn.commit()
conn.close()

print(f"Dodano {count} zadan.")
