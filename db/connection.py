from pymongo import MongoClient
import os
from dotenv import load_dotenv


load_dotenv()

connection_string = os.getenv("MONGODB_CONNECTION_STRING")
database_name = os.getenv("MONGODB_DATABASE_NAME")


class MongoConnection:
    def __init__(self, connection_string: str, database_name: str):
        self.connection_string = connection_string
        self.database_name = database_name
        self.client = None
        self.database = None

    def connect(self):
        try:
            self.client = MongoClient(self.connection_string)
            self.database = self.client[self.database_name]
        except Exception as e:
            print(f"Falha na conexão com o Banco de Dados: {e}")

    def get_database(self):
        return self.database
