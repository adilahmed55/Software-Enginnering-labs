"""Hypothesis Property-Based Fuzz Testing Suite for password_policy module.

Lab 7: Fuzzing for Input Validation Bugs
Student Name: N. Adil Ahmed (PES1UG24CS285)
Course: Software Engineering Lab - SETAPESU26
"""

from hypothesis import given, strategies as st
from password_policy import first_character_type, split_credentials, digit_ratio


@given(st.text() | st.none())
def test_first_character_type_no_crash(s):
    """Verify first_character_type never crashes on arbitrary text or None."""
    try:
        result = first_character_type(s)
        assert result in ("digit", "letter", "symbol", "empty", "invalid")
    except Exception as exc:  # pylint: disable=broad-exception-caught
        assert False, f"first_character_type crashed with: {type(exc).__name__}: {exc}"


@given(st.text() | st.none())
def test_split_credentials_no_crash(s):
    """Verify split_credentials never crashes on arbitrary text or None."""
    try:
        username, password = split_credentials(s)
        assert isinstance(username, str)
        assert isinstance(password, str)
    except Exception as exc:  # pylint: disable=broad-exception-caught
        assert False, f"split_credentials crashed with: {type(exc).__name__}: {exc}"


@given(st.text() | st.none())
def test_digit_ratio_no_crash(s):
    """Verify digit_ratio never crashes on arbitrary text or None."""
    try:
        ratio = digit_ratio(s)
        assert isinstance(ratio, float)
        assert 0.0 <= ratio <= 1.0
    except Exception as exc:  # pylint: disable=broad-exception-caught
        assert False, f"digit_ratio crashed with: {type(exc).__name__}: {exc}"
