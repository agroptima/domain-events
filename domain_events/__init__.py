from .event import Event
from .publisher import Publisher
from .subscriber import Subscriber


VERSION = (1, 0, 1, 'final')
__version__ = VERSION


def get_version():
    version = '{}.{}'.format(VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '{}.{}'.format(version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '{} pre-alpha'.format(version)
    else:
        if VERSION[3] != 'final':
            version = '{} {}'.format(version, VERSION[3])

    return version
