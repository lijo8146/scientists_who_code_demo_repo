"""Create the exemplar's single, documented result figure."""
from pathlib import Path

import matplotlib

# A non-interactive backend makes this script work on workshop servers as well as laptops.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from pyproj import Transformer

ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "processed" / "daily_streamflow.csv"
FIGURE_FILE = ROOT / "outputs" / "figures" / "boulder_creek_streamflow.png"
SUMMARY_FILE = ROOT / "outputs" / "streamflow_summary.csv"
LOCATION_FILE = ROOT / "data" / "raw" / "site_location.json"
MAP_FILE = ROOT / "outputs" / "figures" / "boulder_creek_streamgage_location.png"


def create_outputs(input_file=INPUT_FILE, figure_file=FIGURE_FILE, summary_file=SUMMARY_FILE):
    """Plot daily discharge and write a compact, auditable summary table."""
    frame = pd.read_csv(input_file, parse_dates=["date"])
    summary = frame["discharge_cfs"].agg(["count", "min", "median", "mean", "max"]).to_frame("discharge_cfs")
    summary.index.name = "statistic"
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(summary_file)
    figure_file.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.plot(frame["date"], frame["discharge_cfs"], color="#1261A0", linewidth=1.8)
    ax.set(title="Boulder Creek daily mean streamflow", xlabel="Date", ylabel="Discharge (cubic feet per second)")
    ax.text(0.01, -0.27, "USGS site 06730200; 2024-05-01 to 2024-09-30.\nValues are observations, not a prediction or causal estimate.", transform=ax.transAxes, fontsize=8)
    ax.spines[["top", "right"]].set_visible(False)
    fig.subplots_adjust(bottom=0.27, left=0.12, right=0.96, top=0.9)
    fig.savefig(figure_file, dpi=180)
    plt.close(fig)
    return summary


def create_location_map(location_file=LOCATION_FILE, map_file=MAP_FILE):
    """Create an offline projected locator map for the streamgage.

    The source coordinates are WGS84 longitude/latitude and are transformed to
    NAD83 / UTM zone 13N (EPSG:26913), appropriate for the Boulder-area view.
    """
    import json
    with open(location_file, encoding="utf-8") as handle:
        location = json.load(handle)
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:26913", always_xy=True)
    east_m, north_m = transformer.transform(location["longitude_wgs84"], location["latitude_wgs84"])
    map_file.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(6.8, 5.4))
    extent = 7_500
    ax.set_xlim(east_m - extent, east_m + extent)
    ax.set_ylim(north_m - extent, north_m + extent)
    ax.grid(color="#c7d6df", linewidth=0.8)
    ax.scatter(east_m, north_m, s=95, color="#d1495b", edgecolor="white", linewidth=1.5, zorder=3)
    ax.annotate(location["site_name"], (east_m, north_m), xytext=(10, 10), textcoords="offset points", fontsize=9)
    ax.set(title="USGS streamgage location: Boulder Creek", xlabel="Easting (m), EPSG:26913", ylabel="Northing (m), EPSG:26913")
    ax.text(0.02, 0.02, "Source coordinates: USGS, WGS84; projected for display to NAD83 / UTM zone 13N.\nGrid is a locator reference, not a basemap.", transform=ax.transAxes, fontsize=8, va="bottom")
    ax.spines[["top", "right"]].set_visible(False)
    fig.subplots_adjust(bottom=0.19, left=0.16, right=0.96, top=0.9)
    fig.savefig(map_file, dpi=180)
    plt.close(fig)
    return east_m, north_m


if __name__ == "__main__":
    summary = create_outputs()
    create_location_map()
    print(summary.round(2))
