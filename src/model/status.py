from enum import Enum


class Status(Enum):
    APPROVED = 'APPROVED'
    UNAPPROVED = 'UNAPPROVED'
    NEEDS_WORK = 'NEEDS_WORK'


def parse_status(key: str) -> Status:
    for item in Status:
        if item.value == key:
            return item
    raise Exception('Unknown key for Status = {}'.format(key))
