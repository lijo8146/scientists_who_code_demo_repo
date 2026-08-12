from src.processing import extract_daily_values


def test_extract_daily_values_converts_dates_and_missing_values():
    payload = {"value": {"timeSeries": [{"values": [{"value": [
        {"dateTime": "2024-05-01T00:00:00.000-06:00", "value": "12.4", "qualifiers": ["A"]},
        {"dateTime": "2024-05-02T00:00:00.000-06:00", "value": "", "qualifiers": ["P"]},
    ]}]}]}}
    result = extract_daily_values(payload)
    assert list(result.columns) == ["date", "discharge_cfs", "qualifier"]
    assert result.loc[0, "discharge_cfs"] == 12.4
    assert result.loc[1, "discharge_cfs"] != result.loc[1, "discharge_cfs"]  # NaN
