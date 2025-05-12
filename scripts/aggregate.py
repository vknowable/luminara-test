from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd

log = Path("data/minute_log.csv")
agg = Path("data/hourly_agg.csv")
last_run_file = Path("data/.last_agg_time")
now = datetime.utcnow()

# Only aggregate if an hour has passed
if last_run_file.exists():
    last_run = datetime.fromisoformat(last_run_file.read_text().strip())
    if now - last_run < timedelta(hours=1):
        print("Aggregation skipped: less than 1 hour since last run")
        exit(0)
else:
    last_run = now - timedelta(hours=1, minutes=1)  # force first run

df = pd.read_csv(log)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df[df['timestamp'] > now - timedelta(hours=1)]

summary = {
    "timestamp": now.isoformat(),
    "total_checks": len(df),
    "status_200": (df["status"] == 200).sum()
}

agg_df = pd.DataFrame([summary])
write_header = not agg.exists()
agg_df.to_csv(agg, mode="a", index=False, header=write_header)

# Save timestamp
last_run_file.write_text(now.isoformat())
