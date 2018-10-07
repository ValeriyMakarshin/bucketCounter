from enum import Enum


class ActionType(Enum):
    MERGED = 'MERGED'
    APPROVED = 'APPROVED'
    COMMENTED = 'COMMENTED'
    RESCOPED = 'RESCOPED'
    REVIEWED = 'REVIEWED'  # need_work
    OPENED = 'OPENED'
    UNAPPROVED = 'UNAPPROVED'
    REOPENED = 'REOPENED'
    DECLINED = 'DECLINED'
    UPDATED = 'UPDATED'


def parse_action_type(key: str) -> ActionType:
    for item in ActionType:
        if item.value == key:
            return item
    raise Exception('new key = {}'.format(key))
