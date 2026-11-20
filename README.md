# Software Engineering Lab Assignments — Monorepo

**Student Name:** N. Adil Ahmed  
**SRN:** PES1UG24CS285  
**Section:** E (Roll No: 39)  
**Institution:** PES University  
**Organization / Course Source:** `SETAPESU26`  

---

## Repository Index & Overview

This consolidated repository contains the complete solutions, test suites, static analysis reports, and documentation for **Labs 4, 5, 6, and 7** of the Software Engineering laboratory curriculum.

| Lab Folder | Assignment Title | Focus Area & Tools | Key Metrics / Results | Deliverables & Status |
|:---|:---|:---|:---|:---|
| [**Lab-4/**](file:///C:/Users/Asus/.gemini/antigravity/scratch/Software-Enginnering-labs/Lab-4) | **VibeCoding: Endless Runner** | AI pair-programming, Pygame, Game Physics | • Continuous Collision Detection (CCD)<br>• Capped speed curve<br>• Game Over UI + High Score<br>• Difficulty selection (1/2/3)<br>• Procedural 8-bit sound effects | Completed<br>(Code + Chat Transcript) |
| [**Lab-5/**](file:///C:/Users/Asus/.gemini/antigravity/scratch/Software-Enginnering-labs/Lab-5) | **Static Code Analysis** | Security & quality auditing via `Pylint`, `Bandit`, `Flake8` | • Pylint: **10.00 / 10** (Target > 9.5)<br>• Bandit: **0 issues** (was 4)<br>• Flake8: **0 violations** (was 4) | Completed<br>(3 separate commits + reports) |
| [**Lab-6/**](file:///C:/Users/Asus/.gemini/antigravity/scratch/Software-Enginnering-labs/Lab-6) | **Code and Branch Coverage** | Statement & branch testing via `coverage.py`, `pytest` | • Code Coverage: **100%** (Target $\ge 90\%$)<br>• Branch Coverage: **100%** (36/36 branches) | Completed<br>(2 separate commits + test suites) |
| [**Lab-7/**](file:///C:/Users/Asus/.gemini/antigravity/scratch/Software-Enginnering-labs/Lab-7) | **Fuzzing Input Validation** | Property-based fuzz testing via `Hypothesis`, `pytest` | • Uncovered 3 unhandled exception classes<br>• Hardened against `None`, empty, malformed text<br>• Passing 100% property tests | Completed<br>(Before/After logs + report) |

---

## Directory Structure

```
Software-Enginnering-labs/
├── .gitignore
├── README.md                                           <-- You are here
├── Lab-4/                                              <-- Lab 4: VibeCoding
│   ├── main.py                                         # Game entry point
│   ├── requirements.txt                                # Pygame dependency
│   ├── README.md                                       # Detailed feature & run guide
│   ├── PROMPTS_AND_CHAT_HISTORY.md                     # Comprehensive LLM prompt transcript
│   └── game/
│       ├── __init__.py
│       ├── game_engine.py                              # State machine, CCD, Game Over UI
│       ├── obstacle.py                                 # Swept-box collision detection
│       ├── player.py                                   # Jumping physics & gravity
│       └── sound_manager.py                            # Dynamic 8-bit audio synthesizer
├── Lab-5/                                              <-- Lab 5: Static Code Analysis
│   ├── vehicle_service.py                              # Refactored script (10.00/10 rating)
│   ├── vehicle_service_original.py                     # Original buggy script from assigned repo
│   ├── issues.md                                       # Prioritized issue table & remediation
│   ├── reflection.md                                   # In-depth reflection question answers
│   ├── pylint_report_before.txt                        # Pylint baseline (4.66/10)
│   ├── pylint_report.txt                               # Pylint final (10.00/10)
│   ├── bandit_report_before.txt                        # Bandit baseline (4 vulnerabilities)
│   ├── bandit_report.txt                               # Bandit final (0 issues)
│   ├── flake8_report_before.txt                        # Flake8 baseline (style violations)
│   ├── flake8_report.txt                               # Flake8 final (0 violations)
│   └── README.md
├── Lab-6/                                              <-- Lab 6: Code & Branch Coverage
│   ├── password_policy.py                              # Application module under test
│   ├── CodeCoverageTest_password_policy_application.py  # 100% statement coverage suite
│   ├── BranchCoverageTest_password_policy_application.py# 100% branch coverage suite
│   ├── initial_test_password_policy.py                 # Baseline test file (55% coverage)
│   ├── code_coverage_report.txt                        # Terminal code coverage report
│   ├── branch_coverage_report.txt                      # Terminal branch coverage report
│   └── README.md
└── Lab-7/                                              <-- Lab 7: Fuzz Testing with Hypothesis
    ├── password_policy.py                              # Hardened, defensively programmed script
    ├── password_policy_original.py                     # Original crash-prone script
    ├── test_password_policy.py                         # Hypothesis property-based fuzz tests
    ├── fuzz_test_failures.txt                          # Terminal log showing Hypothesis failure cases
    ├── fuzz_test_passed.txt                            # Terminal log showing 100% tests passing
    ├── fuzzing_report.md                               # Root-cause analysis & defensive guide
    └── README.md
```

---

## Global Quick Start Guide

### Prerequisites
Make sure Python 3.10+ is installed on your machine.

```bash
# Clone the repository
git clone https://github.com/adilahmed55/Software-Enginnering-labs.git
cd Software-Enginnering-labs

# Install testing and analysis dependencies
pip install pylint bandit flake8 coverage pytest hypothesis pygame
```

---

## Running Individual Labs

### Lab 4: Endless Runner Game
```bash
cd Lab-4
python main.py
```
- Jump: `SPACE`, `UP ARROW`, or `W`
- On Game Over: Press `[1]` Easy, `[2]` Medium, `[3]` Hard, `[R]` Restart, `[Q]` Quit.

### Lab 5: Static Analysis Checks
```bash
cd Lab-5
python vehicle_service.py              # Verify output correctness
python -m pylint vehicle_service.py     # Verify 10.00/10 quality score
python -m bandit -r vehicle_service.py  # Verify 0 security findings
python -m flake8 vehicle_service.py    # Verify 0 style violations
```

### Lab 6: Code & Branch Coverage Analysis
```bash
cd Lab-6
# Statement coverage (100% achieved)
coverage run -m pytest CodeCoverageTest_password_policy_application.py
coverage report -m

# Branch coverage (100% achieved)
coverage run --branch -m pytest BranchCoverageTest_password_policy_application.py
coverage report -m
```

### Lab 7: Fuzz Testing with Hypothesis
```bash
cd Lab-7
pytest test_password_policy.py
```
