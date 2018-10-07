import json

from src.model.action_type import parse_action_type
from src.model.author import Author
from src.model.comment import Comment
from src.model.pull_request import PullRequest
from src.model.response import Response
from src.model.user import User


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
    closed_date = json_dic['closedDate']
    author_json_dic = json_dic['author']
    author = parse_author(author_json_dic)
    return PullRequest(
        pull_request_id=pull_request_id,
        title=title,
        created_date=created_date,
        closed_date=closed_date,
        author=author
    )


def parse_author(json_dic: dict) -> Author:
    user_json_dic = json_dic['user']
    user = parse_user(user_json_dic)
    return Author(user)


def parse_user(json_dic: dict) -> User:
    display_name = json_dic['displayName']
    return User(display_name)


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
