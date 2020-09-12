=============
py-mysql-lock
=============
------------------------------
MySQL Backed Locking Primitive
------------------------------

.. image:: https://img.shields.io/pypi/v/py-mysql-lock.svg
        :target: https://pypi.python.org/pypi/py-mysql-lock

.. image:: https://img.shields.io/travis/sanketplus/py-mysql-lock
        :target: https://travis-ci.com/sanketplus/py-mysql-lock

.. image:: https://codecov.io/github/sanketplus/py-mysql-lock/coverage.svg?branch=master&precision=2
    :target: https://codecov.io/gh/sanketplus/py-mysql-lock
    :alt: Coverage!

.. image:: https://readthedocs.org/projects/py-mysql-lock/badge/?version=latest
        :target: https://Py-MySQL-Lock.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


py-mysql-lock provides locking primitive based on MySQL's GET_LOCK

Though there are mature locking primitives provided by systems like Zookeeper and etcd, when you have an application which is primarily dependent on MySQL for its uptime and health, added resiliency provided by systems just mentioned doesn't add much benefit. py-mysql-lock helps when you have multiple application instances which are backed by a common mysql instance and you want only one of those application instances to hold a lock and do certain tasks.


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
* Setting UP CI with Travis
* Increase code coverage and add its badge
* pypi publish
* video demo
* mark this project ready for review


**Credits:** This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
