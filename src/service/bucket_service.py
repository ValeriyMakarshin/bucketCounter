from src.model.pull_request import PullRequest
from src.service.api import get_request
from src.service.parser import parse_response

PULL_REQUEST_PATH = 'pull-requests'
COMMENT_PATH = 'pull-requests/{}/activities'


def get_pull_requests():
    params = {'order': 'newest', 'state': 'ALL', 'start': 0}
    return get_request(url_postfix=PULL_REQUEST_PATH, params=params)


def get_comments(pull_request_id: int):
    url_postfix = COMMENT_PATH.format(pull_request_id)
    params = {'start': 0, 'limit': 500}
    return get_request(url_postfix=url_postfix, params=params)


# print(get_comments(6961).text)
res = get_pull_requests().text
parse_response(res, PullRequest)
# print(get_pull_requests().text)
