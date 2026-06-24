# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The first time I ran it, the game includes a box that asks for user input, with 3 boxes for you to submit your guess, generate a new game, and toggle on and off a hint. 
- List at least two concrete bugs you noticed at the start  
  When you guess over 100, the hint suggests that you guess higher. 
  When you guess a negative number, the hint suggests that you guess lower.

  So the two bugs would be being able to guess higher than what is supposed to be the upper limit, and being able to guess lower than the bottom limit.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
 -1000    Number not in range   Go Lower        None
  500     Number not in range   Go higher       None
  78      Go lower              Go higher       None
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI suggestion suggested that the range of acceptable values be between 1 and 50. This is actually incorrect because the range needs to be between 1 and 100.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
