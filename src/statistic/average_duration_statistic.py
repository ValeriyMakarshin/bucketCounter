from src.statistic.average import Average


def count_average_duration(pull_requests: list) -> Average:
    average = Average()
    for pull_request in pull_requests:
        user = pull_request.author.user
        duration = pull_request.closed_date - pull_request.created_date
        average.consider_user(user, duration)
    return average
