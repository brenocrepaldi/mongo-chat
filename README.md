# Chat Terminal com MongoDB e Criptografia

## Descrição

Este projeto é um chat por terminal desenvolvido com o objetivo de facilitar a troca de mensagens de forma segura e eficiente. Utilizando o PyMongo, as mensagens são armazenadas em um banco de dados MongoDB, e a comunicação é protegida através de criptografia AES. O sistema permite que os usuários enviem e recebam mensagens de maneira simples, com a garantia de que as conversas são armazenadas de forma persistente e segura.

## Funcionalidades

- **Troca de Mensagens Segura:** Mensagens enviadas entre usuários são criptografadas antes de serem armazenadas.
- **Persistência de Dados:** As mensagens são salvas em um banco de dados MongoDB, assegurando que as conversas não sejam perdidas.
- **Interface de Linha de Comando:** O chat é acessível diretamente pelo terminal, proporcionando uma experiência de usuário simples e direta.
- **Autenticação de Usuários:** Os usuários podem criar contas e fazer login para participar do chat.

## Tecnologias Utilizadas

- **Python:** Linguagem principal do projeto, utilizada para a implementação de toda a lógica.
- **PyMongo:** Biblioteca que permite a interação com o MongoDB.
- **Cryptography:** Biblioteca para realizar a criptografia das mensagens utilizando o algoritmo AES.
- **MongoDB:** Banco de dados NoSQL que armazena as mensagens e dados dos usuários.

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/brenocrepaldi/chat-mongo.git
   cd MongoChat
   ```

2. **Criação do Ambiente Virtual:**
   Para garantir que todas as dependências sejam isoladas do sistema, crie e ative um ambiente virtual Python:

   macOS/Linux

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   Windows

   ```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   > **Nota:** Se estiver utilizando o PyCharm, configure o interpretador do projeto para o ambiente virtual recém-criado acessando: `File > Settings > Project: MongoChat > Python Interpreter` e selecionando o ambiente virtual `.venv`.

3. **Instale as dependências:**
   Após ativar o ambiente virtual, instale os pacotes necessários a partir do arquivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Crie as variáveis de ambiente:**
   As variáveis de ambiente são cruciais para o programa. Crie o arquivo `.env` e insira as variáveis abaixo:

   ```
   MONGODB_CONNECTION_STRING="string de conexão do MongoDB"
   MONGODB_DATABASE_NAME="nome da database"
   ```

   _Importante:_ duas coleções precisam estar criadas no banco de dados para o funcionamento do programa: `users` e `messages`.

5. **Execute o chat:**

   ```bash
   python main.py
   ```

6. **Inicie a conversa:** Siga as instruções exibidas no terminal para enviar e receber mensagens.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar um pull request ou abrir uma issue para sugestões ou problemas.

## Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.
