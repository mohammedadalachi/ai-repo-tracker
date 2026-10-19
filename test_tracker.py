import pytest
from tracker import repos_to_dicts, dicts_to_repos, ask_topic
from repo import Repo

@pytest.fixture
def one_dict():
    """Return a single dictionary for other test functions to use."""
    one_dict = {'name': 'zero-to-hero', 'stars': 30000,
                   'owner': 'Abderrahamane',
                   'url': 'https://github.com/abderrahmane/zero-to-hero',
                   'description': 'master LLMs from zero to hero'}
    return one_dict

def test_repos_to_dicts(one_dict):
    """repos_to_dicts turns a list of Repo objects into a list of dictionaries."""
    repo = Repo('zero-to-hero', 30_000, 'Abderrahamane',
                'https://github.com/abderrahmane/zero-to-hero',
                'master LLMs from zero to hero')
    repos = [repo]
    dicts = repos_to_dicts(repos)
    single_dict = dicts[0]
    assert single_dict == one_dict
    
def test_dicts_to_repos(one_dict):
    """dicts_to_repos turns a list of dictionaries into a list of repositories."""
    list_of_dict = [one_dict]
    repos = dicts_to_repos(list_of_dict)
    repo = repos[0]
    assert repo.name == 'zero-to-hero'
    assert repo.stars == 30_000
    assert repo.owner == 'Abderrahamane'
    assert repo.url == 'https://github.com/abderrahmane/zero-to-hero'
    assert repo.description == 'master LLMs from zero to hero'
    
def test_ask_topic(monkeypatch):
    """ask_topic lowers, strips and hyphenates the typed topic."""
    def fake_input(_prompt):
        return " Machine Learning"
    monkeypatch.setattr('builtins.input', fake_input)
    assert ask_topic() == "machine-learning"
    
def test_dicts_to_repos_empty():
    """dicts_to_repos returns an empty list when given an empty list."""
    list_of_dict = []
    repos = dicts_to_repos(list_of_dict)
    assert repos == []