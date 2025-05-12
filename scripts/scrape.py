import csv
import time
from datetime import datetime
from pathlib import Path

data_file = Path("data/minute_log.csv")
data_file.parent.mkdir(exist_ok=True)

now = datetime.utcnow().isoformat()
row = [now, "https://example.com", 200]

write_header = not data_file.exists()

with data_file.open("a", newline="") as f:
    writer = csv.writer(f)
    if write_header:
        writer.writerow(["timestamp", "url", "status"])
    writer.writerow(row)
