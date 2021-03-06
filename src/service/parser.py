import json

from src.model.action_type import parse_action_type
from src.model.author import Author
from src.model.comment import Comment
from src.model.pull_request import PullRequest
from src.model.response import Response
from src.model.reviewer import Reviewer
from src.model.status import parse_status
from src.model.user import User

DEFAULT_DATE_VALUE = 0


def parse_response(json_str: str, clazz: type) -> Response:
    json_dic = json.loads(json_str)

    is_last_page: bool = bool(json_dic['isLastPage'])
    values_str = json_dic['values']

    parse_lambda_dict = {
        PullRequest: lambda dic: parse_pull_request(dic),
        Comment: lambda dic: parse_comment(dic)
    }

    parse_lambda = parse_lambda_dict[clazz]
    value = list(parse_lambda(item_json) for item_json in values_str)
    response = Response(is_last_page, value)
    return response


def parse_pull_request(json_dic: dict) -> PullRequest:
    pull_request_id = json_dic['id']
    title = json_dic['title']
    created_date = json_dic['createdDate']
    closed_date = parse_closed_date(json_dic)
    comment_count = parse_comment_count(json_dic)
    reviewers_list = json_dic['reviewers']
    reviewers = list(parse_reviewers(item_json) for item_json in reviewers_list)
    author_json_dic = json_dic['author']
    author = parse_author(author_json_dic)
    return PullRequest(
        pull_request_id=pull_request_id,
        title=title,
        comment_count=comment_count,
        reviewers=reviewers,
        created_date=created_date,
        closed_date=closed_date,
        author=author
    )


def parse_closed_date(json_dic: dict) -> int:
    closed_date_key = 'closedDate'
    return json_dic[closed_date_key] if closed_date_key in json_dic else DEFAULT_DATE_VALUE


def parse_comment_count(json_dic: dict) -> int:
    comment_count_key = 'commentCount'
    properties = json_dic['properties']
    return properties[comment_count_key] if comment_count_key in properties else 0


def parse_reviewers(json_dic: dict) -> Reviewer:
    status_str = json_dic['status']
    status = parse_status(status_str)
    user_dic = json_dic['user']
    user = parse_user(user_dic)
    return Reviewer(status=status, user=user)


def parse_user(json_dic: dict) -> User:
    display_name = json_dic['displayName']
    return User(display_name)


def parse_author(json_dic: dict) -> Author:
    user_json_dic = json_dic['user']
    user = parse_user(user_json_dic)
    return Author(user)


def parse_comment(json_dic: dict) -> Comment:
    user_json_dic = json_dic['user']
    user = parse_user(user_json_dic)
    action_type_key = json_dic['action']
    action_type = parse_action_type(action_type_key)
    message = parse_message(json_dic)
    return Comment(user, action_type, message)


def parse_message(json_dic: dict) -> str:
    comment_key = 'comment'
    return json_dic[comment_key]['text'] if comment_key in json_dic else None
