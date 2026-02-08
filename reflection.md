# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - A simple template with title's, an entry box for integer values and 3 buttons- submit guess, new game , and show hint 
  - There’s a space for debug info that contains secret, attempts, score, difficulty, and history
  - At the left edge there's a option box to choose difficulty level- easy, normal, and difficult 
  - The game has a secret number the player has to guess. When the player enters the number the game gives hints by telling the player to go higher or lower based on the number entered compared to the secret number.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - Expected: Accurate hint based on answer submitted
    Actual:The hint given is not accurate for all difficulties
  - Expected: Game renews when the renew button is clicked
    Actual:Once you win or lose the game and want to start a new game it changes the all the info in the debugger but you can't submit a new guess and the "You already won. Start a new game to play again." or "Out of attempts! The secret was ... Score: ..." doesn't dissappear
  - Expected:Scoring should be properly logged
    Actual:The final score doesn’t reflect the debugger info


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
 - I told the Agentic AI to refactor only the check_guess logic from the file app.py to logic_utils.py but it seemed to try and do the other logics and in the process it didn't complete the process. It removed the other logics from app.py but never refactored them to logic_utils.py
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I would: 1. reload and test the local instance of the app. 2. Run the unit test created for the feature
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - It was not changing in my case. 
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Streamlit reruns the entire script top-to-bottom whenever a user interacts with a widget. Regular variables disappear on each rerun, so st.session_state stores persistent data (like game state) across reruns. You initialize it once with if key not in st.session_state, then update it during user interactions to keep values stable between reruns.
- What change did you make that finally gave the game a stable secret number?
  - None because it was not having that issue.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    - I gained a prompting strtegy which is to tell the AI to describe the functions of all the functions first so it's easier to locate where errors could come from
- What is one thing you would do differently next time you work with AI on a coding task?
 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - I no longer see AI generated code as the final solution, but as a draft  