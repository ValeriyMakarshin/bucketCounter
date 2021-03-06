from src.model.pull_request import PullRequest
from src.service.bucket_service import get_pull_requests
from src.utils.date_parser import start_date_after_rubicon_date

PULL_REQUEST_COUNT_LIMIT = 100


def get_all_pull_request_with_time_limitation(state_params: str = 'ALL') -> list:
    start = 0

    all_pull_request = list()

    while True:
        iteration_result = get_pull_request_time_with_filt_time(start, PULL_REQUEST_COUNT_LIMIT, state_params)
        if len(iteration_result) == 0:
            break
        all_pull_request += iteration_result
        start += PULL_REQUEST_COUNT_LIMIT
    return all_pull_request


def get_pull_request_time_with_filt_time(start_params: int, limit_params: int, state_params: str):
    response = get_pull_requests(start_params, limit_params, state_params)
    pull_requests = response.values
    return filter_pull_request_by_time(pull_requests)


def filter_pull_request_by_time(pull_requests: list) -> list:
    return list(item for item in pull_requests if check_pull_request_by_time(item))


def check_pull_request_by_time(pull_request: PullRequest) -> bool:
    create_date = pull_request.created_date
    return start_date_after_rubicon_date(create_date)
