# Lab 5: Static Code Analysis — Vehicle Service Management System

- **Student Name:** N. Adil Ahmed
- **SRN:** PES1UG24CS285
- **Assigned Repository:** `SETAPESU26/L5_39_vehicle_service`

---

## Overview

This lab focuses on using industry-standard static analysis tools (**Pylint**, **Bandit**, and **Flake8**) to detect, document, and rectify security vulnerabilities, code quality bugs, and style issues in a vehicle service desk system.

### Key Metrics Summary

| Analysis Tool | Focus Area | Before Fixes | After Fixes | Status |
|:---|:---|:---|:---|:---|
| **Bandit** | Security Vulnerabilities | 4 issues (2 High, 2 Low) | **0 issues** | Passed |
| **Pylint** | Code Quality & Logic | Score: **4.66 / 10** | **Score: 10.00 / 10** | Target >9.5 Achieved |
| **Flake8** | PEP 8 Style & Conventions | 4 violations | **0 violations** | Passed |

---

## Directory Contents

- `vehicle_service.py`: Cleaned and refactored production script (score: 10.00/10, zero security findings).
- `vehicle_service_original.py`: Original unmodified script from assigned repository.
- `issues.md`: Detailed documentation table of all identified issues, line numbers, descriptions, and fixes.
- `reflection.md`: In-depth answers to the four reflection questions on static analysis and security.
- `pylint_report_before.txt` & `pylint_report.txt`: Pylint reports before and after refactoring.
- `bandit_report_before.txt` & `bandit_report.txt`: Bandit security audit reports before and after refactoring.
- `flake8_report_before.txt` & `flake8_report.txt`: Flake8 PEP 8 compliance reports before and after refactoring.

---

## How to Run and Verify

```bash
# 1. Run the script to verify correct execution
python vehicle_service.py

# 2. Run Pylint analysis (verifies 10.00/10 rating)
python -m pylint vehicle_service.py

# 3. Run Bandit security scan (verifies 0 issues)
python -m bandit -r vehicle_service.py

# 4. Run Flake8 style checker (verifies 0 violations)
python -m flake8 vehicle_service.py
```
