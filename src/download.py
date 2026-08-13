"""Download a small, documented USGS daily-streamflow dataset."""
from datetime import date, datetime, timezone
import json
from pathlib import Path

import requests

SITE = "06730200"
PARAMETER = "00060"  # discharge, cubic feet per second
START_DATE = "2024-05-01"
END_DATE = "2024-09-30"
URL = "https://waterservices.usgs.gov/nwis/dv/"
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"


def download_streamflow():
    """Fetch daily mean streamflow and save both data and provenance."""
    params = {"format": "json", "sites": SITE, "parameterCd": PARAMETER,
              "startDT": START_DATE, "endDT": END_DATE, "siteStatus": "all"}
    response = requests.get(URL, params=params, timeout=30)
    response.raise_for_status()
    payload = response.json()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    (RAW_DIR / "usgs_daily_streamflow.json").write_text(json.dumps(payload, indent=2))
    source_info = payload["value"]["timeSeries"][0]["sourceInfo"]
    geog = source_info["geoLocation"]["geogLocation"]
    location = {
        "site_no": source_info["siteCode"][0]["value"],
        "site_name": source_info["siteName"],
        "latitude_wgs84": float(geog["latitude"]),
        "longitude_wgs84": float(geog["longitude"]),
        "coordinate_reference_system": "EPSG:4326 (WGS 84)",
    }
    (RAW_DIR / "site_location.json").write_text(json.dumps(location, indent=2))
    provenance = {
        "source": "USGS National Water Information System daily values service",
        "source_url": response.url,
        "accessed_utc": datetime.now(timezone.utc).isoformat(),
        "parameters": params,
        "license_note": "Public USGS data; cite the source and verify fitness for use.",
    }
    (RAW_DIR / "provenance.json").write_text(json.dumps(provenance, indent=2))
    return payload


if __name__ == "__main__":
    download_streamflow()
    print(f"Downloaded USGS site {SITE}: {START_DATE} to {END_DATE}.")
