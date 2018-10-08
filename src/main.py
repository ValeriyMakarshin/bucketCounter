from src.command.get_all_comment_from_pull_request_command import get_all_comment_from_pull_request
from src.command.get_all_pull_request_command import get_all_pull_request_with_time_limitation
from src.statistic.approver_statistic import count_approved
from src.statistic.author_statistic import count_author
from src.statistic.average_comment_statistic import count_average_comment
from src.statistic.average_duration_statistic import count_average_duration
from src.statistic.comment_statistic import count_comment
from src.utils.timer import Timer

TOP_DIVIDER = '==============={}==============='
BOTTOM_DIVIDER = '=========================================='


# Сколько тредов комментариев начал каждый человек (использовать аккуратно, запрос делается для каждого pr отдельно)
def print_statistic_comment():
    comments = get_all_comment_from_pull_request()
    statistic = count_comment(comments)
    print(statistic)
    print(BOTTOM_DIVIDER)


# Число пройденных pr для каждого человека
def print_statistic_pull_request_author():
    print(TOP_DIVIDER.format("Top Authors"))
    pull_requests = get_all_pull_request_with_time_limitation(state_params='MERGED')
    statistic = count_author(pull_requests)
    print(statistic)
    print(BOTTOM_DIVIDER)


# Число аппрувов, которые поставил человек
def print_statistic_approved():
    print(TOP_DIVIDER.format("Top Reviewers"))
    pull_requests = get_all_pull_request_with_time_limitation(state_params='MERGED')
    statistic = count_approved(pull_requests)
    print(statistic)
    print(BOTTOM_DIVIDER)


# Среднее число коментариев у автора pr
def print_statistic_comment_in_authors_pull_request():
    print(TOP_DIVIDER.format("Top pr comment"))
    pull_requests = get_all_pull_request_with_time_limitation(state_params='ALL')
    statistic = count_average_comment(pull_requests)
    print(statistic)
    print(BOTTOM_DIVIDER)


# Среднее число время прохождения pr у каждого человека (обязательно MERGED т.к. у DECLINED время закрытия выставляю 0)
def print_statistic_duration_in_authors_pull_request():
    print(TOP_DIVIDER.format("Top Duration"))
    pull_requests = get_all_pull_request_with_time_limitation(state_params='MERGED')
    statistic = count_average_duration(pull_requests)
    print(statistic)
    print(BOTTOM_DIVIDER)


# Включать нужные статистики
def check_statistic():
    # print_statistic_comment()
    print_statistic_pull_request_author()
    print_statistic_approved()
    print_statistic_comment_in_authors_pull_request()
    print_statistic_duration_in_authors_pull_request()
    pass


if __name__ == '__main__':
    timer = Timer()
    timer.start_timer()
    check_statistic()
    print(timer.finish_timer())
