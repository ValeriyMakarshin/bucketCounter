class Response(object):

    def __init__(self, is_last_page: bool, values: list):
        self.is_last_page = is_last_page
        self.values = values
