from collections import defaultdict
from datetime import datetime
import statistics

def bucket_by_time(parsed_logs, window="hour"):
    buckets = defaultdict(int)

    for log in parsed_logs:
        ts = datetime.fromisoformat(log["timestamp"])

        if window == 'minute':
            key = ts.replace(second=0, microsecond=0)
        else: #hour
            key = ts.replace(minute=0, second=0, microsecond=0)
        
        buckets[key] += 1

    return buckets

def detect_anomalies(time_buckets, threshold=2):
    counts = list(time_buckets.values())

    if len(counts) < 3:
        return []
    
    stdev = statistics.stdev(counts)
    mean = statistics.mean(counts)

    if stdev == 0:
        return []
    
    anomalies = []

    for time, count in time_buckets.items():
        z = (count - mean) / stdev
        if z > threshold:
            anomalies.append({
                "time": time.isoformat(),
                "count": count,
                "z_score": round(z, 2),
            })
    
    return anomalies