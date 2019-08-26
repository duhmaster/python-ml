from src.base.Config import config
from src.base.DbConnection import db_connection
import src.base.Route


class App:
    route = None

    def start(self):
        global db_connection
        global config

        config.load()
        db_connection.connect(config.parser.items('DB'))

        self.route = src.base.Route.Route()
        self.route.run()

        return True

    def finish(self):
        global db_connection

        db_connection.close()
        return True
