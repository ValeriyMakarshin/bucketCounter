import datetime

RUBICON_DATE = datetime.datetime(year=2018, month=9, day=7).timestamp()
MILLISECOND_IN_SECOND = 1e3
MILLISECOND_IN_DAY = 1e3 * 60 * 60 * 24


def start_date_after_rubicon_date(start_millisecond: int) -> bool:
    start_second = start_millisecond // MILLISECOND_IN_SECOND
    return start_second > RUBICON_DATE


def convert_millis(millis: int) -> str:
    millis /= MILLISECOND_IN_DAY
    return datetime.timedelta(millis).__str__()
