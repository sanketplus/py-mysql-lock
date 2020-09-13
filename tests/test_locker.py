from PyMySQLLock import Locker


def test_get_lock_success(mysql_conn_params, mysql_connectors):
    for connector in mysql_connectors:
        mysql_conn_params["mysql_lib_connector"] = connector
        locker = Locker(**mysql_conn_params)
        l = locker.lock("test")
        ret = l.acquire(refresh_interval_secs=1)
        assert ret
        assert l.locked()

        # verify the lock returns in get_locks
        assert isinstance(locker.get_all_locks(), list)

        # verify if lock is obtained by trying to acquire again with same name
        l1 = locker.lock("test")
        ret1 = l1.acquire(timeout=1)
        assert not ret1
        assert not l1.locked()

        # release the lock now
        l.release()

        # try again to acquire
        ret1 = l1.acquire(timeout=1)
        assert ret1
        assert l1.locked()

        l1.release()


def test_mysql_error(mysql_conn_params):
    mysql_conn_params["password"] = "foo"  # this will cause an error
    try:
        locker = Locker(**mysql_conn_params)
        l = locker.lock("test")
        ret = l.acquire()
    except Exception as e:
        assert "Could not connect to db" in str(e)
