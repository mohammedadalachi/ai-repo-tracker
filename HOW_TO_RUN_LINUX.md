# How to run AI Repo Tracker (Linux)

This guide is for people with no GitHub or Python experience. You only need
Linux and an internet connection. Copy each command into the terminal and press
Enter. Wait for it to finish before you type the next one.

The install commands in Step 3 are for Ubuntu and Debian. Other distributions
are listed there too.

## Step 1: Open a terminal

Press `Ctrl+Alt+T`. If nothing opens, search your apps for "Terminal".

## Step 2: Check Python

```bash
python3 --version
```

If it prints `Python 3.10` or higher, go to Step 4. If it shows an error or an
older version, go to Step 3.

## Step 3: Install Python

Ubuntu or Debian:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip unzip curl
```

Fedora:

```bash
sudo dnf install python3 python3-pip unzip curl
```

Arch:

```bash
sudo pacman -S python python-pip unzip curl
```

`sudo` runs a command as administrator, so it asks for your password. The
password does not show while you type. Run `python3 --version` again to confirm.

## Step 4: Download the project

This is a plain download. You do not need git or a GitHub account.

```bash
cd ~/Desktop
curl -L -o tracker.zip https://github.com/mohammedadalachi/ai-repo-tracker/archive/refs/heads/main.zip
unzip tracker.zip
cd ai-repo-tracker-main
```

If `cd ~/Desktop` fails, your Desktop folder has another name. Use `cd ~`
instead.

## Step 5: Make a private environment

A virtual environment is a separate folder for this project's libraries, so
nothing else on your computer is changed.

```bash
python3 -m venv .venv
```

On Ubuntu or Debian, an error about `ensurepip` means `python3-venv` is missing.
Install it with the command in Step 3, then run this step again.

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

If no browser opens, the tool still saved the chart as an `.html` file in the
project folder. Open that file in your browser by hand.

## Step 8 (optional): Run the tests

```bash
.venv/bin/python -m pytest
```

## If something goes wrong

| Problem | Fix |
| --- | --- |
| `python3: command not found` | Redo Step 3. |
| `ensurepip is not available` | Install `python3-venv` (Step 3), then redo Step 5. |
| `unzip: command not found` | Install it with your package manager (Step 3 lists it). |
| "GitHub rate limit was reached" | You made too many requests. Wait one minute and search again. |
| "Sorry! No Internet." | The tool could not reach GitHub. Check your connection and search again. |
| "GitHub took too long." | GitHub did not answer in time. Search again. |
| "The json file got corrupted." | A saved result file was damaged. The tool deleted it, so search again. |
| `ModuleNotFoundError` | Step 6 was skipped, or you are in the wrong folder. Run `cd ~/Desktop/ai-repo-tracker-main`, then redo Step 6. |
| The chart does not open | Open the `.html` file in the project folder with your browser. |
