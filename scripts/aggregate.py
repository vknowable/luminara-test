import pandas as pd
from pathlib import Path
from datetime import datetime

if datetime.utcnow().minute == 0:
    log = Path("data/minute_log.csv")
    agg = Path("data/hourly_agg.csv")
    
    df = pd.read_csv(log)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df[df['timestamp'] > datetime.utcnow() - pd.Timedelta("1H")]
    
    summary = {
        "timestamp": datetime.utcnow().isoformat(),
        "total_checks": len(df),
        "status_200": (df["status"] == 200).sum()
    }
    
    agg_df = pd.DataFrame([summary])
    write_header = not agg.exists()
    
    agg_df.to_csv(agg, mode="a", index=False, header=write_header)

else:
    print("Not top of the hour, skipping aggregation.")
    exit(0)
