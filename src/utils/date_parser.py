import datetime

RUBICON_DATE = datetime.datetime(year=2018, month=10, day=1).timestamp()
MILLISECOND_IN_SECOND = 1e3
MILLISECOND_IN_DAY = 1e3 * 60 * 60 * 24


def start_date_after_rubicon_date(start_millisecond: int) -> bool:
    start_second = start_millisecond // MILLISECOND_IN_SECOND
    return start_second > RUBICON_DATE


def convert_millis(millis: int) -> str:
    millis /= MILLISECOND_IN_DAY
    delta = datetime.timedelta(millis)
    delta -= datetime.timedelta(microseconds=delta.microseconds)
    return delta.__str__()
