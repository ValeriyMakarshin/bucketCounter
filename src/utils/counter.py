from src.model.user import User


class Counter(object):
    def __init__(self):
        self.user_dict = dict()

    def consider_user(self, user: User):
        user_name = user.__str__()
        actual_count = self.user_dict.get(user_name)
        self.user_dict[user_name] = actual_count + 1 if actual_count else 1

    def __str__(self) -> str:
        return self.user_dict.__str__()


if __name__ == '__main__':
    counter = Counter()
    user1 = User('123')
    counter.consider_user(user1)
    print(counter)
