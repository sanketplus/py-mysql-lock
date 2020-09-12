from PyMySQLLock import Locker


def test_get_lock_success(mysql_conn_params):
    locker = Locker(**mysql_conn_params)
    l = locker.lock("test")
    l.acquire()
    # TODO: verify lock actually obtained
    l.release()
