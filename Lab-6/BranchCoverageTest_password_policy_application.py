"""Branch Coverage Test Suite for password_policy application.

Target: Achieve >= 90% (Target: 100%) branch coverage across password_policy.py.
Author: N. Adil Ahmed (PES1UG24CS285)
Course: Software Engineering Lab - Lab 6
"""

import pytest
from password_policy import check_password, strength, suggest_fix


class TestPasswordPolicyBranchCoverage:
    """Comprehensive branch coverage testing exercising all conditional branches."""

    def test_check_password_branches(self):
        """Exercise all branches in check_password:

        - len(pw) < 8 (True and False)
        - len(pw) > 64 (True and False)
        - pw.lower() in COMMON (True and False)
        - Character classification loop (upper, lower, digit, special)
        - Zero count condition flags (True and False for each category)
        """
        # Branch: valid password where all conditions pass
        # len < 8 is False, len > 64 is False, common is False
        # upper > 0, lower > 0, digit > 0, special > 0
        issues = check_password("ValidPassword123!")
        assert issues == []

        # Branch: len(pw) < 8 is True
        issues_short = check_password("Short1!")
        assert "too short" in issues_short

        # Branch: len(pw) > 64 is True
        issues_long = check_password("A" * 65 + "b1!")
        assert "too long" in issues_long

        # Branch: common password is True (mixed case to test lower() evaluation)
        issues_common = check_password("Password")
        assert "common" in issues_common

        # Branch: common password is False
        issues_not_common = check_password("UniquePasswd99$")
        assert "common" not in issues_not_common

        # Branch: upper == 0 is True
        issues_no_upper = check_password("alllowercase123!")
        assert "no uppercase" in issues_no_upper

        # Branch: lower == 0 is True
        issues_no_lower = check_password("ALLUPPERCASE123!")
        assert "no lowercase" in issues_no_lower

        # Branch: digit == 0 is True
        issues_no_digit = check_password("NoDigitsAtAllHere!")
        assert "no digit" in issues_no_digit

        # Branch: special == 0 is True
        issues_no_special = check_password("NoSpecialChars123")
        assert "no special" in issues_no_special

    def test_strength_branches(self):
        """Exercise all branches in strength:

        - not issues (True):
            - len(pw) >= 14 (True -> 'strong')
            - len(pw) >= 14 (False -> 'good')
        - not issues (False):
            - len(issues) <= 2 (True -> 'weak')
            - len(issues) <= 2 (False -> 'very weak')
        """
        # Branch 1: not issues True and len >= 14 True -> "strong"
        assert strength("A1!a" * 4) == "strong"  # 16 chars

        # Branch 2: not issues True and len >= 14 False -> "good"
        assert strength("A1!aA1!a") == "good"  # 8 chars

        # Branch 3: not issues False and len(issues) <= 2 True -> "weak"
        # Has only 1 issue: no special
        assert strength("JustLettersAndDigits123") == "weak"
        # Has 2 issues: no uppercase, no special
        assert strength("onlylowercaseand123") == "weak"

        # Branch 4: not issues False and len(issues) <= 2 False -> "very weak"
        # Has 4 issues: too short, no uppercase, no digit, no special
        assert strength("xyz") == "very weak"

    def test_suggest_fix_branches(self):
        """Exercise all branches in suggest_fix:

        - not issues (True -> 'none needed')
        - not issues (False):
            - first == 'too short' (True -> 'add more characters')
            - first == 'common' (True -> 'avoid common passwords')
            - first.startswith('no ') (True -> 'add ' + first[3:])
            - fallback (False to all above -> 'shorten it')
        """
        # Branch: not issues is True
        assert suggest_fix([]) == "none needed"

        # Branch: first == 'too short' is True
        assert suggest_fix(["too short", "no digit"]) == "add more characters"

        # Branch: first == 'common' is True
        assert suggest_fix(["common", "no uppercase"]) == "avoid common passwords"

        # Branch: first.startswith('no ') is True
        assert suggest_fix(["no uppercase"]) == "add uppercase"
        assert suggest_fix(["no lowercase"]) == "add lowercase"
        assert suggest_fix(["no digit"]) == "add digit"
        assert suggest_fix(["no special"]) == "add special"

        # Branch: fallback is True (e.g. 'too long')
        assert suggest_fix(["too long"]) == "shorten it"
