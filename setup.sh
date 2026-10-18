#!/usr/bin/env bash
# Workshop setup for Mac / Linux. Run from the workshop folder: bash setup.sh
set -e

if ! command -v ollama >/dev/null 2>&1; then
  echo "Ollama is not installed. Get it from https://ollama.com/download and run this again."
  exit 1
fi

echo "Ollama found: $(ollama --version)"
echo
echo "Step 1/3: Downloading gemma4:e4b (about 10 GB, this can take a while)..."
ollama pull gemma4:e4b

echo
echo "Step 2/3: Creating the workshop model with a bigger context window..."
ollama create gemma4-workshop -f Modelfile

echo
echo "Step 3/3: Testing the model..."
ollama run gemma4-workshop "Say hello to a workshop student in one short sentence."

echo
echo "Done. In VS Code, select the model 'gemma4-workshop' and the agent 'debug-tutor'."
