from expects import (
    be_empty,
    be_false,
    be_true,
    equal,
    expect,
    have_len,
    raise_error
)
from mamba import (
    context,
    description,
    it
)

from domain_events import (
    Event,
    Publisher,
    Subscriber
)


class SpySubscriber(Subscriber):
    def __init__(self):
        self.domain_event = None
        self.is_handled = False
        self.__events_subscribed_to = []

    def handle(self, event):
        self.domain_event = event
        self.is_handled = True

    def subscribe_to(self, event_class):
        self.__events_subscribed_to.append(event_class)

    def _events_subscribed_to(self):
        return self.__events_subscribed_to


class DumbEvent(Event):

    def __init__(self, name, *args, **kwargs):
        super(DumbEvent, self).__init__(*args, **kwargs)
        self.name = name


with description('Publisher'):

    with before.all:
        Publisher().clear()

    with it('should notify subscribers'):
        domain_event = DumbEvent('Test event')
        subscriber = SpySubscriber()
        subscriber.subscribe_to(DumbEvent)
        Publisher().subscribe(subscriber)

        Publisher().publish(domain_event)

        expect(subscriber.is_handled).to(be_true)
        expect(domain_event).to(equal(subscriber.domain_event))

    with it('does not notify to subscribers not subscribed to event'):
        subscriber = SpySubscriber()
        domain_event = DumbEvent('Test Event')
        Publisher().subscribe(subscriber)

        Publisher().publish(domain_event)

        expect(subscriber.is_handled).to(be_false)

    with it('should clear all subscribers'):
        subscriber_id = Publisher().subscribe(SpySubscriber())

        Publisher().clear()

        expect(Publisher().subscribers).to(be_empty)

    with it('fails when tries to subscribe with same uuid'):
        subscriber = SpySubscriber()
        domain_event_publisher = Publisher()
        domain_event_publisher.subscribe(subscriber, subscriber_uuid="same_uuid")

        expect(lambda: domain_event_publisher.subscribe(subscriber, subscriber_uuid="same_uuid")).to(
            raise_error(Exception, "There already exists a subscriber with this uuid (same_uuid)")
        )
