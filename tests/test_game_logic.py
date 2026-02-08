from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score
import pytest

# Tests for check_guess function with correct tuple return values
def test_winning_guess():
    """Test that matching guess and secret returns Win outcome with correct message"""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    """Test that guess > secret returns Too High outcome with correct message"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    """Test that guess < secret returns Too Low outcome with correct message"""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

# Bug fix tests: Type mismatch when secret is converted to string (even attempts)
def test_check_guess_string_secret_win():
    """Bug fix: check_guess should handle string secrets correctly (Win case)"""
    # This mimics the bug where secret is converted to string on even attempts
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_check_guess_string_secret_too_high():
    """Bug fix: check_guess should handle string secrets correctly (Too High case)"""
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"

def test_check_guess_string_secret_too_low():
    """Bug fix: check_guess should handle string secrets correctly (Too Low case)"""
    outcome, message = check_guess(40, "50")
    assert outcome == "Too Low"

# Tests for parse_guess function
def test_parse_guess_valid_integer():
    """Test parsing a valid integer string"""
    ok, guess_int, error = parse_guess("42")
    assert ok is True
    assert guess_int == 42
    assert error is None

def test_parse_guess_valid_float_string():
    """Test parsing a float string (should be converted to int)"""
    ok, guess_int, error = parse_guess("42.7")
    assert ok is True
    assert guess_int == 42
    assert error is None

def test_parse_guess_empty_string():
    """Test parsing empty string returns error"""
    ok, guess_int, error = parse_guess("")
    assert ok is False
    assert guess_int is None
    assert error == "Enter a guess."

def test_parse_guess_none_input():
    """Test parsing None returns error"""
    ok, guess_int, error = parse_guess(None)
    assert ok is False
    assert guess_int is None
    assert error == "Enter a guess."

def test_parse_guess_invalid_string():
    """Test parsing non-numeric string returns error"""
    ok, guess_int, error = parse_guess("abc")
    assert ok is False
    assert guess_int is None
    assert error == "That is not a number."

# Tests for get_range_for_difficulty function
def test_range_easy():
    """Test Easy difficulty returns correct range"""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    """Test Normal difficulty returns correct range"""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_range_hard():
    """Bug fix test: Hard difficulty range (was 1-50, check if this is intended)"""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50  # Note: Hard has smaller range than Normal (potential bug)

def test_range_unknown_difficulty():
    """Test unknown difficulty defaults to Normal range"""
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100

# Tests for update_score function
def test_score_win_first_attempt():
    """Test score update on winning (high score for quick win)"""
    new_score = update_score(0, "Win", 0)
    assert new_score == 90  # 100 - 10*(0+1) = 90

def test_score_win_multiple_attempts():
    """Test score update on winning with more attempts (lower score)"""
    new_score = update_score(0, "Win", 5)
    assert new_score == 40  # 100 - 10*(5+1) = 40

def test_score_win_minimum_points():
    """Test score update on winning with too many attempts (minimum 10 points)"""
    new_score = update_score(0, "Win", 20)
    assert new_score == 10  # Minimum score is 10

def test_score_too_high_even_attempt():
    """Test score update for Too High on even attempt number (gains points)"""
    new_score = update_score(50, "Too High", 2)
    assert new_score == 55  # 50 + 5

def test_score_too_high_odd_attempt():
    """Test score update for Too High on odd attempt number (loses points)"""
    new_score = update_score(50, "Too High", 1)
    assert new_score == 45  # 50 - 5

def test_score_too_low():
    """Test score update for Too Low always loses points"""
    new_score = update_score(50, "Too Low", 0)
    assert new_score == 45  # 50 - 5
