
class Lock:
    """
    Represents a lock object which has one-to-one correspondence with a Mysql connection.
    A lock is held by a connection.
    """
    def __init__(self, locker, name):
        """

        :param locker: Instance of Locker which will be used to generate new mysql connections.
        :param name: Name of the lock
        """
        self.locker = locker
        self.name = name
        self.acquired = False
        self.conn = None

    def acquire(self, timeout=-1):
        """
        Try to obtain lock with the set name.

        :param timeout: Timeout for getting the lock in seconds. Defaults to -1 which will wait for indefinite time.
        :return: The return value is True if the lock is acquired successfully, False if not (for example if the
        timeout expired).
        """
        # TODO: refresh conn after lock is acquired
        self.conn = self.locker.connection_factory.new()
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT GET_LOCK(%s, %s)", (self.name, str(timeout)))
            rows = cursor.fetchall()
            ret_value = rows[0][0]
            if isinstance(ret_value, int) and ret_value == 1:
                self.acquired = True
                return True
        return False

    def release(self):
        """
        Releases the lock and closes the corresponding mysql connection.

        :return: No return value.
        """
        with self.conn.cursor() as cursor:
            cursor.execute("DO RELEASE_LOCK(%s)", (self.name,))
        # this anyway releases the lock
        self.conn.close()
        self.conn = None
        self.acquired = False

    def locked(self):
        """
        Check whether lock is acquired or not.

        :return: True if lock is acquired, False if not.
        """
        return self.acquired
