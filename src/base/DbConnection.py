from mysql.connector import MySQLConnection, Error


class CursorByName:
    def __init__(self, cursor):
        self._cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        row = self._cursor.__next__()

        return {description[0]: row[col] for col, description in enumerate(self._cursor.description)}


class DbConnection:
    config = {}

    connection = MySQLConnection()

    def connect(self, config):
        try:
            for item in config:
                self.config[item[0]] = item[1]

            self.connection = MySQLConnection(**self.config)

        except Error as e:
            print(e)
            return False

        return True

    def query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            data = []
            for row in CursorByName(cursor):
                data.append(row)
        except Error as e:
            print(e)
            return []

        cursor.close()

        return data

    def close(self):
        try:
            self.connection.close()
        except Error as e:
            print(e)
            return False

        return True


db_connection = DbConnection()
