from PyMySQLLock import Locker


def test_get_lock_success(mysql_conn_params, mysql_connectors):
    for connector in mysql_connectors:
        mysql_conn_params["mysql_lib_connector"] = connector
        locker = Locker(**mysql_conn_params)
        l = locker.lock("test")
        ret = l.acquire()
        assert ret

        # verify if lock is obtained by trying to acquire again with same name
        l1 = locker.lock("test")
        ret1 = l1.acquire(1)
        assert not ret1

        # release the lock now
        l.release()

        # try again to acquire
        ret1 = l1.acquire(1)
        assert ret1

        l1.release()
