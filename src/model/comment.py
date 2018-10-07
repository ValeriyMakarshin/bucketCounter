from src.model.action_type import ActionType
from src.model.user import User


class Comment(object):
    user: User
    action: ActionType
    message: str

    def __init__(self, user: User, action: ActionType, message: str = None):
        self.user = user
        self.action = action
        self.message = message

    def __str__(self) -> str:
        return 'Comment(user = {}, type = {}, message = {})'.format(self.user.__str__(), self.action, self.message)
