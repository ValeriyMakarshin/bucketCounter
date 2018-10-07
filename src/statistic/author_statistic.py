from src.statistic.counter import Counter


def count_author(pull_requests: list) -> Counter:
    pull_request_count = len(pull_requests)
    counter = Counter(pull_request_count)
    for pull_request in pull_requests:
        counter.consider_user(pull_request.author.user)
    counter.sort()
    return counter
