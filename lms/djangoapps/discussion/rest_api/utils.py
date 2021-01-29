"""
Utils for discussion API.
"""

from datetime import datetime

from pytz import UTC


def is_course_discussion_in_blackout(course):
    """
    Check if discussion is in blackout period or not.
    """
    discussion_blackout_status = False
    current_datetime = datetime.now(UTC)
    for blackout in course.get_discussion_blackout_datetimes():
        if blackout['start'] < current_datetime < blackout['end']:
            discussion_blackout_status = True
    return discussion_blackout_status
