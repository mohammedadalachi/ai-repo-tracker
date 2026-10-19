from repo import Repo
from pathlib import Path
from datetime import date, timedelta
import requests, time, json, webbrowser
import plotly.express as px

def show_welcome():
    """Print a welcome message to the user."""
    welcome_title = "WELCOME TO THE AI REPO TRACKER TOOL\n"
    print(welcome_title.center(80))
    welcome = "Description: ask for a tech topic you are interested in" 
    welcome += " and you will get the most starred GitHub repos" 
    welcome += " about it in the last 90 days.\n"
    welcome += "\nExamples: llm, python, cpp, csharp and machine learning.\n"
    print(welcome)
    
def ask_topic():
    """Store a topic the user entered."""
    prompt1 = "Enter a topic (type 'q' to quit): "
    topic = input(prompt1).lower().strip().replace(' ', '-')
    return topic

def ask_language():
    """Store a language the user entered."""
    prompt2 = "Enter a programming language" 
    prompt2 += " (press Enter to skip): "
    language = input(prompt2).lower().strip()
    return language

def fetch_repos(topic, language):
    """Return the first page of GitHub results for a topic, a language or both."""
    # Store the API address in a variable called url.
    url = "https://api.github.com/search/repositories"
    since = date.today() - timedelta(days=90)
    query_parts = []
    if topic:
        query_parts.append(f"topic:{topic}")
    if language:
        query_parts.append(f"language:{language}")
    query_parts.append("sort:stars")
    query_parts.append(f"created:>{since}")
    
    # Build the query from query_parts, joined with spaces. 
    params = {"q": " ".join(query_parts)}
    
    # Make a dictionary called headers to send an extra note to GitHub.
    headers = {"Accept":"application/vnd.github.v3+json"}
    # Make an API call and store the response object in r.
    r = requests.get(url, headers=headers, timeout=10, params=params)
    if r.status_code != 200:
        raise ConnectionError(f"GitHub answered with status: {r.status_code}")

    # Convert the JSON data we received into a Python dictionary.
    response_dict = r.json()

    repo_dicts = response_dict['items']
    repos = []
    for repo_dict in repo_dicts:
        repo = Repo(repo_dict['name'], repo_dict['stargazers_count'], 
                      repo_dict['owner']['login'], repo_dict['html_url'],
                      repo_dict['description'])
        repos.append(repo)
    return repos

def repos_to_dicts(repos):
    """Convert the repos into dictionaries that could be saved as JSON files."""
    dicts = []
    for repo in repos:
        info = {'name': repo.name, 'stars': repo.stars, 'owner': repo.owner, 
                'url': repo.url, 'description': repo.description}
        dicts.append(info)
    return dicts
        
def dicts_to_repos(dicts):
    """Converts the list of dictionaries into repos."""
    repos = []
    for repo_dict in dicts:
        repo = Repo(repo_dict['name'], repo_dict['stars'], repo_dict['owner'], 
                    repo_dict['url'], repo_dict['description']) 
        repos.append(repo)
    return repos

def show_repos(repos):
    """Print the name and stars count of each repo."""
    for repo in repos:
        print(repo.name)
        print(repo.stars)
        
def make_chart(repos, search_name):
    """Make a bar chart of the repos."""
    stars = [repo.stars for repo in repos]
    repo_links = [f"<a href='{repo.url}'>{repo.name}</a>" for repo in repos]
    hover_texts = [f"{repo.owner}<br />{repo.description}" for repo in repos]
    title = f"Newest Most-Starred {search_name.replace('_', ' ').strip().title()}" 
    title += " GitHub Repos In The Last 90 Days"
    fig = px.bar(x=repo_links, y=stars, title=title, 
                 labels={'x': 'Repository', 'y': 'Stars'}, 
                 hover_name=hover_texts)
    fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
                      yaxis_title_font_size=20)
    fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
    fig.write_html(f'{search_name}.html')
    webbrowser.open(f'{search_name}.html')

# Run the program only when this file is started directly,
# so importing it (for example from pytest) does not start the loop
if __name__ == "__main__":
    # Display a welcome message.
    show_welcome()
    while True:
        topic_name = ask_topic()
        if topic_name == 'q':
            break
        language_name = ask_language()
        if not topic_name and not language_name:
            print("Please! Enter at least a topic or a language")
            continue
        search_name = f"{topic_name}_{language_name}"
        # Keep the returned list in repos so we can pass it on.        
        try:
            path = Path(f'{search_name}.json')
            if path.exists() and time.time() - path.stat().st_mtime < 3600:
                contents = path.read_text(encoding='utf-8')
                data = json.loads(contents)
                repos = dicts_to_repos(data)
                show_repos(repos)
                make_chart(repos, search_name)
            else:
                repos = fetch_repos(topic_name, language_name)
                if repos == []:
                    print("No repos found for that search.")
                else:
                    data = repos_to_dicts(repos)
                    contents = json.dumps(data)
                    path.write_text(contents, encoding='utf-8')
                    show_repos(repos)
                    make_chart(repos, search_name)
        except requests.exceptions.ConnectionError:
            print("Sorry! No Internet.")
        except ConnectionError as err:
            print(err)
        except KeyError:
            print("GitHub's response wasn't in the expected shape")
        except requests.exceptions.Timeout:
            print("GitHub took too long.")
            