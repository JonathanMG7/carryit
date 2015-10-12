# encoding:utf-8
import time
from datetime import datetime


def get_timestamp():
    now = datetime.now()
    return int(time.mktime(now.timetuple()))
