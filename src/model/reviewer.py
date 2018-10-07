from src.model.status import Status
from src.model.user import User


class Reviewer(object):

    def __init__(self, user: User, status: Status):
        self.user: User = user
        self.status: Status = status
