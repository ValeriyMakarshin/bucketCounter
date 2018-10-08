from src.model.user import User


class Average(object):
    str_before_block = lambda _, x: x

    def __init__(self):
        self.user_dict = dict()

    def consider_user(self, user: User, value: int):
        user_name = user.__str__()
        actual_pair = self.user_dict.get(user_name)
        if not actual_pair:
            actual_pair = Pair()
            self.user_dict[user_name] = actual_pair
        actual_pair.consider_value(value)

    def get_average_dict(self) -> dict:
        value_dict = dict()
        for user_name, pair in self.user_dict.items():
            value_dict[user_name] = pair.get_average_value()
        sorted_list = sorted(value_dict.items(), key=lambda kv: kv[1])
        return dict(sorted_list)

    def __str__(self) -> str:
        average_dict = self.get_average_dict()
        string = ''
        for user_name, user_count in average_dict.items():
            user_count = self.str_before_block(user_count)
            string += '{:35} | {:>17}\n'.format(user_name, user_count)
        return string


class Pair(object):
    value: int = 0
    count: int = 0

    def consider_value(self, value: int):
        self.value += value
        self.count += 1

    def get_average_value(self) -> float:
        return self.value / self.count
