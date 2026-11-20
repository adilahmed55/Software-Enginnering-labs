# Lab 7: Fuzz Testing Report — Input Validation Bugs

- **Student Name:** N. Adil Ahmed
- **SRN:** PES1UG24CS285
- **Assigned Repository:** `SETAPESU26/L6_L7_39_password_policy/lab7`
- **Application Script:** `password_policy.py`
- **Fuzzing Library:** `Hypothesis` with `pytest`

---

## 1. Executive Summary

Fuzz testing (or fuzzing) is a dynamic software testing methodology that automatically generates unexpected, semi-random, and malformed inputs to expose edge-case bugs, crashes (unhandled exceptions), and security vulnerabilities.

In this lab, property-based fuzz testing was applied to the `password_policy` module using Python's **Hypothesis** library (`@given(st.text() | st.none())`). Hypothesis rapidly exposed three critical failure modes across all functions in the original script. By analyzing these failures, defensive programming fixes were implemented, resulting in a resilient and crash-free codebase.

---

## 2. Uncovered Bugs and Root Causes

| Function | Malformed Input Detected | Original Exception | Root Cause | Defensive Fix Applied |
|:---|:---|:---|:---|:---|
| `first_character_type(pw)` | `""` (empty string) | `IndexError: string index out of range` | Directly indexing `pw[0]` without validating length. | Added length check `if not pw: return "empty"`. |
| `first_character_type(pw)` | `None` | `TypeError: 'NoneType' object is not subscriptable` | Assuming `pw` is always a subscriptable string. | Added type check `if not isinstance(pw, str): return "empty"`. |
| `split_credentials(text)` | `"anytextwithoutcolon"` | `ValueError: not enough values to unpack (expected 2, got 1)` | Unconditional tuple unpacking `user, password = text.split(':')`. | Added check `if ':' not in text: return text.strip(), ""`. |
| `split_credentials(text)` | `"user:pass:extra"` | `ValueError: too many values to unpack (expected 2)` | Unpacking more than 2 elements when multiple colons exist. | Limited split to 1 occurrence: `text.split(':', 1)`. |
| `split_credentials(text)` | `None` | `AttributeError: 'NoneType' object has no attribute 'split'` | Calling string method `.split()` directly on `None`. | Added guard `if not isinstance(text, str) or not text: return "", ""`. |
| `digit_ratio(pw)` | `""` (empty string) | `ZeroDivisionError: division by zero` | Dividing by `len(pw)` when length is zero. | Guarded with `if len(pw) == 0: return 0.0`. |
| `digit_ratio(pw)` | `None` | `TypeError: 'NoneType' object is not iterable` | Iterating over `pw` when value is `None`. | Guarded with `if not isinstance(pw, str): return 0.0`. |

---

## 3. Terminal Execution Logs

### Before Fixes (Fuzzing Failures)
```text
============================= test session starts =============================
platform win32 -- Python 3.13.7, pytest-9.2.0, pluggy-1.7.0
rootdir: C:\Users\Asus\.gemini\antigravity\scratch\Software-Enginnering-labs\Lab-7
plugins: anyio-4.10.0, hydra-core-1.3.2, hypothesis-6.170.16
collected 3 items

FAILED test_password_policy.py::test_first_character_type_no_crash
    AssertionError: first_character_type crashed with: IndexError: string index out of range
    Failing input: s=''

FAILED test_password_policy.py::test_split_credentials_no_crash
    AssertionError: split_credentials crashed with: ValueError: not enough values to unpack (expected 2, got 1)
    Failing input: s=''

FAILED test_password_policy.py::test_digit_ratio_no_crash
    AssertionError: digit_ratio crashed with: ZeroDivisionError: division by zero
    Failing input: s=''

============================== 3 failed in 3.41s ==============================
```

### After Fixes (Hardened Verification)
```text
============================= test session starts =============================
platform win32 -- Python 3.13.7, pytest-9.2.0, pluggy-1.7.0
rootdir: C:\Users\Asus\.gemini\antigravity\scratch\Software-Enginnering-labs\Lab-7
plugins: anyio-4.10.0, hydra-core-1.3.2, hypothesis-6.170.16
collected 3 items

test_password_policy.py ...                                              [100%]

============================== 3 passed in 1.38s ==============================
```

---

## 4. Key Learnings & Defensive Programming Best Practices
1. **Never Assume Input Types or Shapes**: External data from APIs, forms, or network payloads often arrives as `None`, empty strings, or strings lacking expected delimiters.
2. **Defensive Guards Preempt Crashes**: Simple guard clauses (`if not isinstance(...)` and `len == 0`) eliminate runtime exceptions before high-cost operations occur.
3. **Hypothesis vs. Traditional Unit Tests**: While unit tests only check what developers anticipate, Hypothesis generates adversarial inputs (boundary values, Unicode, zero-length arrays, null bytes) that reveal unanticipated edge cases automatically.
