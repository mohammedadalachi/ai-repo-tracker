# How to run AI Repo Tracker (macOS)

This guide is for people with no GitHub or Python experience. You only need a
Mac and an internet connection. Copy each command into Terminal and press
Enter. Wait for it to finish before you type the next one.

## Step 1: Open Terminal

Press `Cmd+Space`, type `Terminal`, and press Enter.

## Step 2: Check Python

```bash
python3 --version
```

If it prints `Python 3.10` or higher, go to Step 4. If it shows an older
version, go to Step 3. If macOS asks to install "command line developer tools",
click Install, wait for it to finish, and run the command again.

## Step 3: Install Python

The simplest way is the official installer. Download the latest Python 3 for
macOS from python.org/downloads, open the file, and click through the
installer. Then close Terminal, open a new one, and run `python3 --version`
again. A new window is needed so the Mac finds the new install.

If you already use Homebrew (a tool that installs programs from the terminal),
you can run this instead:

```bash
brew install python@3.12
```

## Step 4: Download the project

This is a plain download. You do not need git or a GitHub account.

```bash
cd ~/Desktop
curl -L -o tracker.zip https://github.com/mohammedadalachi/ai-repo-tracker/archive/refs/heads/main.zip
unzip tracker.zip
cd ai-repo-tracker-main
```

## Step 5: Make a private environment

A virtual environment is a separate folder for this project's libraries, so
nothing else on your Mac is changed.

```bash
python3 -m venv .venv
```

## Step 6: Install the libraries

This uses the environment's own Python, so there is no activation step.

```bash
.venv/bin/python -m pip install -r requirements.txt
```

## Step 7: Run the tool

```bash
.venv/bin/python tracker.py
```

Type a topic such as `machine learning` and press Enter. Then type a
programming language such as `python` and press Enter. You can skip one of them
by pressing Enter, but give at least one. The chart opens in your browser. Click
a repo name to open it on GitHub. Type `q` at the topic question to quit.

## Step 8 (optional): Run the tests

```bash
.venv/bin/python -m pytest
```

## If something goes wrong

| Problem | Fix |
| --- | --- |
| `python3` shows a version below 3.10 | Install a newer Python (Step 3), open a new Terminal, and redo Step 5. |
| `command not found: python3` | Redo Step 3. |
| `brew: command not found` | You do not have Homebrew. Use the python.org installer in Step 3. |
| "GitHub rate limit was reached" | You made too many requests. Wait one minute and search again. |
| "Sorry! No Internet." | The tool could not reach GitHub. Check your connection and search again. |
| "GitHub took too long." | GitHub did not answer in time. Search again. |
| "The json file got corrupted." | A saved result file was damaged. The tool deleted it, so search again. |
| `ModuleNotFoundError` | Step 6 was skipped, or you are in the wrong folder. Run `cd ~/Desktop/ai-repo-tracker-main`, then redo Step 6. |
| A certificate error when installing libraries | If you used the python.org installer, open the Python folder in Applications and double-click `Install Certificates.command`, then redo Step 6. |
