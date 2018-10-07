from src.command.get_all_comment_from_pull_request_command import get_all_comment_from_pull_request
from src.utils.comment_statistic import count_comment


def print_statistic_comment():
    comments = get_all_comment_from_pull_request()
    statistic = count_comment(comments)
    print(statistic)


if __name__ == '__main__':
    print_statistic_comment()
