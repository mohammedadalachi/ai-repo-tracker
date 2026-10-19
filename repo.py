class Repo:
    """A class to model a GitHub repository."""
    def __init__(self, name, stars, owner, url, description):
        self.name = name
        self.stars = stars
        self.owner = owner
        self.url = url
        self.description = description