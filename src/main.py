from datetime import datetime

from src.service.bucket_service import get_pull_requests

DATE_START = 1
SECOND_VALUE = 1e3


def get_pull_request_for_date():
    get_pull_requests()
    # print(response)


if __name__ == '__main__':
    print(1e3)
    r = datetime.fromtimestamp(1538752080657 / 1e3)
    print(r)
