from uuid import uuid4


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Publisher:
    __metaclass__ = Singleton

    def __init__(self):
        self.__subscribers = {}

    @property
    def subscribers(self):
        return self.__subscribers.copy()

    def subscribe(self, subscriber, subscriber_uuid=None, priority=0):
        uuid = subscriber_uuid or str(uuid4())

        if uuid in self.__subscribers.keys():
            raise Exception("There already exists a subscriber with this uuid ({})".format(uuid))

        self.__subscribers[uuid] = (subscriber, priority)

        return uuid

    def publish(self, event):
        for a_subscriber in self.__order_subscribers_by_priority():
            if a_subscriber.is_subscribed_to(event):
                a_subscriber.handle(event)

    def __order_subscribers_by_priority(self):
        subscriber_index = 0
        priority_index = 1

        sorted_subscribers = sorted(
            self.__subscribers.iteritems(), key=lambda (key, value): value[priority_index], reverse=True)

        return [value[subscriber_index] for _, value in sorted_subscribers]

    def clear(self):
        self.__subscribers.clear()
