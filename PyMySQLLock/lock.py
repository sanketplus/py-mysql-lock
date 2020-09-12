
class Lock:
    def __init__(self, locker, name):
        self.locker = locker
        self.name = name
        self.acquired = False
        self.conn = None

    def acquire(self, timeout=-1):
        # TODO: refresh conn after lock is acquired
        # TODO: return appropriate exception or return value, compatible with current threading module
        self.conn = self.locker.connection_factory.new()
        with self.conn.cursor() as cursor:
            res = cursor.execute("SELECT GET_LOCK(%s, %s)", (self.name, str(timeout)))
            rows = cursor.fetchall()
            print(cursor.fetchone())

    def release(self):
        # TODO: exception handling, return codes?
        with self.conn.cursor() as cursor:
            res = cursor.execute("DO RELEASE_LOCK(%s)", (self.name,))
        # this anyway releases the lock
        self.conn.close()
        self.conn = None
