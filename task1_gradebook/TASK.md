# Task 1: Fix the Gradebook (main task, ~20 minutes)

`gradebook.py` calculates grades for a class. It has **4 bugs**.
You start at `3/9 tests passed`. Heads up: fixing one bug can make a
different test start failing. That is normal. It means a hidden bug just showed up.

## Steps

1. Run the tests and look at what fails:

   ```
   python task1_gradebook/test_gradebook.py
   ```

2. Open the Chat view. Check that the model is **gemma4-workshop** and the agent is **debug-tutor**.

3. Use the tutor to find each bug. Good questions to ask:
   - "What does `average` do? Walk me through it with the list [80, 90, 100]."
   - "The test `test_letter_grade_exact_boundaries` fails. Where should I look?"
   - "What does `list.remove` do to the list I pass in?"
   - "Give me a hint about `drop_lowest`, but don't tell me the answer."

4. **Type each fix yourself**, then run the tests again.

5. You are done when you see `9/9 tests passed`.

## Keep a short log

For each bug, write one line:

| Bug | Where | Did the tutor's hint help? | Was the hint correct? |
| --- | --- | --- | --- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

## Halfway through

Turn off your Wi-Fi and ask the tutor another question. It still works,
because the model runs on your laptop.

## Finished early?

Try **Task 2** in `task2_store/`. It is much harder.
