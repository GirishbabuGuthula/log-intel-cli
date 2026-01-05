# 🚀 Log Intel CLI

**AI-powered log analysis CLI** that transforms raw access and error logs into actionable insights using **structured parsing, statistical anomaly detection, and NLP-based clustering**.

Built with scalability, configurability, and real-world observability use cases in mind.

---

## ✨ Features

- 🔍 **Structured Log Parsing**  
  Regex-based parsing with named capture groups (configurable via YAML)

- ⚙️ **Config-Driven Architecture**  
  Change log formats and behavior without touching code

- 🧠 **Anomaly Detection (AI Touch)**  
  Detect abnormal error spikes using time-window aggregation and Z-score analysis

- 🧩 **NLP Log Clustering**  
  Group semantically similar error messages using TF-IDF + cosine similarity

- 📊 **Multiple Output Formats**  
  Generate reports in **TXT**, **JSON**, or **CSV**

- 🚄 **Large File Optimized**  
  Streaming I/O, compiled regex reuse, early filtering, gzip support

- 🧪 **Unit Tested**  
  Parsing, analysis, and reporting covered using `pytest`

- 💻 **Command-Line Interface**  
  Simple, intuitive CLI built with `argparse`

---

## 🧠 Why This Project?

Modern systems generate **huge volumes of logs**, making manual inspection inefficient and error-prone.

This project demonstrates how to:
- Convert unstructured logs into structured data
- Detect anomalies before they become incidents
- Reduce noise using NLP-based clustering
- Build scalable, production-style backend tooling

---

## 📦 Project Structure

```
log-intel-cli/
├── src/
│   ├── analyser.py        # Core log analysis logic
│   ├── parser.py          # Structured regex parsing
│   ├── reporter.py        # TXT / JSON / CSV output
│   ├── anomaly.py         # Statistical anomaly detection
│   ├── nlp_cluster.py     # NLP-based log clustering
│   ├── config_loader.py  # YAML config loader
│   └── utils.py           # Shared utilities (gzip, streaming, etc.)
│
├── tests/
│   ├── test_parser.py
│   ├── test_analyser.py
│   └── test_reporter.py
│
├── config.yaml
├── main.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

```bash
git clone https://github.com/your-username/log-intel-cli.git
cd log-intel-cli
pip install -r requirements.txt
```

---

## ▶️ Usage

### Basic Run
```bash
python main.py \
  --access-log logs/access.log \
  --error-log logs/errors.log \
  --output reports/summary.json \
  --config config.yaml
```

### Output Formats
The output format is **automatically inferred** from the file extension:

```bash
--output report.txt    # Human-readable text
--output report.json   # Machine-readable JSON
--output report.csv    # Spreadsheet-friendly CSV
```

### Output Directory Handling
Directories are created automatically:

```bash
--output results/2025/march/summary.json
```

---

## ⚙️ Configuration (`config.yaml`)

```yaml
access_log:
  pattern: >
    (?P<ip>\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+\[(?P<timestamp>[^\]]+)\]\s+\"(?P<method>GET|POST|PUT|DELETE)\s+(?P<path>[^\"]+)\"\s+(?P<status>\d{3})

error_log:
  pattern: >
    (?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\s+(?P<level>ERROR|WARNING|INFO)\s+(?P<message>.+)
```

This allows the tool to adapt to **any log format** without code changes.

---

## 🤖 Anomaly Detection

- Errors are grouped into time windows (hourly)
- Z-score is computed for each window
- Spikes above the threshold are flagged

### Example Output
```json
"anomalies": [
  {
    "time": "2025-03-25T14:00:00",
    "count": 40,
    "z_score": 3.8
  }
]
```

---

## 🧩 NLP Log Clustering

Error messages are clustered by **semantic similarity**, not exact text.

### Example
```json
"log_clusters": {
  "0": [
    "Database connection failed",
    "DB connection failure",
    "Failed to connect to database"
  ],
  "1": [
    "Timeout while calling auth service",
    "Auth service timeout"
  ]
}
```

This significantly improves **root-cause analysis**.

---

## 🚀 Performance Considerations

- Streams log files line-by-line (constant memory)
- Compiles regex patterns once per file
- Skips non-matching lines early
- Supports `.gz` compressed log files

Designed to handle **very large log files** efficiently.

---

## 🧪 Running Tests

```bash
pytest
```

Tests cover:
- Regex parsing
- Log aggregation logic
- Multi-format report generation

---

## 📌 Tech Stack

- Python
- argparse
- PyYAML
- scikit-learn
- pytest

---

## 📄 Resume Highlights

> Built an AI-powered log analysis CLI featuring structured parsing, statistical anomaly detection, and NLP-based log clustering, optimized for large-scale log processing.

---

## 🔮 Future Enhancements

- Package as `pip install log-intel-cli`
- Docker support
- Streamlit dashboard
- Real-time log streaming
- LLM-based log summarization

---

## 🧑‍💻 Author

**Girish Babu**  
AI Engineering Enthusiast | Backend & Systems Builder
