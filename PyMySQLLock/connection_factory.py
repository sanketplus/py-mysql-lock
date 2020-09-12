
class ConnectionFactory:
    """
    ConnectionFactory creates new mysql connections (session). It tries to import one of supported mysql python
    connector/library and passes given arguments to that library's connect function.
    """
    def __init__(self, *args, **kwargs):
        """
        :param args: args to be passed to mysql library's connect function
        :param kwargs: kwargs to be passed to mysql library's connect function
        """
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
        """
        Creates a mysql connection with the found mysql library, passing the args and kwargs given with constructor.

        :return: A mysql connection
        """
        return self.connector(*self.args, **self.kwargs)
