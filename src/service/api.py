import requests

from src.utils.setting import get_bitbucket_access_token

ACCESS_TOKEN = 'Bearer {}'.format(get_bitbucket_access_token())
BASE_PROJECT_URL = 'http://git.moscow.alfaintra.net/rest/api/latest/projects/AM/repos/am-android/settings/'


def get_request(url_postfix: str):
    headers = {'Authorization': ACCESS_TOKEN}
    r = requests.get(
        BASE_PROJECT_URL + url_postfix,
        headers=headers
    )
    print(r.text)
    return r


get_request('pull-requests')
