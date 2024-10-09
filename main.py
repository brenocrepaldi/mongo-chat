from controllers.auth_controller import AuthController
from controllers.message_controller import MessageController
from views.cli_view import CLIView


def main():
    cli_view = CLIView()
    auth_controller = AuthController(cli_view)
    message_controller = MessageController(cli_view)

    while True:
        option = cli_view.show_main_menu()
        if option == 1:
            auth_controller.login()
        elif option == 2:
            auth_controller.create_account()
        elif option == 3:
            message_controller.send_message()
        elif option == 4:
            message_controller.view_messages()
        elif option == 0:
            break
        else:
            cli_view.show_invalid_option()


if __name__ == "__main__":
    main()
