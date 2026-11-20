"""Code Coverage Test Suite for password_policy application.

Target: Achieve >= 90% (Target: 100%) line coverage across password_policy.py.
Author: N. Adil Ahmed (PES1UG24CS285)
Course: Software Engineering Lab - Lab 6
"""

import pytest
from password_policy import check_password, strength, suggest_fix


class TestPasswordPolicyCodeCoverage:
    """Test suite targeting 100% statement/line coverage."""

    def test_check_password_valid_no_issues(self):
        """Test a fully compliant password resulting in zero issues."""
        assert check_password("ValidPassword123!") == []

    def test_check_password_too_short(self):
        """Test password shorter than 8 characters."""
        issues = check_password("Ab1!")
        assert "too short" in issues

    def test_check_password_too_long(self):
        """Test password exceeding 64 characters."""
        long_pwd = "A" * 60 + "abc1!"
        assert len(long_pwd) > 64
        issues = check_password(long_pwd)
        assert "too long" in issues

    def test_check_password_common_dictionary(self):
        """Test common password detection in lowercase and mixed case."""
        assert "common" in check_password("password")
        assert "common" in check_password("Password")
        assert "common" in check_password("123456")
        assert "common" in check_password("qwerty")
        assert "common" in check_password("letmein")

    def test_check_password_missing_uppercase(self):
        """Test password with no uppercase characters."""
        issues = check_password("validlower123!")
        assert "no uppercase" in issues

    def test_check_password_missing_lowercase(self):
        """Test password with no lowercase characters."""
        issues = check_password("VALIDUPPER123!")
        assert "no lowercase" in issues

    def test_check_password_missing_digit(self):
        """Test password with no numeric digits."""
        issues = check_password("ValidPasswordNoDigits!")
        assert "no digit" in issues

    def test_check_password_missing_special(self):
        """Test password with no special characters."""
        issues = check_password("ValidPassword1234")
        assert "no special" in issues

    def test_strength_strong(self):
        """Test valid password with length >= 14 rated as 'strong'."""
        assert strength("SuperSecurePass123!#") == "strong"

    def test_strength_good(self):
        """Test valid password with length < 14 rated as 'good'."""
        assert strength("Secure123!") == "good"

    def test_strength_weak(self):
        """Test password with 1 or 2 issues rated as 'weak'."""
        # 1 issue: no special
        assert strength("SecurePassword123") == "weak"
        # 2 issues: no uppercase, no special
        assert strength("lowercase123456") == "weak"

    def test_strength_very_weak(self):
        """Test password with more than 2 issues rated as 'very weak'."""
        # 'abc': too short, no upper, no digit, no special (4 issues)
        assert strength("abc") == "very weak"

    def test_suggest_fix_none_needed(self):
        """Test suggestion when no issues exist."""
        assert suggest_fix([]) == "none needed"

    def test_suggest_fix_too_short(self):
        """Test suggestion for too short password."""
        assert suggest_fix(["too short", "no special"]) == "add more characters"

    def test_suggest_fix_common(self):
        """Test suggestion for common password."""
        assert suggest_fix(["common", "no uppercase"]) == "avoid common passwords"

    def test_suggest_fix_no_uppercase(self):
        """Test suggestion for missing character types."""
        assert suggest_fix(["no uppercase"]) == "add uppercase"
        assert suggest_fix(["no lowercase"]) == "add lowercase"
        assert suggest_fix(["no digit"]) == "add digit"
        assert suggest_fix(["no special"]) == "add special"

    def test_suggest_fix_too_long(self):
        """Test suggestion for too long password."""
        assert suggest_fix(["too long"]) == "shorten it"
