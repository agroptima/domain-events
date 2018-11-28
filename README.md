# Domain Events

[![Build Status](https://travis-ci.org/agroptima/domain-events.svg)](https://travis-ci.org/agroptima/domain-events)
[![License GPLv3](https://img.shields.io/badge/license-GPLv3-red.svg)](https://opensource.org/licenses/GPL-3.0)
![Python versions](https://img.shields.io/badge/python-2.7-blue.svg)

A lightweight library with an implementation of Pub-Sub.

## Install

```
$ pipenv install domain-events
```

or

```
$ pip install domain-events
```

## Usage


In order to have the pub-sub working in your application, you'll need to write your own subscribers and to subscribe them to the publisher.

`domain-events` provides an interface for subscribers that needs to be implemented by your own subscribers in the first place. Two methods are mandatory: `handle(self, event)` and `_events_subscribed_to(self)`. Following is an example of how to do it.

```python

from domain_events import Subscriber


class ExampleSubscriber(Subscriber):

    def handle(self, event):
      #  Logic to handle the occurring event

    def _events_subscribed_to(self):
      """ Return the tuple of events it is subscribed to. """

      return (AnEvent, AnotherEvent)
```

Once the subscriber is implemented, you'll need to subscribe it to the event publisher.

```python

from domain_events import Publisher

Publisher().subscribe(ExampleSubscriber())
```

Now, in order to publish an event, just call the `publish` method on the `Publisher` with one of your domain events.

```python
from domain_events import Event, Publisher


class AnEvent(Event):
    pass

Publisher().publish(AnEvent())
```

The event will be passed on to the proper subscribers.


### Subscribers priority

In order to add priority to subscribers to be executed in certain order, you can add it when subscribing the subscriber to the publisher. The higher the number the higher the priority.

```python
  publisher = Publisher()
  publisher.subscribe(a_subscriber)
  publisher.subscribe(a_subscriber_with_priority, priority=10)
  publisher.subscribe(another_subscriber_with_priority, priority=15)
```

The execution order will be:
 - another_subscriber_with_priority
 - a_subscriber_with_priority
 - a_subscriber
