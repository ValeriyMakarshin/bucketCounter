from src.command.get_all_comment_from_pull_request_command import get_all_comment_from_pull_request
from src.command.get_all_pull_request_command import get_all_pull_request_with_time_limitation
from src.statistic.author_statistic import count_author
from src.statistic.comment_statistic import count_comment
from src.utils.timer import Timer


def print_statistic_comment():
    comments = get_all_comment_from_pull_request()
    statistic = count_comment(comments)
    print(statistic)


def print_statistic_pull_request_author():
    pull_requests = get_all_pull_request_with_time_limitation()
    statistic = count_author(pull_requests)
    print(statistic)


if __name__ == '__main__':
    timer = Timer()
    timer.start_timer()
    print_statistic_pull_request_author()
    print(timer.finish_timer())
