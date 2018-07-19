import datetime

import pytz
from expects import (
    be_above,
    be_below,
    be_false,
    be_true,
    equal,
    expect,
    raise_error
)
from mamba import (
    description,
    it
)

from domain_events import Event


class DumbEvent(Event):

    def __init__(self, name, *args, **kwargs):
        super(DumbEvent, self).__init__(*args, **kwargs)
        self.name = name


with description('Event'):
    with it('has a type name'):
        domain_event = DumbEvent(name="Test Event")

        expect(domain_event.type_name).to(equal("specs/event_spec.DumbEvent"))
        expect(domain_event.type_name).to(equal(DumbEvent.type_name()))

    with it('has a occurred_on datetime'):
        before_event = datetime.datetime.now(tz=pytz.utc)
        domain_event = DumbEvent(name="Test Event")
        after_event = datetime.datetime.now(tz=pytz.utc)

        expect(domain_event.occurred_on).to(be_above(before_event))
        expect(domain_event.occurred_on).to(be_below(after_event))
