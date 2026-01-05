import gzip

def open_log_file(path):
    if path.endswith(".gz"):
        return gzip.open(path, "rt")
    return open(path)