import re

class LogParser:
    def __init__(self, pattern: str):
        self.regex = re.compile(pattern)
    
    def parse_line(self, line: str):
        match = self.regex.search(line)

        if match:
            return match.groupdict()
        return None