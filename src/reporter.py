import os
import json
import csv

def write_output(data, output_path: str):
    ext = os.path.splitext(output_path)[1].lower()

    if ext == ".json":
        write_json(data, output_path)
    elif ext == ".csv":
        write_csv(data, output_path)
    else:
        write_text(data, output_path)

def write_json(data, path: str):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def write_csv(data, path: str):
    del data["anomalies"]
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["section", "key", "count"])

        for section, values in data.items():
            for key, count in values.items():
                writer.writerow([section, key, count])

def write_text(data, path: str):
    with open(path, "w") as f:
        f.write("=== Access Log Analysis ===\n")
        for k, v in data["access_log"]["ip_counts"].items():
            f.write(f"{k}: {v}\n")

        f.write("\n=== Status Codes ===\n")
        for k, v in data["access_log"]["status_counts"].items():
            f.write(f"{k}: {v}\n")

        f.write("\n=== Error Log Analysis ===\n")
        for k, v in data["error_log"].items():
            f.write(f"{k}: {v}\n")