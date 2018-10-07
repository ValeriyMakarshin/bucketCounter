from src.model.author import Author


class PullRequest(object):

    def __init__(self, title: str, created_date: int, author: Author):
        self.title: str = title
        self.created_date: int = created_date
        self.author: Author = author
