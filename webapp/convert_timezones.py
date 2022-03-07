import pytz
from datetime import datetime


def utc_to_est(datetime_input, format_input):
    x = datetime.utcfromtimestamp(datetime_input)
    dt_utc = x.replace(tzinfo=pytz.UTC)
    my_datetime_est = dt_utc.astimezone(pytz.timezone("US/Eastern")).strftime(
        format_input
    )
    return my_datetime_est
