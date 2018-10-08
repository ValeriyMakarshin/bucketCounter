from src.statistic.average import Average


def count_average_comment(pull_requests: list) -> Average:
    average = Average()
    average.str_before_block = lambda value: '{:.1f}'.format(value)
    for pull_request in pull_requests:
        user = pull_request.author.user
        average.consider_user(user, pull_request.comment_count)
    return average

