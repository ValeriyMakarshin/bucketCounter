from src.model.action_type import ActionType
from src.model.comment import Comment
from src.statistic.counter import Counter

TRIGGER_ACTION = ActionType.COMMENTED


def count_comment(comments: list) -> Counter:
    comment_count = len(comments)
    counter = Counter(comment_count)
    for comment in comments:
        if check_comment(comment):
            counter.consider_user(comment.user)
    counter.sort()
    return counter


def check_comment(comment: Comment) -> bool:
    is_not_jenkins = comment.user.display_name != 'hook from jenkins'
    is_need_action_type = comment.action == TRIGGER_ACTION
    return is_not_jenkins and is_need_action_type
