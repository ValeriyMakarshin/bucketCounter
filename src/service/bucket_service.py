from src.model.comment import Comment
from src.model.pull_request import PullRequest
from src.model.response import Response
from src.service.api import get_request
from src.service.parser import parse_response

PULL_REQUEST_PATH = 'pull-requests'
COMMENT_PATH = 'pull-requests/{}/activities'


def get_pull_requests(start_params: int = 0, limit_params: int = 100) -> Response:
    params = {'start': start_params, 'limit': limit_params, 'order': 'newest', 'state': 'ALL'}
    response = get_request(url_postfix=PULL_REQUEST_PATH, params=params)
    return parse_response(response, PullRequest)


def get_comments(pull_request_id: int) -> Response:
    url_postfix = COMMENT_PATH.format(pull_request_id)
    params = {'start': 0, 'limit': 500}
    response = get_request(url_postfix=url_postfix, params=params)
    return parse_response(response, Comment)
