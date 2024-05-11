from os import getenv
from dotenv import load_dotenv


class EnvVariableNotFound(Exception):
    pass


class Config:

    def __init__(self):
        load_dotenv()
        self.DB_URL = self.get_var("DB_URL")
        self.HOST = self.get_var("HOST")
        self.PORT = int(self.get_var("PORT"))
        self.SECRET_KEY = self.get_var("SECRET_KEY")
        self.SECRET_KEY = self.get_var("SECRET_KEY")
        self.SSL_CERTFILE_PATH = self.get_var("SSL_CERTFILE_PATH", optional=True)
        self.SSL_KEYFILE_PATH = self.get_var("SSL_KEYFILE_PATH", optional=True)
        self.SSL_CA_BUNDLE_FILE_PATH = self.get_var("SSL_CA_BUNDLE_FILE_PATH", optional=True)

    @staticmethod
    def get_var(item: str, optional: bool = False):
        var = getenv(item)
        if not var and not optional:
            raise EnvVariableNotFound(f"Environment variable {item} not found")
        return var


config = Config()
