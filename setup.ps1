# Workshop setup for Windows. Run from the workshop folder:
#   powershell -ExecutionPolicy Bypass -File setup.ps1
$ErrorActionPreference = "Stop"

if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) {
    Write-Host "Ollama is not installed. Get it from https://ollama.com/download, restart PowerShell, and run this again."
    exit 1
}

Write-Host "Ollama found: $(ollama --version)"
Write-Host ""
Write-Host "Step 1/3: Downloading gemma4:e4b (about 10 GB, this can take a while)..."
ollama pull gemma4:e4b

Write-Host ""
Write-Host "Step 2/3: Creating the workshop model with a bigger context window..."
ollama create gemma4-workshop -f Modelfile

Write-Host ""
Write-Host "Step 3/3: Testing the model..."
ollama run gemma4-workshop "Say hello to a workshop student in one short sentence."

Write-Host ""
Write-Host "Done. In VS Code, select the model 'gemma4-workshop' and the agent 'debug-tutor'."
