import requests

from src.utils.setting import get_bitbucket_access_token

ACCESS_TOKEN = 'Bearer {}'.format(get_bitbucket_access_token())
BASE_PROJECT_URL = 'http://git.moscow.alfaintra.net/projects/AM/repos/am-android/browse'


def get_request():
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
    r = requests.get(
        'http://git.moscow.alfaintra.net/rest/api/latest/projects/AM/repos/am-android/settings/pull-requests',
        headers=headers
    )
    print(r.text)
    return r


get_request()
