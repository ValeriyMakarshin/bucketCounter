from src.model.user import User


class Author(object):
    def __init__(self, user: User):
        self.user: User = user
