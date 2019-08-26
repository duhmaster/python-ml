import configparser
import os


class Config:
    data = []

    path = 'config/main.config.ini'

    parser = configparser.ConfigParser()

    def create_config(self, path):
        self.parser.add_section('DB')
        self.parser.set('DB', 'host', '10.227.1.4')
        self.parser.set('DB', 'database', 'acma')
        self.parser.set('DB', 'user', 'root')
        self.parser.set('DB', 'password', '123')

        with open(path, 'w') as config_file:
            self.parser.write(config_file)

    def skip_config(self):
        self.parser = configparser.ConfigParser()
        self.create_config(self.path)
        return True

    def load(self):
        if not os.path.exists(self.path):
            self.create_config(self.path)

        self.parser = configparser.ConfigParser()
        self.parser.read(self.path)

        self.data = self.parser.items()
        return True


config = Config()
