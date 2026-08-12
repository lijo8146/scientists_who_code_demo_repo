"""Clean the USGS response into an analysis-ready table."""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data" / "raw" / "usgs_daily_streamflow.json"
PROCESSED_FILE = ROOT / "data" / "processed" / "daily_streamflow.csv"


def extract_daily_values(payload: dict) -> pd.DataFrame:
    """Return date, discharge, and qualification code from a USGS response."""
    series = payload["value"]["timeSeries"][0]
    values = series["values"][0]["value"]
    frame = pd.DataFrame(values)
    frame["date"] = pd.to_datetime(frame["dateTime"], utc=True).dt.tz_localize(None).dt.normalize()
    frame["discharge_cfs"] = pd.to_numeric(frame["value"], errors="coerce")
    frame["qualifier"] = frame["qualifiers"].str.join(",")
    return frame[["date", "discharge_cfs", "qualifier"]].sort_values("date").reset_index(drop=True)


def make_processed_data(raw_file=RAW_FILE, output_file=PROCESSED_FILE) -> pd.DataFrame:
    """Read raw JSON, remove missing discharge records, and write a CSV."""
    with open(raw_file, encoding="utf-8") as handle:
        payload = json.load(handle)
    frame = extract_daily_values(payload).dropna(subset=["discharge_cfs"])
    output_file.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_file, index=False)
    return frame


if __name__ == "__main__":
    frame = make_processed_data()
    print(f"Wrote {len(frame)} daily records to {PROCESSED_FILE.relative_to(ROOT)}.")
