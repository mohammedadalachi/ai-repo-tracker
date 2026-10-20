# AI Repo Tracker

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-charts-3F4F75?logo=plotly&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-2C5BB4)
![pytest](https://img.shields.io/badge/pytest-6%20tests-0A9EDC?logo=pytest&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub-REST%20API-181717?logo=github&logoColor=white)
![Platform](https://img.shields.io/badge/CLI-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

Built with:

![Python, Git, GitHub and VS Code icons](https://skillicons.dev/icons?i=python,git,github,vscode)

A command-line program that finds the newest GitHub repositories for a topic,
a programming language, or both, and draws an interactive bar chart of them. It looks at repos created in the
last 90 days and shows the ones with the most stars first. Stars can be
inflated, so this is a list of popular new repos, not a measure of quality.

![Bar chart of the 30 most-starred new machine-learning repos written in Python on GitHub](screenshot.png)

## What it does

1. Asks for a topic, for example `machine learning` or `llm`. Press Enter to skip it.
2. Asks for a programming language, for example `python` or `c++`. Press Enter
   to skip it. You must give at least one of the two.
3. Calls the GitHub API and gets the first page of matching repos.
4. Prints each repo name and its star count.
5. Saves the chart as `topic_language.html` and opens it in the browser.
6. Saves the results to `topic_language.json`. If that file is less than an hour
   old, the program reads it instead of calling GitHub again.

A topic is a tag the owner put on the repo. A language is the language the repo
is written in. The topic `cpp` is the tag for C++ projects, while the language
`c++` means code written in C++.

In the chart, each bar is one repo. Click a repo name to open it on GitHub.
Hover over a bar to see the owner and the description.

## Tech stack

| Tool | Used for |
| --- | --- |
| Python | The whole program |
| `requests` | Calling the GitHub search API |
| `plotly` | The interactive bar chart (saved as HTML) |
| `json` | Caching results per search |
| `pytest` | Tests with a fixture, monkeypatch and a fake `requests` |
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

Type a topic and press Enter, then type a language and press Enter. Skip one
of them by pressing Enter. Type `q` at the topic question to quit.

## If something goes wrong

The program catches these problems, prints a message and asks for the next
search. It does not crash.

| Message | What it means |
| --- | --- |
| `Sorry! No Internet.` | The program could not reach GitHub. Check your connection. |
| `GitHub took too long.` | GitHub did not answer within 10 seconds. Try again. |
| `GitHub rate limit was reached. Please! Wait a minute.` | Status 403. You made too many requests. Wait a minute. |
| `GitHub answered with status: ...` | Any other status that is not 200. |
| `GitHub's response wasn't in the expected shape` | The answer did not have the data the program needs. |
| `Sorry! The json file got corrupted.` | The saved cache file was damaged. The program deletes it, so search again. |

## Run the tests

```text
python -m pytest
```

## Files

| File | What it holds |
| --- | --- |
| `tracker.py` | The program: fetching, saving, loading and the chart |
| `repo.py` | The `Repo` class (name, stars, owner, url, description) |
| `test_tracker.py` | Six pytest tests with a fixture, monkeypatch and a fake `requests` |
| `requirements.txt` | The libraries the project needs |
| `HOW_TO_RUN.md` | A PowerShell-only guide for beginners |
| `LICENSE` | The MIT license |

## License

MIT. See the `LICENSE` file.

## What I practiced

Classes, functions, loops, error handling, JSON files, the GitHub API,
Plotly charts, pytest, and git.
