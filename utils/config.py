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

    @staticmethod
    def get_var(item: str):
        var = getenv(item)
        if not var:
            raise EnvVariableNotFound(f"Environment variable {item} not found")
        return var


config = Config()
