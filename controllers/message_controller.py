from models.models import MongoModel, Message
from services.crypto_service import CryptoService
from db.connection import connection_string, database_name


class MessageController:
    def __init__(self, cli_view):
        self.cli_view = cli_view
        self.model = MongoModel(connection_string, database_name)
        self.crypto_service = CryptoService("chave_secreta")  # CHAVE SECRETA

    def send_message(self):
        sender = self.cli_view.get_sender()
        receiver = self.cli_view.get_receiver()
        content = self.cli_view.get_message_content()
        encrypted_content = self.crypto_service.encrypt(content)
        message = Message(sender, receiver, encrypted_content)
        self.model.add_message(message)
        self.cli_view.show_message_sent()

    def view_messages(self):
        messages = self.model.get_messages()
        for message in messages:
            decrypted_content = self.crypto_service.decrypt(message["content"])
            self.cli_view.show_message(
                message["sender"], message["receiver"], decrypted_content
            )
