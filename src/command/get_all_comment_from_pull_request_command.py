from src.command.get_all_comment_command import get_all_comment_for_pull_request
from src.command.get_all_pull_request_command import get_all_pull_request_with_time_limitation


def get_all_comment_from_pull_request() -> list:
    all_comments = list()
    pull_requests = get_all_pull_request_with_time_limitation()

    for pull_request in pull_requests:
        pull_request_id = pull_request.pull_request_id
        iteration_comments = get_all_comment_for_pull_request(pull_request_id)
        all_comments += iteration_comments
    return all_comments
