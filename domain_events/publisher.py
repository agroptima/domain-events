from uuid import uuid4


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Publisher(metaclass=Singleton):

    def __init__(self):
        self.__subscribers = {}

    @property
    def subscribers(self):
        return self.__subscribers.copy()

    def subscribe(self, subscriber, subscriber_uuid=None):
        uuid = subscriber_uuid or str(uuid4())

        if uuid in list(self.__subscribers.keys()):
            raise Exception("There already exists a subscriber with this uuid ({})".format(uuid))

        self.__subscribers[uuid] = subscriber

        return uuid

    def publish(self, event):
        for uuid, a_subscriber in self.__subscribers.items():
            if a_subscriber.is_subscribed_to(event):
                a_subscriber.handle(event)

    def clear(self):
        self.__subscribers.clear()
