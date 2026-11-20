# Lab 7: Fuzzing for Input Validation Bugs

- **Student Name:** N. Adil Ahmed
- **SRN:** PES1UG24CS285
- **Assigned Repository:** `SETAPESU26/L6_L7_39_password_policy/lab7`
- **Application Script:** `password_policy.py`

---

## Deliverables Checklist

- [x] Fixed application Python script (`password_policy.py`)
- [x] Updated property-based test script (`test_password_policy.py`)
- [x] Original buggy code reference (`password_policy_original.py`)
- [x] Fuzz test failure output log (`fuzz_test_failures.txt`)
- [x] Fuzz test passing output log (`fuzz_test_passed.txt`)
- [x] Comprehensive report and analysis (`fuzzing_report.md`)

---

## Quick Start & Verification

```bash
# 1. Run property-based fuzz tests on the hardened script
pytest test_password_policy.py

# 2. Or run via python -m pytest
python -m pytest test_password_policy.py
```
