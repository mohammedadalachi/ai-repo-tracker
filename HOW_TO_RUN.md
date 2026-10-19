# How to run AI Repo Tracker (PowerShell only)

This guide is for people with no GitHub or Python experience. You only need
Windows and an internet connection. Copy each command into PowerShell and press
Enter. Wait for it to finish before you type the next one.

## Step 1: Open PowerShell

Press the Windows key, type `PowerShell`, and press Enter.

## Step 2: Check Python

```powershell
python --version
```

If it prints `Python 3.10` or higher, go to Step 4. If it shows an error or
opens the Microsoft Store, go to Step 3.

## Step 3: Install Python

```powershell
winget install Python.Python.3.12
```

Close PowerShell and open a new one. A new window is needed so Windows finds
the new install. Run `python --version` again to confirm.

## Step 4: Download the project

This is a plain download. You do not need git or a GitHub account.

```powershell
cd $HOME\Desktop
Invoke-WebRequest https://github.com/mohammedadalachi/ai-repo-tracker/archive/refs/heads/main.zip -OutFile tracker.zip
Expand-Archive tracker.zip -DestinationPath .
cd ai-repo-tracker-main
```

## Step 5: Make a private environment

A virtual environment is a separate folder for this project's libraries, so
nothing else on your PC is changed.

```powershell
python -m venv .venv
```

## Step 6: Install the libraries

This uses the environment's own Python, so there is no activation step.
Activation is often blocked by PowerShell's script policy.

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Step 7: Run the tool

```powershell
.\.venv\Scripts\python.exe tracker.py
```

Type a topic such as `machine learning` and press Enter. The chart opens in
your browser. Click a repo name to open it on GitHub. Type `q` to quit.

## Step 8 (optional): Run the tests

```powershell
.\.venv\Scripts\python.exe -m pytest
```

## If something goes wrong

| Problem | Fix |
| --- | --- |
| `python` is not recognized | Close PowerShell, open a new one. If it still fails, redo Step 3. |
| "too many requests" or a 403 error | GitHub's rate limit. Wait one minute and run again. |
| `ModuleNotFoundError` | Step 6 was skipped, or you are in the wrong folder. Run `cd $HOME\Desktop\ai-repo-tracker-main`, then redo Step 6. |
| `winget` is not recognized | Download Python from python.org and tick "Add python.exe to PATH" in the installer. |
