from src.model.action_type import ActionType
from src.model.user import User


class Reviewer(object):

    def __init__(self, user: User, status: ActionType):
        self.user: User = user
        self.status: ActionType = status
