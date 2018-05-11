import datetime
from dateutil import tz


def get_api_usage_info(response):
    """
    Extracts usage info from Cloudinary response
    :param response: Cloudinary API response
    :return:
    """
    reset_datetime = datetime.datetime(*response.rate_limit_reset_at[:6])
    utc_tz = tz.tzutc()
    local_tz = tz.tzlocal()
    reset_datetime = reset_datetime.replace(tzinfo=utc_tz)

    return {
        'rate_limit_remaining': response.rate_limit_remaining,
        'rate_limit_allowed': response.rate_limit_allowed,
        'rate_limit_reset_at': reset_datetime.astimezone(local_tz)
    }
