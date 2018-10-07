from src.statistic.average import Average
from src.utils.date_parser import convert_millis


def count_average_duration(pull_requests: list) -> Average:
    average = Average()
    average.str_before_block = lambda value: convert_millis(value)
    for pull_request in pull_requests:
        user = pull_request.author.user
        duration = pull_request.closed_date - pull_request.created_date
        average.consider_user(user, duration)
    return average
