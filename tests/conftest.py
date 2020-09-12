import pytest

import PyMySQLLock.connection_factory


@pytest.fixture
def mysql_conn_params():
    return {"user": "root"}


@pytest.fixture
def mysql_connectors():
    connectors = []
    from pymysql import connect
    connectors.append(connect)

    from MySQLdb import connect
    connectors.append(connect)

    from mysql.connector import connect
    connectors.append(connect)

    return connectors
