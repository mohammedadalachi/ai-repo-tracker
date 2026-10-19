# AI Repo Tracker

A command-line program that finds trending GitHub repositories for a topic
and draws an interactive bar chart of them. Trending here means repos created
in the last 90 days, with the most stars first.

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

## Requirements

- Python 3.10 or newer
- `requests`, `plotly` and `pytest`

Install them with:

```text
python -m pip install requests plotly pytest
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

## What I practiced

Classes, functions, loops, error handling, JSON files, the GitHub API,
Plotly charts, pytest, and git.
