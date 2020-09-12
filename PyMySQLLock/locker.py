"""Main module."""

from .connection_factory import ConnectionFactory
from .lock import Lock


class Locker:

    lock_class = Lock

    def __init__(self, *args, **kwargs):
        self.connection_factory = ConnectionFactory(*args, **kwargs)

    def lock(self, name):
        return self.lock_class(self, name)
