from abc import (
    ABCMeta,
    abstractmethod
)


class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def handle(self, event):
        pass

    @abstractmethod
    def _events_subscribed_to(self):
        pass

    def is_subscribed_to(self, event):
        for subscribed_event in self._events_subscribed_to():
            if isinstance(event, subscribed_event):
                return True

        return False
