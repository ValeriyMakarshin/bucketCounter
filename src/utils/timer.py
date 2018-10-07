from datetime import datetime


class Timer(object):
    start_time: int
    finish_time: int

    def start_timer(self):
        self.start_time = datetime.now()

    def finish_timer(self) -> int:
        self.finish_time = datetime.now()
        return self.get_value()

    def get_value(self) -> int:
        return self.finish_time - self.start_time

    def reset(self):
        self.start_time = 0
        self.finish_time = 0
