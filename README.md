# AuthTokenFetcher

**AuthTokenFetcher** é um código Python que demonstra como obter um token de autenticação de um determinado site ou api e utilizá-lo para fazer requisições autenticadas.

## Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes Python)
- Conta de acesso ao site que fornece o token

## Configuração

1. Clone o repositório:

    ```bash
    git clone https://github.com/victorgoveia/AuthTokenFetcher.git
    cd AuthTokenFetcher
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure suas credenciais no arquivo `.env`. Use o arquivo `.env.example` como base:

    ```plaintext
    LOGIN=seu_email_ou_usuario
    PASSWORD=sua_senha
    ```

5. Renomeie o arquivo `.env.example` para `.env`:

    ```bash
    mv .env.example .env
    ```

## Uso

### 1. Obtenção do Token

Execute o script `get_token.py` para obter o token de autenticação:

```bash
python get_token.py


### 2. Utilização da função para obter o token antes de iniciar a requisição no arquivo `get_data_from_api.py`