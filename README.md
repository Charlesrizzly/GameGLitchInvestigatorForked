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

- [x] Describe the game's purpose.
   - The app is a Streamlit-based Number Guessing Game. The player tries to guess a secret integer (typically 1–100). After each guess the app gives a hint — "Higher" or "Lower" — until the player finds the secret number.

- [x] Detail which bugs you found.
   - The secret number reset on every interaction because it was reinitialized on each Streamlit rerun instead of being persisted in `st.session_state`.
   - The hint logic was incorrect (comparisons were reversed), causing the app to tell the player the wrong direction.
   - Attempt/count state wasn't preserved across reruns, making progress tracking unreliable.

- [x] Explain what fixes you applied.
   - Persisted the secret number and attempt counter using `st.session_state` so values survive button clicks and reruns.
   - Corrected the comparison logic so the app displays "Higher" when the guess is less than the secret and "Lower" when the guess is greater than the secret.
   - Refactored core game logic into `logic_utils.py` (pure functions for checking guesses and generating hints) and added unit tests in `tests/` to verify behavior. After these changes the tests pass with `pytest`.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
