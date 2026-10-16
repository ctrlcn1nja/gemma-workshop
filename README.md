# Local AI Workshop: Debugging with Gemma 4

In this workshop you run an open AI model, **Gemma 4 E4B**, entirely on your own laptop
and use it inside VS Code as a *debugging tutor*.

The tutor is set up to **give hints, not answers**. It cannot edit your files.
You find the bugs and type every fix yourself.

---

## Part 1: Setup (do this before the workshop if you can)

The model download is about 10 GB. Please download it at home, not on workshop Wi-Fi.

### 1. Install the tools

| Tool | Where to get it |
| --- | --- |
| VS Code | https://code.visualstudio.com |
| Python 3.10 or newer | https://www.python.org/downloads |
| Ollama (version 0.20 or newer) | https://ollama.com/download |
| Git | https://git-scm.com/downloads (Macs usually have it already) |
| A GitHub account | https://github.com/signup (students can get Copilot free through GitHub Education) |

### 2. Get the workshop files

```
git clone https://github.com/YOUR-ORG/gemma-workshop.git
cd gemma-workshop
```

No Git? On the GitHub page, click **Code → Download ZIP** and unzip it.

### 3. Download the model and create the workshop version

In the `gemma-workshop` folder, run:

- **Mac / Linux:** `bash setup.sh`
- **Windows (PowerShell):** `powershell -ExecutionPolicy Bypass -File setup.ps1`

The script downloads `gemma4:e4b` and creates a copy called **`gemma4-workshop`**
with a bigger context window, so the model can see your whole file at once.
At the end it should print a short hello from the model.

> **Laptop with 8 GB of RAM?** Open `Modelfile`, change `16384` to `8192`,
> and run the setup script again.

### 4. Connect the model to VS Code

1. Open the `gemma-workshop` folder in VS Code (**File → Open Folder…**),
   or run `code .` from inside it.
2. Install the recommended extensions when VS Code asks (GitHub Copilot Chat and Python).
3. Sign in to GitHub when Copilot asks.
4. Open the Chat view, click the **model picker** at the bottom of the chat box,
   choose **Manage Models…**, select **Ollama**, and tick **gemma4-workshop**.
   (Exact labels can differ a little between VS Code versions.)
5. In the chat box, pick **gemma4-workshop** as the model and **debug-tutor** as the agent.

**Quick check:** ask the tutor *"What does gradebook.py do?"* It should answer about the code.

---

## Part 2: The rules

1. Always use the **debug-tutor** agent with the **gemma4-workshop** model.
2. Type every fix yourself. Do not paste code from the chat.
3. Run the tests after every change.
4. If the tutor's hint is wrong, that counts as a finding. Small models make mistakes.
   Write it down.

---

## Part 3: The tasks

| Task | Folder | For | How to run the tests |
| --- | --- | --- | --- |
| Main task | `task1_gradebook/` | Everyone | `python task1_gradebook/test_gradebook.py` |
| Challenge | `task2_store/` | If you finish early or want a real challenge | `python task2_store/test_store.py` |

Each folder has a `TASK.md` with instructions. Start with Task 1.

---

## Part 4: Things to try during the workshop

- **Unplug the internet.** Turn off Wi-Fi halfway through and keep working.
  The model still answers, because it runs on your machine. Your code never leaves your laptop.
- **Jailbreak challenge (last 5 minutes).** Try to get the tutor to give you the full fixed code.
  If it works, think about why. Is a system prompt a real security boundary?

---

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `ollama: command not found` | Restart your terminal after installing Ollama. On Windows, restart VS Code too. |
| Model not listed in VS Code | Make sure Ollama is running (`ollama list` should work), then reopen Manage Models. |
| Answers are very slow | Close other apps. Set `num_ctx` to `8192` in `Modelfile` and rerun setup. |
| The tutor "forgot" the code | Your context window is too small. Rerun setup with the `Modelfile`. |
| No **debug-tutor** in the agent list | Make sure you opened *this* folder, not its parent. |


## Tuning the model for your laptop

Both settings live in the `Modelfile`. After any change, rerun:

    ollama create gemma4-workshop -f Modelfile

Then in VS Code, run **Ollama: Refresh Models** (or reload the window).

### Context size (how much the model can "see" at once)

Change this line in `Modelfile`:

    PARAMETER num_ctx 16384

| Value | When to use |
| --- | --- |
| 8192 | Laptop with 8 GB RAM, or answers are very slow |
| 16384 | Default, good for most laptops |
| 32768 | 16 GB+ RAM and the tutor seems to "forget" your file |
| 65536 | 32 GB+ RAM or a strong GPU |

### GPU or CPU

Ollama uses your GPU automatically if it can. To choose yourself,
add one of these lines to `Modelfile`:

    PARAMETER num_gpu 0     # CPU only: slower, works on every laptop
    PARAMETER num_gpu 99    # put the whole model on the GPU (if it fits)

Leave the line out to let Ollama decide (recommended).

### Check what you actually got

Ask the tutor one question, then run:

    ollama ps

Look at the PROCESSOR column:
- `100% GPU`: running fully on your graphics card (fastest)
- `100% CPU`: running on the processor only
- `30%/70% CPU/GPU`: split between them. If it's slow, lower `num_ctx`
  until it shows `100% GPU`.

Notes:
- **Mac (Apple Silicon):** the GPU shares memory with the system, so
  Ollama uses it automatically. You don't need `num_gpu`.
- **Windows/Linux with NVIDIA:** the GPU is used automatically if the
  drivers are up to date.
- **Laptops with only built-in Intel/AMD graphics:** expect CPU.
  That's fine, just slower.