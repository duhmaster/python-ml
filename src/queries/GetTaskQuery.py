from src.base.DbConnection import db_connection


class GetTaskQuery:
    query = 'SELECT * FROM `fs30_tasks` limit 1000 '

    def get_all(self):
        global db_connection

        return db_connection.query(self.query)
