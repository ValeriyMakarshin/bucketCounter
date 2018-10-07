from src.statistic.counter import Counter


def count_author(pull_requests: list) -> Counter:
    counter = Counter()
    for pull_request in pull_requests:
        counter.consider_user(pull_request.author.user)
    return counter
