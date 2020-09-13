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

    def get_all_locks(self):
        """
        Get all locks queries mysql metadata table to get all user acquired locks.

        For mysql 5.7 and older, instrumentations needs to be enabled in order for this API to work. Read more at:
        https://dev.mysql.com/doc/refman/5.7/en/performance-schema-metadata-locks-table.html

        For mysql 8, this API will work on default setup of mysql.

        :return: list of locks acquired on the given mysql database
        """
        conn = self.connection_factory.new()
        with conn.cursor() as cursor:
            cursor.execute("select object_name from performance_schema.metadata_locks "
                           "where object_type = 'USER LEVEL LOCK'")
            rows = cursor.fetchall()
            return [i[0] for i in rows]
