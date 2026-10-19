# AI Repo Tracker

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-charts-3F4F75?logo=plotly&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-2C5BB4)
![pytest](https://img.shields.io/badge/pytest-4%20tests-0A9EDC?logo=pytest&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub-REST%20API-181717?logo=github&logoColor=white)
![Platform](https://img.shields.io/badge/CLI-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

A command-line program that finds the newest GitHub repositories for a topic
and draws an interactive bar chart of them. It looks at repos created in the
last 90 days and shows the ones with the most stars first. Stars can be
inflated, so this is a list of popular new repos, not a measure of quality.

![Bar chart of the 30 most-starred new machine-learning repos on GitHub](screenshot.png)

## What it does

1. Asks for a topic, for example `machine learning` or `llm`.
2. Calls the GitHub API and gets the first page of matching repos.
3. Prints each repo name and its star count.
4. Saves the chart as `topic.html` and opens it in the browser.
5. Saves the results to `topic.json`. If that file is less than an hour old,
   the program reads it instead of calling GitHub again.

In the chart, each bar is one repo. Click a repo name to open it on GitHub.
Hover over a bar to see the owner and the description.

## Tech stack

| Tool | Used for |
| --- | --- |
| Python | The whole program |
| `requests` | Calling the GitHub search API |
| `plotly` | The interactive bar chart (saved as HTML) |
| `json` | Caching results per topic |
| `pytest` | Tests with a fixture and monkeypatch |
| Git and GitHub | Version control and hosting |

## Requirements

- Python 3.10 or newer
- `requests`, `plotly` and `pytest` (listed in `requirements.txt`)

Install them with:

```text
python -m pip install -r requirements.txt
```

## How to run

```text
python tracker.py
```

Type a topic and press Enter. Type `q` to quit.

If GitHub says too many requests, wait a minute and try again.

## Run the tests

```text
python -m pytest
```

## Files

| File | What it holds |
| --- | --- |
| `tracker.py` | The program: fetching, saving, loading and the chart |
| `repo.py` | The `Repo` class (name, stars, owner, url, description) |
| `test_tracker.py` | Four pytest tests with a fixture and monkeypatch |
| `requirements.txt` | The libraries the project needs |
| `HOW_TO_RUN.md` | A PowerShell-only guide for beginners |

## What I practiced

Classes, functions, loops, error handling, JSON files, the GitHub API,
Plotly charts, pytest, and git.
