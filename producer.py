import csv
import os
import sys

QUEUE_FILE = "queue.csv"

count = int(sys.argv[1]) if len(sys.argv) > 1 else 1

rows = []
if os.path.exists(QUEUE_FILE):
    with open(QUEUE_FILE, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

next_id = (max([int(r["id"]) for r in rows], default=0) + 1) if rows else 1
for _ in range(count):
    rows.append({"id": str(next_id), "status": "pending"})
    next_id += 1

with open(QUEUE_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "status"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Dodano {count} zadan.")
