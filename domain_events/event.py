import datetime

import pytz


class Event(object):

    def __init__(self, *args, **kwargs):
        self.occurred_on = kwargs.get('occurred_on', datetime.datetime.now(tz=pytz.utc))
        self.type_name = self.type_name()

    @classmethod
    def type_name(cls):
        return "{}.{}".format(cls.__module__, cls.__name__)
