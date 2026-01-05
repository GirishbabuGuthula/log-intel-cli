import re
from collections import Counter
from src.parser import LogParser
from src.utility import open_log_file

def analyse_access_log(file_path: str, config=None):
    parser = LogParser(config["pattern"])

    ip_counter = Counter()
    status_counter = Counter()

    with open_log_file(file_path) as lines:
        for line in lines:
            parsed = parser.parse_line(line)
            if not parsed:
                continue
            ip_counter[parsed["ip"]] += 1
            status_counter[parsed["status"]] += 1
    return ip_counter, status_counter



def analyse_errors_log(file_path: str, config=None):
    parser = LogParser(config["pattern"])
    error_counter = Counter()
    parsed_logs = []

    with open_log_file(file_path) as lines:
        for line in lines:
            parsed = parser.parse_line(line)
            if not parsed:
                continue
            error_counter[parsed["level"]] += 1
            if parsed['level'] == 'ERROR':
                parsed_logs.append(parsed)

    return error_counter, parsed_logs