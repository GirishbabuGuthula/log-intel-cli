from src.analyser import analyse_access_log, analyse_errors_log
import tempfile

def test_access_log_analysis():
    log_data = """\
    192.168.1.1 GET /home 200
    192.168.1.1 GET /home 500
    """

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(log_data)
        path = f.name

    config = {
        "pattern": r"(?P<ip>\d+\.\d+\.\d+\.\d+).*(?P<status>\d{3})"
    }

    ip_counts, status_counts = analyse_access_log(path, config)

    assert ip_counts["192.168.1.1"] == 2
    assert status_counts["200"] == 1
    assert status_counts["500"] == 1


def test_error_log_analysis():
    log_data = """\
    2025 ERROR Database failed
    2025 WARNING Disk low
    """

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(log_data)
        path = f.name

    config = {
        "pattern": r"\S+\s+(?P<level>ERROR|WARNING)"
    }

    error_counts = analyse_errors_log(path, config)

    assert error_counts["ERROR"] == 1
    assert error_counts["WARNING"] == 1