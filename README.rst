=============
py-mysql-lock
=============
------------------------------
MySQL Backed Locking Primitive
------------------------------

.. image:: https://img.shields.io/pypi/v/PyMySQLLock.svg
        :target: https://pypi.python.org/pypi/PyMySQLLock

.. image:: https://img.shields.io/travis/sanketplus/PyMySQLLock.svg
        :target: https://travis-ci.com/sanketplus/PyMySQLLock

.. image:: https://readthedocs.org/projects/PyMySQLLock/badge/?version=latest
        :target: https://Py-MySQL-Lock.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/sanketplus/PyMySQLLock/shield.svg
     :target: https://pyup.io/repos/github/sanketplus/PyMySQLLock/
     :alt: Updates


py-mysql-lock provides locking primitive based on MySQL's GET_LOCK

Though there are mature locking primitives provided by systems like Zookeeper and etcd, when you have an application which is primarily dependent on MySQL for its uptime and health, added resiliency provided by systems just mentioned doesn't add much benefit. py-mysql-lock helps when you have multiple application instances which are backed by a common mysql instance and you want only one of those application instances to hold a lock and do certain tasks.


* Free software: MIT license
* Documentation: https://py-mysql-lock.readthedocs.io.


Features
--------

* TODO

TODO
====
* complete TODOs in code
* Expand readme with examples and features
    * learn RST :/
* Populate and tidy up docs
* readthedocs URL badge and setup
* Setting UP CI with Travis
* Increase code coverage and add its badge
* pypi publish
* video demo
* mark this project ready for review


**Credits:** This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
