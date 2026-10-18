# OFFLINE: The Last Outpost

A short Python debugging challenge for a workshop about locally running Gemma.

## Story and objective

A storm has cut off the internet at a remote research outpost. The water purifier, automated food collector, and emergency radio are malfunctioning. Repair **all three** to restore the outpost and transmit a rescue signal. There are **no days, timers, health points, or survival inventory**.

## Requirements

- Python 3.9+ (standard library only)
- Optional: Ollama with the Gemma 3 1B model, installed and downloaded **before** going offline

## Run

From the project directory:

```bash
python game.py
```

Use menu choices 1–3 to test each system and 4 to view status. The program runs diagnostics on the actual system functions. A working system is marked ONLINE. All three must pass to win.

## Debugging

1. Run the game and select a broken system.
2. Read the diagnostic output; compare expected and actual behavior.
3. Open the relevant file in `systems/` and consult your local Gemma tutor for hints.
4. Edit **only** `systems/purifier.py`, `systems/food_collector.py`, or `systems/radio.py`.
5. Exit and restart `python game.py` to reload your changes.
6. Run the tests and repeat until all systems are online.

```bash
python -m unittest discover -s tests -v
```

Several tests **intentionally fail** at first. Some passing tests are included to help you reason about edge cases. Do not modify `diagnostics.py`, `game.py`, or `tests/`.

## Local Gemma tutor (optional)

Install Ollama and download the model while connected to the internet:

```bash
ollama pull gemma3:1b
ollama create outpost-tutor -f Modelfile
ollama run outpost-tutor
```

Ollama must be running for chat to work. The `Modelfile` configures tutoring behavior; `GEMMA_RULES.md` is a human-readable expanded guide and is **not** automatically read by Ollama. A small model may occasionally break the no-solutions rule.

Once the model and dependencies are downloaded, both the game and local chatbot can operate without internet.

## Example prompt

"The water purifier diagnostic expected 16 but got -20. Here's the function. Can you give me one conceptual hint, without writing the fix?"

## Success

All three systems report ONLINE, and the game displays **MISSION COMPLETE**.
