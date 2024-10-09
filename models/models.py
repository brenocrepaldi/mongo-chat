from db.connection import MongoConnection


class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password


class Message:
    def __init__(self, sender: str, receiver: str, content: str):
        self.sender = sender
        self.receiver = receiver
        self.content = content


class MongoModel:
    def __init__(self, connection_string: str, database_name: str):
        self.connection = MongoConnection(connection_string, database_name)
        self.connection.connect()
        self.database = self.connection.get_database()

    def get_users(self):
        return list(self.database["users"].find())

    def add_user(self, user: User):
        self.database["users"].insert_one(vars(user))

    def add_message(self, message: Message):
        self.database["messages"].insert_one(vars(message))

    def get_messages(self):
        return list(self.database["messages"].find())
