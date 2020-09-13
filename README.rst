=============
py-mysql-lock
=============

------------------------------
MySQL Backed Locking Primitive
------------------------------

.. image:: https://img.shields.io/pypi/v/PyMySQLLock.svg
        :target: https://pypi.python.org/pypi/PyMySQLLock

.. image:: https://api.travis-ci.com/sanketplus/py-mysql-lock.svg
        :target: https://travis-ci.com/sanketplus/py-mysql-lock

.. image:: https://codecov.io/github/sanketplus/py-mysql-lock/coverage.svg?branch=master&precision=2
        :target: https://codecov.io/gh/sanketplus/py-mysql-lock
        :alt: Coverage!

.. image:: https://readthedocs.org/projects/py-mysql-lock/badge/?version=latest
        :target: https://Py-MySQL-Lock.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


py-mysql-lock provides locking primitive based on MySQL's GET_LOCK


Use Cases
---------

Though there are mature locking primitives provided by systems like Zookeeper and etcd, when you have an application which is primarily dependent on MySQL for its uptime and health, added resiliency provided by systems just mentioned doesn't add much benefit. py-mysql-lock helps when you have multiple application instances which are backed by a common mysql instance and you want only one of those application instances to hold a lock and do certain tasks.


    Documentation: https://py-mysql-lock.readthedocs.io


Installation
------------

py-mysql-lock can be installed from pip. Alternate installation methods can be found in `installation documentation <https://py-mysql-lock.readthedocs.io/en/latest/installation.html>`_
::

    pip install PyMySQLLock

-----
Usage
-----

py-mysql-lock works with existing python mysql libraries like PyMYSQL, mysql-connector-python amd mysqlclient.

Getting A Named Lock
--------------------

Getting a named lock is a three step process. First you will create a ``Locker`` instance. Argument to locker are the
same arguments that you give to your MySQL library's ``connect`` method. Locker then can be used to create Locks. Locks
can be acquired and released.
::

    from PyMySQLLock import Locker

    locker = Locker(host="localhost", user="root",
                    password="password", database="db")
    lock = locker.lock("lock_name")

    lock.acquire()  # returns True if lock is acquired

    # do something

    lock.release()

Timeout For Acquisition
-----------------------

Call to a lock's ``acquire`` method takes an optional ``timeout`` arguments. The value is timeout
in seconds. Default value is -1 which denotes wait for indefinite time.
::

    # wait for 10 seconds. If lock is not acquired, False is returned
    lock.acquire(timeout=10)

Refresh Interval
-----------------------

Since the lock is acquired on a mysql connection, it is important for the connection to stay alive. To prevent connection
from breaking due to inactivity, py-mysql-lock keeps pinging on the connection in background. The default ping interval
is 10 seconds and optionally can be set with ``acquire`` call,
::

    lock.acquire(timeout=10, refresh_interval_secs=1)

Get All Locks
-----------------------

You can also query the mysql database for getting all current acquired locks on the given db.
::

    locker.get_all_locks()  # returns list of names (string) of locks acquired on the db



**Credits:** This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
