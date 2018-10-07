from src.command.get_all_comment_from_pull_request_command import get_all_comment_from_pull_request
from src.command.get_all_pull_request_command import get_all_pull_request_with_time_limitation
from src.statistic.approver_statistic import count_approved
from src.statistic.author_statistic import count_author
from src.statistic.average_comment_statistic import count_average_comment
from src.statistic.comment_statistic import count_comment
from src.utils.timer import Timer


# Сколько тредов комментариев начал каждый человек (использовать аккуратно, запрос делается для каждого pr отдельно)
def print_statistic_comment():
    comments = get_all_comment_from_pull_request()
    statistic = count_comment(comments)
    print(statistic)


# Число пройденных pr для каждого человека
def print_statistic_pull_request_author():
    pull_requests = get_all_pull_request_with_time_limitation(state_params='MERGED')
    statistic = count_author(pull_requests)
    print(statistic)


# Число аппрувов, которые поставил человек
def print_statistic_approved():
    pull_requests = get_all_pull_request_with_time_limitation(state_params='MERGED')
    statistic = count_approved(pull_requests)
    print(statistic)


def print_statistic_approved123():
    pull_requests = get_all_pull_request_with_time_limitation(state_params='MERGED')
    statistic = count_average_comment(pull_requests)
    print(statistic)


if __name__ == '__main__':
    timer = Timer()
    timer.start_timer()
    print_statistic_approved123()
    print(timer.finish_timer())
