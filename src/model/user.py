class User(object):

    def __init__(self, display_name: str):
        self.display_name: str = display_name

    def __str__(self) -> str:
        return 'User(name = "{}")'.format(self.display_name)
