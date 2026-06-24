from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

# ── check_guess ──────────────────────────────────────────────────────────────
# check_guess returns (outcome, message) — these tests unpack both values.

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "high" in message.lower()

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "low" in message.lower()

def test_guess_exactly_at_boundary_low():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_guess_exactly_at_boundary_high():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"


# ── parse_guess ───────────────────────────────────────────────────────────────

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_none_input():
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert "number" in err.lower()

def test_parse_guess_float_string():
    ok, _, _ = parse_guess("3.14")
    assert ok is False

def test_parse_guess_whitespace_only():
    ok, _, _ = parse_guess("   ")
    assert ok is False

def test_parse_guess_negative_number():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5


# ── get_range_for_difficulty ──────────────────────────────────────────────────
# These tests will fail until the function is refactored from app.py into logic_utils.py.

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 50

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 100

def test_hard_range_wider_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high

def test_normal_range_wider_than_easy():
    _, normal_high = get_range_for_difficulty("Normal")
    _, easy_high = get_range_for_difficulty("Easy")
    assert normal_high > easy_high


# ── update_score ──────────────────────────────────────────────────────────────
# These tests will fail until the function is refactored from app.py into logic_utils.py.

def test_win_early_gives_high_score():
    # Winning on attempt 1 should give more points than winning on attempt 5
    score_early = update_score(0, "Win", attempt_number=1)
    score_late = update_score(0, "Win", attempt_number=5)
    assert score_early > score_late

def test_win_score_has_floor():
    # Winning very late should still earn at least 10 points
    score = update_score(0, "Win", attempt_number=100)
    assert score >= 10

def test_too_high_deducts_points():
    score = update_score(50, "Too High", attempt_number=1)
    assert score < 50

def test_too_low_deducts_points():
    score = update_score(50, "Too Low", attempt_number=1)
    assert score < 50

def test_too_high_and_too_low_deduct_same():
    score_high = update_score(50, "Too High", attempt_number=3)
    score_low = update_score(50, "Too Low", attempt_number=3)
    assert score_high == score_low

def test_unknown_outcome_does_not_change_score():
    score = update_score(50, "Unknown", attempt_number=1)
    assert score == 50
