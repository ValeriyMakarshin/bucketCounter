from src.model.action_type import ActionType
from src.model.user import User


class Comment(object):

    def __init__(self, user: User, action: ActionType, message: str = None):
        self.user = user
        self.action = action
        self.message = message
