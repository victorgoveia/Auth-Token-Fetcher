import requests
import os
from dotenv import load_dotenv

load_dotenv()


LOGIN = os.environ.get("LOGIN")
PASSWORD = os.environ.get("PASSWORD")


def get_token():
    url = "https://suaurl.com.br/api/auth"

    payload = {
        "email": LOGIN,  
        "password": PASSWORD,
    }
    req = requests.post(url, json=payload)

    if req.status_code == 200:

        req_data = req.json()

        if req_data.get("success"):
            token = req_data["data"].get("token")
            return token
        else:
            print("Autenticação falhou:", req_data.get("msg"))
    else:
        print("Erro ao acessar a API:", req.status_code)
        print(req.text)

    return None


token = get_token()

if token:
    print("Token obtido com sucesso: Bearer", token)
else:
    print("Falha ao obter o token.")
