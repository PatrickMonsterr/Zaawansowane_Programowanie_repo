import csv
import os
import time

QUEUE_FILE = "queue.csv"


def read_rows():
    if not os.path.exists(QUEUE_FILE):
        return []
    with open(QUEUE_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_rows(rows):
    with open(QUEUE_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "status"])
        writer.writeheader()
        writer.writerows(rows)


while True:
    rows = read_rows()
    job = None
    for row in rows:
        if row["status"] == "pending":
            row["status"] = "in_progress"
            job = row["id"]
            break

    if job is None:
        time.sleep(5)
        continue

    write_rows(rows)
    print(f"Start zadania {job}")
    time.sleep(30)

    rows = read_rows()
    for row in rows:
        if row["id"] == job:
            row["status"] = "done"
            break
    write_rows(rows)
    print(f"Koniec zadania {job}")
