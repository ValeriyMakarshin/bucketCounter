import datetime

RUBICON_DATE = datetime.datetime(year=2018, month=10, day=1).timestamp()
MILLISECOND_IN_SECOND = 1e3


def start_date_after_rubicon_date(start_millisecond: int) -> bool:
    start_second = start_millisecond // MILLISECOND_IN_SECOND
    return start_second > RUBICON_DATE
