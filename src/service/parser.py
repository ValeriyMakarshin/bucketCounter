import json

from src.model.author import Author
from src.model.pull_request import PullRequest
from src.model.response import Response
from src.model.user import User

JSON = '{"size":25,"limit":25,"isLastPage":false,"values":[{"id":7021,"version":2,"title":"Feature/fast tranfer ","state":"OPEN","open":true,"closed":false,"createdDate":1538752080657,"updatedDate":1538766519047,"fromRef":{"id":"refs/heads/feature/fast_tranfer","displayId":"feature/fast_tranfer","latestCommit":"6cdf5cd25991454c15e2106a562e2f47c944310d","repository":{"slug":"am-android","id":4632,"name":"AM Android","scmId":"git","state":"AVAILABLE","statusMessage":"Available","forkable":true,"origin":{"slug":"am-android","id":167,"name":"AM Android","scmId":"git","state":"AVAILABLE","statusMessage":"Available","forkable":true,"project":{"key":"AM","id":106,"name":"AlfaMobile","description":"AlfaMobile","public":false,"type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/projects/AM"}]}},"public":false,"links":{"clone":[{"href":"http://u_m0z35@git.moscow.alfaintra.net/scm/am/am-android.git","name":"http"},{"href":"ssh://git@git/am/am-android.git","name":"ssh"}],"self":[{"href":"http://git.moscow.alfaintra.net/projects/AM/repos/am-android/browse"}]}},"project":{"key":"~U_M0WZ2","id":1606,"name":"Ремаренко Сергей Александрович","type":"PERSONAL","owner":{"name":"u_m0wz2","emailAddress":"SRemarenko@alfabank.ru","id":7294,"displayName":"Ремаренко Сергей Александрович","active":true,"slug":"u_m0wz2","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0wz2"}]}},"links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0wz2"}]}},"public":false,"links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0wz2/repos/am-android/browse"}]}}},"toRef":{"id":"refs/heads/feature/fast_tranfer","displayId":"feature/fast_tranfer","latestCommit":"cb89a77c45d2d8a98d4b611430386204eff53313","repository":{"slug":"am-android","id":167,"name":"AM Android","scmId":"git","state":"AVAILABLE","statusMessage":"Available","forkable":true,"project":{"key":"AM","id":106,"name":"AlfaMobile","description":"AlfaMobile","public":false,"type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/projects/AM"}]}},"public":false,"links":{"clone":[{"href":"http://u_m0z35@git.moscow.alfaintra.net/scm/am/am-android.git","name":"http"},{"href":"ssh://git@git/am/am-android.git","name":"ssh"}],"self":[{"href":"http://git.moscow.alfaintra.net/projects/AM/repos/am-android/browse"}]}}},"locked":false,"author":{"user":{"name":"u_m0wz2","emailAddress":"SRemarenko@alfabank.ru","id":7294,"displayName":"Ремаренко Сергей Александрович","active":true,"slug":"u_m0wz2","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0wz2"}]}},"role":"AUTHOR","approved":false,"status":"UNAPPROVED"},"reviewers":[{"user":{"name":"u_m0yru","emailAddress":"AYUsachev@alfabank.ru","id":10745,"displayName":"Усачев Артемий Юрьевич","active":true,"slug":"u_m0yru","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0yru"}]}},"role":"REVIEWER","approved":false,"status":"UNAPPROVED"},{"user":{"name":"u_m0wgm","emailAddress":"AASimonenko@alfabank.ru","id":6610,"displayName":"Симоненко Александр Анатольевич","active":true,"slug":"u_m0wgm","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0wgm"}]}},"role":"REVIEWER","approved":false,"status":"UNAPPROVED"},{"user":{"name":"u_m0y0v","emailAddress":"ATer-Oganisyan@alfabank.ru","id":9429,"displayName":"Тер-Оганисян Арсен Ваганович","active":true,"slug":"u_m0y0v","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0y0v"}]}},"role":"REVIEWER","approved":false,"status":"UNAPPROVED"},{"user":{"name":"rum0w72","emailAddress":"NPKrylov@alfabank.ru","id":7475,"displayName":"Крылов Николай Петрович","active":true,"slug":"rum0w72","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/rum0w72"}]}},"role":"REVIEWER","approved":false,"status":"UNAPPROVED"},{"user":{"name":"u_m10c1","emailAddress":"EKozochkin@alfabank.ru","id":15233,"displayName":"Козочкин Евгений Александрович","active":true,"slug":"u_m10c1","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m10c1"}]}},"role":"REVIEWER","approved":false,"status":"UNAPPROVED"},{"user":{"name":"u_m0zs6","emailAddress":"AVSobol@alfabank.ru","id":12880,"displayName":"Соболь Александр Владимирович","active":true,"slug":"u_m0zs6","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0zs6"}]}},"role":"REVIEWER","approved":false,"status":"UNAPPROVED"},{"user":{"name":"u_m0wtj","emailAddress":"ADNovoselov@alfabank.ru","id":7119,"displayName":"Новоселов Алексей Дмитриевич","active":true,"slug":"u_m0wtj","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0wtj"}]}},"role":"REVIEWER","approved":false,"status":"UNAPPROVED"},{"user":{"name":"u_m0z35","emailAddress":"VMakarshin@alfabank.ru","id":11473,"displayName":"Макаршин Валерий Алексеевич","active":true,"slug":"u_m0z35","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0z35"}]}},"lastReviewedCommit":"6cdf5cd25991454c15e2106a562e2f47c944310d","role":"REVIEWER","approved":true,"status":"APPROVED"},{"user":{"name":"u_m0zw3","emailAddress":"EMyasnikov@alfabank.ru","id":13094,"displayName":"Мясников Евгений Олегович","active":true,"slug":"u_m0zw3","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0zw3"}]}},"role":"REVIEWER","approved":false,"status":"UNAPPROVED"},{"user":{"name":"u_m0x0x","emailAddress":"VIlyichev@alfabank.ru","id":7878,"displayName":"Ильичев Владимир Сергеевич","active":true,"slug":"u_m0x0x","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m0x0x"}]}},"role":"REVIEWER","approved":false,"status":"UNAPPROVED"},{"user":{"name":"u_021kc","emailAddress":"MNadudik@alfabank.ru","id":5261,"displayName":"Надудик Михаил Александрович","active":true,"slug":"u_021kc","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_021kc"}]}},"role":"REVIEWER","approved":false,"status":"UNAPPROVED"},{"user":{"name":"u_m10as","emailAddress":"AKazakov2@alfabank.ru","id":15187,"displayName":"Казаков Антон Георгиевич","active":true,"slug":"u_m10as","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/u_m10as"}]}},"role":"REVIEWER","approved":false,"status":"UNAPPROVED"}],"participants":[{"user":{"name":"build-status","emailAddress":"no@reply.com","id":3217,"displayName":"hook from jenkins","active":true,"slug":"build-status","type":"NORMAL","links":{"self":[{"href":"http://git.moscow.alfaintra.net/users/build-status"}]}},"role":"PARTICIPANT","approved":false,"status":"UNAPPROVED"}],"properties":{"mergeResult":{"outcome":"CLEAN","current":true},"resolvedTaskCount":1,"commentCount":4,"openTaskCount":0},"links":{"self":[{"href":"http://git.moscow.alfaintra.net/projects/AM/repos/am-android/pull-requests/7021"}]}}],"start":0,"nextPageStart":25}'


def parse_response(json_str: str, clazz: type) -> Response:
    json_dic = json.loads(json_str)

    is_last_page: bool = bool(json_dic['isLastPage'])
    values_str = json_dic['values']

    # PullRequest == clazz
    value = list(parse_pull_request(item_json) for item_json in values_str)

    response = Response(is_last_page, value)
    return response


def parse_pull_request(json_dic: dict) -> PullRequest:
    title = json_dic['title']
    created_date = json_dic['createdDate']
    author_json = json_dic['author']
    author = parse_author(author_json)
    return PullRequest(title, created_date, author)


def parse_author(json_dic: dict) -> Author:
    user_json = json_dic['user']
    user = parse_user(user_json)
    return Author(user)


def parse_user(json_dic: dict) -> User:
    display_name = json_dic['displayName']
    return User(display_name)
