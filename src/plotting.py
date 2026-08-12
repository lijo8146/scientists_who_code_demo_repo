"""Create the exemplar's single, documented result figure."""
from pathlib import Path

import matplotlib

# A non-interactive backend makes this script work on workshop servers as well as laptops.
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "processed" / "daily_streamflow.csv"
FIGURE_FILE = ROOT / "outputs" / "figures" / "boulder_creek_streamflow.png"
SUMMARY_FILE = ROOT / "outputs" / "streamflow_summary.csv"


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


if __name__ == "__main__":
    summary = create_outputs()
    print(summary.round(2))
