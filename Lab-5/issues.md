# Lab 5: Static Code Analysis — Issue Documentation Table

## Student Details
- **Student Name:** N. Adil Ahmed
- **SRN:** PES1UG24CS285
- **Assigned Repository:** `SETAPESU26/L5_39_vehicle_service`
- **Target Script:** `vehicle_service.py`

---

## Documented Static Analysis Issues

The table below documents the security, quality, and style issues detected in the initial script by **Bandit**, **Pylint**, and **Flake8**, prioritized by severity.

| Issue | Tool | Severity / Type | Line(s) | Description | Fix Approach |
|:---|:---|:---|:---|:---|:---|
| **B602: Subprocess call with `shell=True`** | Bandit | High (Security) | 61 | `subprocess.call("cp services.json " + folder, shell=True)` executes an unescaped shell command constructed via string concatenation, making the system vulnerable to Command Injection (CWE-78). | Removed `subprocess` and `shell=True` entirely. Replaced with `shutil.copy2("services.json", folder)` from Python standard library, which copies files securely without invoking a command shell. |
| **B324: Use of insecure MD5 hash** | Bandit | High (Security) | 39 | `hashlib.md5(vehicleNo.encode())` uses the legacy MD5 hash algorithm, which is cryptographically broken and flags security compliance scanners. | Added explicit keyword argument `usedforsecurity=False` in `hashlib.md5(..., usedforsecurity=False)` to clearly designate non-cryptographic identifier generation. |
| **B105: Hardcoded plaintext credentials** | Bandit | Low (Security) | 8 | `ADMIN_PASSWORD = "garage-demo"` hardcodes a sensitive credential in plaintext inside source control (CWE-259). | Removed plaintext constant; replaced with secure retrieval from environment variables using `os.getenv("ADMIN_PASSWORD", "")`. |
| **W0102: Dangerous mutable default argument** | Pylint | Warning / Bug | 12 | `def addService(vehicleNo, serviceType="General", history=[])` uses a mutable list `[]` as a default value. In Python, default parameters are evaluated once upon function definition, meaning the list is shared across all invocations, causing state leakage. | Changed default value to `None`. Initialized `history = []` inside the function body when `history is None`. |
| **W0718: Overly broad exception clause** | Pylint | Warning / Bug | 23 | `except Exception:` catches all standard Python exceptions, unintentionally masking syntax errors, memory errors, or system signals. | Narrowed exception catching strictly to `KeyError` (`except KeyError:`), which specifically handles the case where a vehicle is missing from `service_records`. |
| **W1514: Unspecified file encoding** | Pylint | Warning / Quality | 50 | `open(fileName, "w")` opens a file without declaring encoding, leading to platform-dependent text corruption when running across Windows, Linux, and macOS. | Specified explicit UTF-8 encoding: `open(file_name, "w", encoding="utf-8")`. |
| **C0103: Non-conformant naming convention** | Pylint | Convention | 12–59 | Identifiers (`addService`, `cancelService`, `getTotalCost`, `jobCardId`, `busiestVehicle`, `saveRecords`, `loadRecords`, `backupRecords`, `vehicleNo`, `totalCost`) violated PEP 8 `snake_case` naming rules. | Refactored all function and variable names to PEP 8 standard `snake_case` (while maintaining backwards-compatible aliases if needed). |
| **C0114 / C0116: Missing module and function docstrings** | Pylint | Convention | 1, 12, 20, 31, 38, 42, 49, 54, 59, 64 | Neither the module nor its public functions contained docstrings explaining their purpose, parameters, and return types. | Added comprehensive docstrings conforming to PEP 257 for the module and all functions. |
| **E231 / E225: Whitespace violations** | Flake8 | Style (PEP 8) | 7, 43 | Missing whitespace after comma in `SERVICE_RATES` and missing whitespace around operator in `best=None`. | Formatted dictionary entries and assignments with standard whitespace (`best = None`, `"General": 2500, "Brake Check": 1200`). |
| **E302 / E501: Blank line spacing and line length** | Flake8 | Style (PEP 8) | 49, 77 | Missing 2 blank lines before top-level function definitions and print statement exceeding 79 characters. | Added standard 2 blank lines between function definitions and split long print strings within PEP 8 line limits. |
