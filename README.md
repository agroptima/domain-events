# Domain Events

[![Build Status](https://travis-ci.org/agroptima/domain-events.svg)](https://travis-ci.org/agroptima/domain-events)
[![License GPLv3](https://img.shields.io/badge/license-GPLv3-red.svg)](https://opensource.org/licenses/GPL-3.0)
![Python versions](https://img.shields.io/badge/python-3.x-blue.svg)

A lightweight library with an implementation of Pub-Sub.

## Install

```sh
pipenv install domain-events
```

or

```sh
pip install domain-events
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

## Publishing to PyPI

Follow these steps to publish a new version of the package to PyPI:

1. **Update the version number** in `setup.py`

2. **Install build tools** (if not already installed):

   ```sh
   pip install build twine
   ```

3. **Build the distribution packages**:

   ```sh
   python -m build
   ```

   This creates both source distribution (.tar.gz) and wheel (.whl) in the `dist/` directory.

4. **Verify the build**:

   ```sh
   twine check dist/*
   ```

5. **Upload to PyPI** using twine:

   ```sh
   twine upload dist/*
   ```

   **Note**: Use an API token instead of username/password. Configure it in `~/.pypirc`:

   ```ini
   [pypi]
   username = __token__
   password = pypi-YOUR-API-TOKEN-HERE
   ```

6. **Clean up** the build artifacts (optional):

   ```sh
   rm -rf build/ dist/ *.egg-info/
   ```

### Best Practices

- **Use version tags**: After publishing, tag the release in git:

  ```sh
  git tag -a vX.Y.Z -m "Release vX.Y.Z"
  git push origin --tags
  ```

### Prerequisites

- You need a PyPI account with the appropriate permissions to upload this package
