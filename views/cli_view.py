class CLIView:
    def show_main_menu(self):
        option = input(
            "\n1 - Fazer Login\n2 - Criar uma conta\n3 - Enviar mensagem\n4 - Ver mensagens\n0 - Sair\nEscolha a opção desejada: "
        )
        return int(option)

    def get_email(self):
        return input("Digite o email: ")

    def get_password(self):
        return input("Digite a senha: ")

    def get_name(self):
        return input("Digite seu nome: ")

    def get_sender(self):
        return input("Digite seu nome (remetente): ")

    def get_receiver(self):
        return input("Digite o nome do destinatário: ")

    def get_message_content(self):
        return input("Digite a mensagem: ")

    def show_login_success(self, name):
        print(f"\nLogin bem-sucedido! Bem-vindo, {name}!")

    def show_login_failure(self):
        print("\nLogin falhou! Email ou senha inválidos.")

    def show_account_created(self):
        print("\nConta criada com sucesso!")

    def show_message_sent(self):
        print("\nMensagem enviada com sucesso!")

    def show_message(self, sender, receiver, content):
        print(f"\nDe: {sender} Para: {receiver} - Mensagem: {content}")

    def show_invalid_option(self):
        print("\nOpção inválida!")
