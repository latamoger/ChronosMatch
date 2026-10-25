# ChronosMatch: Zero-Copy High-Frequency Trading Engine

## Project Overview

ChronosMatch is a Python-based trading engine project designed to match buy and sell orders efficiently using price-time priority.

The project focuses on order matching, partial order execution, API development, functional testing, and performance evaluation.

## Technologies Used

- Python
- Flask
- SQLite (planned backend integration)
- HTML, CSS, JavaScript (planned frontend)
- Python unittest
- Git and GitHub

## Key Features

- Buy and sell order matching
- Price-time priority
- Partial order execution
- Order book management
- Trade history
- Practice Flask API
- Automated functional testing
- Performance benchmarking

## Project Structure

```text
ChronosMatch/
├── matching_engine.py
├── practice_api.py
├── app.py
├── database.py
├── main.py
├── requirements.txt
├── tests/
│   ├── test_matching.py
│   ├── test_api.py
│   └── test_performance.py
└── reports/
    ├── bug_report.txt
    ├── test_report.txt
    ├── testing_documentation.txt
    └── performance_results.csv
```

## Testing Results

| Test Category | Passed | Failed |
|---|---:|---:|
| Matching Engine | 7 | 0 |
| Practice API | 7 | 0 |
| **Total** | **14** | **0** |

## Performance Results

| Number of Orders | Throughput (orders/sec) |
|---|---:|
| 100 | 454,752.07 |
| 1,000 | 757,575.73 |
| 5,000 | 765,087.52 |
| 10,000 | 466,890.46 |

These are initial benchmark results from a practice workload, not verified production performance.

## Team Members and Responsibilities

**Priyanshu – Core Engine Developer**

- Order matching logic
- Price-time priority
- Partial fills

**Adil – Backend Developer**

- Flask API development
- Database integration

**Gayathri M – Frontend Developer**

- Trading dashboard
- Order and trade display

**Lata Moger – Testing & Performance Developer**

- Functional and API testing
- Performance benchmarking
- Bug reporting
- Testing documentation

## How to Run

Install Flask:

```bash
py -m pip install flask
```

Run the practice API:

```bash
py practice_api.py
```

Run all functional and API tests:

```bash
py -m unittest discover -s tests -v
```

Run performance testing:

```bash
py -m tests.test_performance
```

## Current Project Status

The matching-engine practice implementation, practice API, initial tests, and performance reports are available.

The final integrated frontend, backend, and database still require completion and verification.
