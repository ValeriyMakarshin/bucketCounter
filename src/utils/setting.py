import os

BITBUCKET_ACCESS_TOKEN_KEY = 'BITBUCKET_ACCESS_TOKEN'


def get_bitbucket_access_token() -> str:
    return get_system_environment(BITBUCKET_ACCESS_TOKEN_KEY)


def get_system_environment(key: str) -> str:
    return os.environ[key]
