import requests
from get_token import get_token


def build_url(page):
    base_url = "https://apisearch=&limit=100&page={page}"
    return base_url.format(page=page)


def fetch_all_data(headers):
    all_data = []
    page = 1

    while True:
        url = build_url(page)
        print(f"Realizando requisição para a página {page}")

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                if not data["data"]["items"]:
                    break
                all_data.extend(data["data"]["items"])
                page += 1
            else:
                print(f"Erro ao acessar a API: Status Code {response.status_code}")
                print(response.text)
                break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            break

    return all_data



token = get_token()
if not token:
    print("Falha ao obter o token. Verifique suas credenciais.")
    exit()
# print(token)

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json",
    "User-Agent": "Seu agent",
}

all_data = fetch_all_data(headers)

print("Dados convertidos para Excel com sucesso.")
