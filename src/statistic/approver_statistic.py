from src.model.pull_request import PullRequest
from src.model.status import Status
from src.statistic.counter import Counter


def count_approved(pull_requests: list) -> Counter:
    pull_request_count = len(pull_requests)
    counter = Counter(pull_request_count)
    for pull_request in pull_requests:
        check_all_reviewer(pull_request, counter)
    counter.sort()
    return counter


def check_all_reviewer(pull_request: PullRequest, counter: Counter):
    reviewers = pull_request.reviewers
    for reviewer in reviewers:
        if reviewer.status == Status.APPROVED:
            counter.consider_user(reviewer.user)
