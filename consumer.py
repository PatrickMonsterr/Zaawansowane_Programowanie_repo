import sqlite3
import time

DB_FILE = "queue.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS jobs ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "status TEXT NOT NULL)"
    )
    conn.commit()
    conn.close()


def claim_job():
    conn = sqlite3.connect(DB_FILE, timeout=30)
    cur = conn.cursor()
    cur.execute("BEGIN IMMEDIATE")
    cur.execute(
        "SELECT id FROM jobs WHERE status = 'pending' ORDER BY id LIMIT 1"
    )
    row = cur.fetchone()
    if row is None:
        conn.commit()
        conn.close()
        return None
    job_id = row[0]
    cur.execute(
        "UPDATE jobs SET status = 'in_progress' WHERE id = ?", (job_id,)
    )
    conn.commit()
    conn.close()
    return job_id


def finish_job(job_id):
    conn = sqlite3.connect(DB_FILE, timeout=30)
    cur = conn.cursor()
    cur.execute("UPDATE jobs SET status = 'done' WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()


init_db()

while True:
    job_id = claim_job()
    if job_id is None:
        time.sleep(5)
        continue

    print(f"Start zadania {job_id}")
    time.sleep(30)
    finish_job(job_id)
    print(f"Koniec zadania {job_id}")
