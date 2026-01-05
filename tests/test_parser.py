from src.parser import LogParser

def test_access_log_parsing():
    pattern = (
        r"(?P<ip>\d+\.\d+\.\d+\.\d+)\s+"
        r"(?P<method>GET|POST)\s+"
        r"(?P<status>\d{3})"
    )

    parser = LogParser(pattern)

    line = "192.168.1.1 GET 200"
    result = parser.parse_line(line)

    assert result["ip"] == "192.168.1.1"
    assert result["method"] == "GET"
    assert result["status"] == "200"


def test_invalid_log_line_returns_none():
    parser = LogParser(r"(?P<ip>\d+\.\d+\.\d+\.\d+)")
    assert parser.parse_line("INVALID LINE") is None