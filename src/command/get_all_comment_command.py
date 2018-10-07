from src.service.bucket_service import get_comments

COMMENT_COUNT_LIMIT = 500


def get_all_comment_for_pull_request(pull_request_id: int) -> list:
    start = 0
    all_comments = list()
    while True:
        iteration_result = get_comments(
            pull_request_id=pull_request_id,
            start_params=start,
            limit_params=COMMENT_COUNT_LIMIT
        )
        all_comments += iteration_result.values
        start += COMMENT_COUNT_LIMIT
        if iteration_result.is_last_page:
            break
    return all_comments
