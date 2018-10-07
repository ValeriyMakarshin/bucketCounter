from src.model.action_type import ActionType
from src.model.user import User


class Comment(object):

    def __init__(self, user: User, action: ActionType):
        self.user = user
        self.action = action
