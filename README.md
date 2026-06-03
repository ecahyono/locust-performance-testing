# Sample Locust Performance Testing

Performance testing project using Locust against DummyJSON API.

## Project Overview

This project demonstrates API performance testing using Locust by simulating concurrent users performing authentication and product-related operations.

The test covers:

* User Login
* Get Product List
* Search Product
* Get User Profile

## Technology Stack

* Python 3.x
* Locust
* DummyJSON API

## Target Application

Base URL:

```text
https://dummyjson.com
```

Documentation:

https://dummyjson.com/docs/auth

---

## Test Scenario

### Authentication

```text
Login User
↓
Store Access Token
```

### Business Flow

```text
Get Products
↓
Search Product
↓
Get Current User
```

---

## Test Configuration

| Parameter        | Value        |
| ---------------- | ------------ |
| Concurrent Users | 100          |
| Spawn Rate       | 10 users/sec |
| Duration         | 2 Minutes    |
| Stop Timeout     | 10 Seconds   |
| Report Format    | HTML + CSV   |

---

## Project Structure

```text
locust-performance-testing/
│
├── reports/
│   ├── report.html
│   ├── result_stats.csv
│   ├── result_failures.csv
│   ├── result_exceptions.csv
│   └── result_stats_history.csv
│
├── locustfile.py
├── requirements.txt
├── run_test.bat
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone <repository-url>
cd locust-performance-testing
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install locust
```

---

## Execute Performance Test

Run:

```bash
run_test.bat
```

Or manually:

```bash
locust -f locustfile.py ^
--host=https://dummyjson.com ^
--users 100 ^
--spawn-rate 10 ^
--run-time 2m ^
--headless ^
--html reports/report.html ^
--csv reports/result ^
--stop-timeout 10
```

---

## Generated Reports

After execution completes, the following reports will be generated:

### HTML Report

```text
reports/report.html
```

Contains:

* Request Statistics
* Response Time Distribution
* Throughput Analysis
* Error Analysis

### CSV Reports

```text
reports/result_stats.csv
reports/result_failures.csv
reports/result_exceptions.csv
reports/result_stats_history.csv
```

Contains raw performance metrics for further analysis.

---

## Metrics Monitored

### Response Time

Measures:

* Average Response Time
* Median Response Time
* Min Response Time
* Max Response Time
* 95th Percentile

### Throughput

Measures:

* Requests Per Second (RPS)
* Total Requests

### Reliability

Measures:

* Error Rate
* Failure Count
* Exception Count

---

## Sample Test Result

```text
Concurrent Users : 100
Duration         : 2 Minutes

Total Requests   : 8,500+
Avg Response     : 150 ms
P95 Response     : 350 ms
Error Rate       : 0.00%
Throughput       : 70 req/sec

Status           : PASSED
```

*Results may vary depending on network conditions and target server performance.*

---
