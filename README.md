# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
- [X] Detail which bugs you found.
- [X] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects "easy" mode
2. User guesses a number between 1 and 20, they choose 15
3. Game compares to actual number, and responds accordingly "Too high!"
4. The user continues to guess and receive feedback
5. The game either ends because user ran out of guesses, or because they won the game!

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

============================= test session starts =============================
platform win32 -- Python 3.13.5, pytest-9.0.3, pluggy-1.5.0 -- C:\Users\Kyleena Xin\Miniconda3\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Kyleena Xin\codepath\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.11.0
collecting ... collected 23 items

tests/test_game_logic.py::test_winning_guess PASSED                      [  4%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [  8%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 13%]
tests/test_game_logic.py::test_guess_exactly_at_boundary_low PASSED      [ 17%]
tests/test_game_logic.py::test_guess_exactly_at_boundary_high PASSED     [ 21%]
tests/test_game_logic.py::test_parse_guess_valid_integer PASSED          [ 26%]
tests/test_game_logic.py::test_parse_guess_none_input PASSED             [ 30%]
tests/test_game_logic.py::test_parse_guess_empty_string PASSED           [ 34%]
tests/test_game_logic.py::test_parse_guess_non_numeric PASSED            [ 39%]
tests/test_game_logic.py::test_parse_guess_float_string PASSED           [ 43%]
tests/test_game_logic.py::test_parse_guess_whitespace_only PASSED        [ 47%]
tests/test_game_logic.py::test_parse_guess_negative_number PASSED        [ 52%]
tests/test_game_logic.py::test_range_easy PASSED                         [ 56%]
tests/test_game_logic.py::test_range_normal PASSED                       [ 60%]
tests/test_game_logic.py::test_range_hard PASSED                         [ 65%]
tests/test_game_logic.py::test_hard_range_wider_than_normal PASSED       [ 69%]
tests/test_game_logic.py::test_normal_range_wider_than_easy PASSED       [ 73%]
tests/test_game_logic.py::test_win_early_gives_high_score PASSED         [ 78%]
tests/test_game_logic.py::test_win_score_has_floor PASSED                [ 82%]
tests/test_game_logic.py::test_too_high_deducts_points PASSED            [ 86%]
tests/test_game_logic.py::test_too_low_deducts_points PASSED             [ 91%]
tests/test_game_logic.py::test_too_high_and_too_low_deduct_same PASSED   [ 95%]
tests/test_game_logic.py::test_unknown_outcome_does_not_change_score PASSED [100%]

============================= 23 passed in 0.06s ==============================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
