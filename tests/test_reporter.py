from src.reporter import write_output
from src.utility import open_log_file
import json
import csv
import tempfile
import os

def test_json_output():
    data = {
        "access_log": {
            "ip_counts": {"1.1.1.1": 2},
            "status_counts": {"200": 1}
        },
        "error_log": {"ERROR": 3}
    }

    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        path = f.name

    write_output(data, path)

    with open_log_file(path) as f:
        result = json.load(f)

    assert result["error_log"]["ERROR"] == 3


def test_csv_output():
    data = {
        "access_ip": {"1.1.1.1": 2},
        "error": {"ERROR": 1}
    }

    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
        path = f.name

    write_output(data, path)

    with open_log_file(path) as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows[0] == ["section", "key", "count"]