from models.models import MongoModel, User
from db.connection import connection_string, database_name


class AuthController:
    def __init__(self, cli_view):
        self.cli_view = cli_view
        self.model = MongoModel(connection_string, database_name)

    def login(self):
        email = self.cli_view.get_email()
        password = self.cli_view.get_password()
        users = self.model.get_users()

        for user in users:
            if user["email"] == email and user["password"] == password:
                self.cli_view.show_login_success(user["name"])
                return
        self.cli_view.show_login_failure()

    def create_account(self):
        name = self.cli_view.get_name()
        email = self.cli_view.get_email()
        password = self.cli_view.get_password()
        user = User(name, email, password)
        self.model.add_user(user)
        self.cli_view.show_account_created()
