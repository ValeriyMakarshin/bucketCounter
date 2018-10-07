from src.model.action_type import ActionType
from src.utils.counter import Counter

TRIGGER_ACTION = ActionType.COMMENTED


def count_comment(comments: list) -> Counter:
    counter = Counter()
    for comment in comments:
        if comment.action == TRIGGER_ACTION:
            counter.consider_user(comment.user)
    return counter
