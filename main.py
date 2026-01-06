import argparse
import os
from src.config_loader import load_config
from src.reporter import write_output
from src.analyser import analyse_access_log, analyse_errors_log
from src.anomaly import bucket_by_time, detect_anomalies
from src.nlp_cluster import cluster_log_messages

# ACCESS_LOG = 'logs/access.log'
# ERRORS_LOG = 'logs/errors.log'
# OUTPUT_FILE = 'output/summary.txt'

def parse_args():
    parser = argparse.ArgumentParser(description="Log File Analyser")
    parser.add_argument("--access-log", required=True, help="Path to the log file")
    parser.add_argument("--error-log", required=True, help="Path to the error file")
    parser.add_argument("--output", required=True, help="Full output file path")
    parser.add_argument("--config", default=None, help="Path to config file (YAML)")
    return parser.parse_args()

def main():
    args = parse_args()

    config = load_config(args.config)

    if not os.path.exists(args.access_log):
        raise FileNotFoundError("Access log file not found")
    elif not os.path.exists(args.error_log):
        raise FileNotFoundError("Error log file not found")
    # elif os.path.exists(args.output):
    #     raise FileExistsError("Output file already exists!")
    
    output_dir = os.path.dirname(args.output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    ip_counts, status_counts = analyse_access_log(args.access_log, config=config.get("access_log", {}))
    error_counts, parsed_logs = analyse_errors_log(args.error_log, config=config.get("error_log", {}))

    time_buckets = bucket_by_time(parsed_logs, window="hour")
    anomalies = detect_anomalies(time_buckets)

    error_messages = [log["message"] for log in parsed_logs]

    clusters = cluster_log_messages(error_messages)

    result = {
        "access_log": {
            "ip_counts": dict(ip_counts),
            "status_counts": dict(status_counts)
        },
        "error_log": dict(error_counts),
        "anomalies": anomalies,
        "log_clusters": clusters
    }

    write_output(result, args.output)

    print("Log analysis complete ✅")
    print(f"Report generated at: {args.output}")


if __name__ == "__main__":
    main()