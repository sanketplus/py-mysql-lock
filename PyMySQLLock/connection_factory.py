
class ConnectionFactory:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        # TODO: support more mysql libs
        try:
            from pymysql import connect
        except ImportError:
            raise Exception("No mysql connector found.")

        # testing the given parameters
        # TODO: add this later
        try:
            test_conn = connect(*self.args, **self.kwargs)
            test_conn.ping()
        except Exception as e:
            raise Exception(f"Could not connect to db with given parameters using module {connect.__module__}: {e}")
        self.connector = connect

    def new(self):
        return self.connector(*self.args, **self.kwargs)
