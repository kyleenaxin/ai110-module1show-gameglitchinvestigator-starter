import random
import streamlit as st
from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 8,
    "Normal": 6,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    # FIX: start at 0 to match the New Game reset and give the correct number of attempts
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

# border=False removes the visual box; Enter key triggers the first form_submit_button (Submit Guess)
with st.form("guess_form", border=False):
    raw_guess = st.text_input(
        "Enter your guess:",
        key=f"guess_input_{difficulty}"
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        submit = st.form_submit_button("Submit Guess 🚀")
    with col2:
        new_game = st.form_submit_button("New Game 🔁")
    with col3:
        show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 0
    # FIX: use low and high from the current difficulty instead of hardcoded 1-100
    st.session_state.secret = random.randint(low, high)
    # FIX: reset score, status, and history so they don't carry over from the previous game
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.history.append(raw_guess)
        st.error(err)
    else:
        st.session_state.history.append(guess_int)

        # show an error and skip evaluation if the guess is outside the difficulty range
        if guess_int < low or guess_int > high:
            st.error(f"Out of range! Please guess a number between {low} and {high}.")
        else:
            # FIX: only count valid in-range guesses as attempts so bad input doesn't waste turns
            st.session_state.attempts += 1
            # FIX: always pass the integer secret so check_guess comparison works correctly on every attempt
            outcome, message = check_guess(guess_int, st.session_state.secret)

            if show_hint:
                st.warning(message)

            st.session_state.score = update_score(
                current_score=st.session_state.score,
                outcome=outcome,
                attempt_number=st.session_state.attempts,
            )

            if outcome == "Win":
                st.balloons()
                st.session_state.status = "won"
                st.success(
                    f"You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}"
                )
            else:
                if st.session_state.attempts >= attempt_limit:
                    st.session_state.status = "lost"
                    # FIX: rerun so the page re-renders with the updated attempt count (shows 0, not 1)
                    st.rerun()

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")
