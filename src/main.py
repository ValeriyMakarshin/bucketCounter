from datetime import datetime

from src.command.get_all_comment_command import get_all_comment_for_pull_request


def get_pull_request_for_date():
    get_all_comment_for_pull_request()


if __name__ == '__main__':
    print(1e3)
    r = datetime.fromtimestamp(1538752080657 / 1e3)
    print(r)
