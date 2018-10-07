from src.model.author import Author


class PullRequest(object):

    def __init__(self, pull_request_id: int, title: str, created_date: int, closed_date: int, author: Author):
        self.pull_request_id: int = pull_request_id
        self.title: str = title
        self.created_date: int = created_date
        self.closed_date: int = closed_date
        self.author: Author = author
