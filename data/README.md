# Data

`raw/` contains downloaded USGS responses and a provenance record; it is ignored by Git because it can be regenerated. `processed/` holds the cleaned daily streamflow table made by `src/processing.py`.

The exemplar downloads daily mean discharge (USGS parameter `00060`) for site `06730200` (Boulder Creek at North 75th St. near Boulder, Colorado) between 2024-05-01 and 2024-09-30. The time window is intentionally fixed so workshop participants see the same query and can discuss seasonal patterns without implying a long-term trend.
