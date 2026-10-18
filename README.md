# Open Source AI Workshop

In this workshop you run an open AI model, **Gemma 4 E4B**, entirely on your own laptop
and use it inside VS Code as a *debugging tutor*.

The tutor is set up to **give hints, not answers**. It cannot edit your files.
You find the bugs and type every fix yourself.

---

## Part 1: Setup 

The model download is about 10 GB.

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
git clone https://github.com/ctrlcn1nja/gemma-workshop.git
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


## Part 2: Tuning Hyperparameters
## Tuning Gemma's Generation Parameters with Ollama

This guide demonstrates how to change **temperature** and **top-p** while running Google's Gemma model locally using Ollama.

These parameters influence how the model selects tokens when generating responses.

## 1. Start Gemma in Ollama

Open your terminal and run:

```bash
ollama run gemma4-workshop:latest
```

This starts an interactive chat session with Gemma. If the model isn't already downloaded, Ollama will download it first.

You should see:

```text
>>> Send a message (/? for help)
```

You can now enter prompts directly.

## 2. Changing Temperature

**Temperature controls how strongly the model favors high-probability tokens.**

- **Low temperature (0.0–0.3):** More consistent and predictable responses.
- **Medium temperature (0.5–0.9):** A balance between consistency and variation.
- **High temperature (1.0–1.5):** More varied and potentially unusual responses.

Inside the Ollama interactive session, enter:

```text
/set parameter temperature 0.2
```

Try the following prompt:

```text
Write a two-sentence description of an abandoned research station in Antarctica.
```

Now increase the temperature:

```text
/set parameter temperature 1.3
```

Run the same prompt again and compare the responses.

**Experiment:** Repeat the prompt three times at each temperature. Higher temperature generally increases variation, but the effect is probabilistic and isn't guaranteed for every response.

## 3. Changing Top-p

**Top-p (nucleus sampling) controls which tokens are eligible for selection based on cumulative probability.**

For example, if `top_p = 0.8`, the model considers the smallest set of highest-probability tokens whose combined probability reaches at least 80%.

Inside the interactive session, enter:

```text
/set parameter top_p 0.3
```

Try this prompt:

```text
Invent a creative name and a short backstory for a futuristic research laboratory.
```

Now increase top-p:

```text
/set parameter top_p 0.95
```

Repeat the same prompt.

- **Low top-p:** Restricts sampling to a smaller set of likely tokens.
- **High top-p:** Allows a broader set of tokens to be considered.

For a controlled comparison, keep temperature fixed while changing top-p.

## 4. View Your Current Settings

Inside Ollama, run:

```text
/show parameters
```

To see the available interactive commands:

```text
/?
```

To clear the current conversation history:

```text
/clear
```

Clear the conversation between trials to prevent earlier responses from influencing later ones.

## 5. Suggested Experiment

| Experiment | Temperature | Top-p |
|---|---:|---:|
| Low temperature | 0.2 | 1.0 |
| High temperature | 1.3 | 1.0 |
| Low top-p | 0.9 | 0.3 |
| High top-p | 0.9 | 0.95 |

For each experiment:

1. Set both parameters using `/set parameter`.
2. Run `/clear` to reset conversation history.
3. Enter the same prompt.
4. Repeat several times, clearing history between trials.
5. Compare response variation, coherence, and relevance.

## 6. Exit Ollama

Enter:

```text
/bye
```

## Key Takeaways

- **Temperature** changes the probability distribution used to select the next token.
- **Top-p** restricts the candidate tokens based on cumulative probability.
- Lower temperature does not guarantee factual correctness.
- Higher temperature does not automatically mean better creativity.
- These parameters affect generation behavior, not the model's learned knowledge.

**Remember:** When comparing generation settings, change one parameter at a time to understand its effect.

## Part 3: The tasks

| Task | Folder | For | How to run the tests |
| --- | --- | --- | --- |
| Challenge | `offline_outpost_student/` | Workshop Challenge | `python game.py` |

Run the file above to see current status in the game.

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