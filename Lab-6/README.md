# Lab 6: Code and Branch Coverage Analysis — Password Policy Checker

- **Student Name:** N. Adil Ahmed
- **SRN:** PES1UG24CS285
- **Assigned Repository:** `SETAPESU26/L6_L7_39_password_policy/lab6`
- **Application Script:** `password_policy.py`

---

## Objective & Outcomes

The goal of this lab is to understand, measure, and maximize both **Line/Statement Coverage** and **Branch Coverage** for the `password_policy` module using `coverage.py` and `pytest`.

### Results Summary

| Metric | Target | Baseline (Starter Tests) | Achieved Result | Status |
|:---|:---|:---|:---|:---|
| **Statement / Code Coverage** | $\ge 90\%$ | $55\%$ (21 missing statements) | **100% (47/47 statements)** | Exceeded |
| **Branch Coverage** | $\ge 90\%$ | $< 50\%$ | **100% (36/36 branches, 0 partial)** | Exceeded |

---

## Directory Structure & Deliverables

- `password_policy.py`: The application under test.
- `CodeCoverageTest_password_policy_application.py`: Comprehensive test suite achieving **100% code coverage**.
- `BranchCoverageTest_password_policy_application.py`: Targeted branch test suite evaluating every conditional branch (`if`/`elif`/`else`) to both True and False, achieving **100% branch coverage**.
- `initial_test_password_policy.py`: Initial starter test file demonstrating initial 55% coverage.
- `code_coverage_report.txt`: Terminal output report for code coverage run.
- `branch_coverage_report.txt`: Terminal output report for branch coverage run.

---

## Commands to Run and Verify

### 1. Statement / Code Coverage
```bash
# Run tests and gather statement coverage
coverage run -m pytest CodeCoverageTest_password_policy_application.py

# Display statement coverage report
coverage report -m
```

**Output:**
```
Name                                              Stmts   Miss  Cover   Missing
-------------------------------------------------------------------------------
CodeCoverageTest_password_policy_application.py      53      0   100%
password_policy.py                                   47      0   100%
-------------------------------------------------------------------------------
TOTAL                                               100      0   100%
```

### 2. Branch Coverage
```bash
# Run tests and gather branch coverage
coverage run --branch -m pytest BranchCoverageTest_password_policy_application.py

# Display branch coverage report
coverage report -m
```

**Output:**
```
Name                                                Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------------------------------
BranchCoverageTest_password_policy_application.py      37      0      0      0   100%
password_policy.py                                     47      0     36      0   100%
-----------------------------------------------------------------------------------------------
TOTAL                                                  84      0     36      0   100%
```
