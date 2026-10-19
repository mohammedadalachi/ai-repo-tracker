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
    welcome += "\nExamples: llm, python and machine learning.\n"
    print(welcome)
    
def ask_topic():
    """Store a topic the user entered."""
    prompt = "Enter a topic (type 'q' to quit): "
    topic = input(prompt).lower().strip().replace(' ', '-')
    return topic

def fetch_repos(topic):
    """Return the first page of GitHub results for a topic."""
    # Store the API address in a variable called url.
    url = "https://api.github.com/search/repositories"
    since = date.today() - timedelta(days=90)
    # Add the query: the given topic, sorted by stars, in the last 90 days. 
    params = {"q": f"topic:{topic} sort:stars created:>{since}"}
    
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
        
def make_chart(repos, topic):
    """Make a bar chart of the repos."""
    stars = [repo.stars for repo in repos]
    repo_links = [f"<a href='{repo.url}'>{repo.name}</a>" for repo in repos]
    hover_texts = [f"{repo.owner}<br />{repo.description}" for repo in repos]
    title = f"Newest Most-Starred {topic.title()} GitHub Repos" 
    title += " In The Last 90 Days"
    fig = px.bar(x=repo_links, y=stars, title=title, 
                 labels={'x': 'Repository', 'y': 'Stars'}, 
                 hover_name=hover_texts)
    fig.update_layout(title_font_size=28, xaxis_title_font_size=20, 
                      yaxis_title_font_size=20)
    fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
    fig.write_html(f'{topic}.html')
    webbrowser.open(f'{topic}.html')

# Run the program only when this file is started directly,
# so importing it (for example from pytest) does not start the loop
if __name__ == "__main__":
    # Display a welcome message.
    show_welcome()
    while True:
        topic_name = ask_topic()
        if topic_name == 'q':
            break
        # Keep the returned list in repos so we can pass it on.        
        try:
            path = Path(f'{topic_name}.json')
            if path.exists() and time.time() - path.stat().st_mtime < 3600:
                contents = path.read_text(encoding='utf-8')
                data = json.loads(contents)
                repos = dicts_to_repos(data)
                show_repos(repos)
                make_chart(repos, topic_name)
            else:
                repos = fetch_repos(topic_name)
                if repos == []:
                    print("No repos found for that topic.")
                else:
                    data = repos_to_dicts(repos)
                    contents = json.dumps(data)
                    path.write_text(contents, encoding='utf-8')
                    show_repos(repos)
                    make_chart(repos, topic_name)
        except requests.exceptions.ConnectionError:
            print("Sorry! No Internet.")
        except ConnectionError as err:
            print(err)
        except KeyError:
            print("GitHub's response wasn't in the expected shape")
        except requests.exceptions.Timeout:
            print("GitHub took too long.")

 