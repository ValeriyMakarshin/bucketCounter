import requests

from src.utils.setting import get_bitbucket_access_token

ACCESS_TOKEN = 'Bearer {}'.format(get_bitbucket_access_token())
BASE_PROJECT_URL = 'http://git.moscow.alfaintra.net/rest/api/latest/projects/AM/repos/am-android/'


def get_request(url_postfix: str, params: dict = {}):
    headers = {'Authorization': ACCESS_TOKEN}
    response = requests.get(
        url=BASE_PROJECT_URL + url_postfix,
        headers=headers,
        params=params
    )
    return response.text


get_request('pull-requests')
