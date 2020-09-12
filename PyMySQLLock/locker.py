"""Main module."""

from .connection_factory import ConnectionFactory
from .lock import Lock


class Locker:
    """
    Locker is primary interface to user with this library. Locker is used to create locks with given name.
    """
    lock_class = Lock

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        self.connection_factory = ConnectionFactory(*args, **kwargs)

    def lock(self, name):
        """
        Creates and returns a Lock object with given name.
        :param name: Name of the lock.
        :return: A Lock object.
        """
        return self.lock_class(self, name)
