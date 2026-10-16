# Task 2: Fix the Store (challenge)

`store.py` runs a tiny online store with an inventory and shopping carts.
It has **5 bugs**. Some only show up when you use the code in a certain way,
and one bug can make *other* tests fail too, so the failing test is not always
where the bug is.

## Steps

1. Read the docstring at the top of `store.py`. The pricing and checkout rules
   there are the spec. The tests check them exactly.

2. Run the tests:

   ```
   python task2_store/test_store.py
   ```

3. Use the **debug-tutor** to help, then type each fix yourself.

4. You are done when you see `9/9 tests passed`.

## Good questions for the tutor

- "Why could a brand new cart already have items in it?"
- "What is the difference between copying a dict and copying a reference to it?"
- "How does Python's `round()` handle 2.5? Why?"
- "If checkout fails halfway through, what has already changed?"

## Watch the tutor closely

This task is harder for the AI too. A 4B model running on a laptop will
sometimes give confident but wrong hints here. When it does, note:

- Which bug it got wrong
- What it said
- How you figured out it was wrong

That list is the most interesting thing you can share at the end.

## Still have time?

Add a feature, still writing the code yourself:
`Cart.total()` should reject coupons below 0% or above 50% by raising `ValueError`.
Write your own test for it in `test_store.py`.
