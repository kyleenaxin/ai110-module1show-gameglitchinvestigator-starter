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


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used only Claude Code in this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  One AI suggestion that was correct was fixing the point system. Claude was able to identify that when the guess was wrong, there were times that points would be awarded when the number guessed was odd, even though it was incorrect.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI suggestion suggested that the range of acceptable values be between 1 and 50. This is actually incorrect because the range needs to be between 1 and 100. Additionally, I wanted AI to help me add a feature that when I hit the enter button, it would submit the user's guess. While it did implement this feature, it accidentally also shifted my submit button and disabled its functionality. After each suggestion, I always completed testing and read through their suggestions.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I think the best way to decide whether a bug was really fixded is to test it using a test case and to go and manually run through the game ot see if the changes stuck.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One test that I just manually ran was checking to see if the attempts left number aligned with the actual attempts I had left. I decided to go to the site and manually test it. I counted how many attempts I had taken, and saw if the number displayed was accurate with the number of attempts that I had left.
- Did AI help you design or understand any tests? How?
AI definitely helped me design and understand tests. I had it explain to me the tests that were already written. THen I described the kind of testing I wanted on the new bugs I fixed, and it helped me design them.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Essentially, everytime something happens on the front end, or the user interface (the part you can see), Streamlit reruns the entire app.py from top to bottom. It's like you're refreshing a webpage every time you do something on the page.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing habit, a prompting strategy, or a way you used Git.
    I definitely want to have AI tools explain to me how things work, especially pre-existing architecture and design before I try to change anything. Otherwise it can cause problems down the road.
- What is one thing you would do differently next time you work with AI on a coding task?
    I think I would do my best to review the changes that they suggest more closely, and try to really understand the code that they are adding on a deeper level.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
    I think that i used to think that all AI code was amazing and the answer to everything, and that it was rarely wrong. However, in this project I have noticed that many times the implementation can be incorrect.