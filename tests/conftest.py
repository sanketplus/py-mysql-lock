import pytest


@pytest.fixture("session")
def mysql_conn_params():
    return {"user": "root"}
