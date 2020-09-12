import importlib


SUPPORTED_MYSQL_PYTHON_LIBS = [
    "pymysql",
    "mysql.connector",
    "MySQLdb"
]


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

        # optionally a connect function can be passed, this is useful for testing and for using a custom connect
        # function other than ones given by supported libraries
        if "mysql_lib_connector" in kwargs:
            self.connector = kwargs["mysql_lib_connector"]
            del kwargs["mysql_lib_connector"]
        else:
            for module in SUPPORTED_MYSQL_PYTHON_LIBS:
                try:
                    loaded_module = importlib.import_module(module)
                    self.connector = loaded_module.connect
                except ModuleNotFoundError:
                    continue
                else:
                    break
            else:
                raise Exception("No mysql connector found. Install one of these: PyMySQL, mysql-connector-python, " +
                                "mysqlclient")

        # testing the given parameters
        try:
            test_conn = self.connector(*self.args, **self.kwargs)
            test_conn.ping()
        except Exception as e:
            raise Exception(f"Could not connect to db with given parameters using module {self.connector.__module__}: {e}")

    def new(self):
        """
        Creates a mysql connection with the found mysql library, passing the args and kwargs given with constructor.

        :return: A mysql connection
        """
        return self.connector(*self.args, **self.kwargs)
