import requests
from bs4 import BeautifulSoup

links = []
# Fazer uma solicitação HTTP
url = "https://www.pciconcursos.com.br/cargos/informatica"
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Analisar o HTML da página
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontrar todas as listas <ul> com a classe 'link-d'
    ul_listas = soup.find_all("ul", class_="link-d")
    # Iterar sobre cada <ul>
    for ul_element in ul_listas:
        # Encontrar o primeiro filho <li> de cada <ul>
        primeiro_filho_li = ul_element.find("li")

        # Verificar se o primeiro filho <li> foi encontrado
        if primeiro_filho_li:
            # Acessar o primeiro filho <a> dentro do <li>
            primeiro_link_a = primeiro_filho_li.find("a")

            # Verificar se o primeiro link <a> foi encontrado
            if primeiro_link_a:
                # Obter o atributo 'href' do link
                link = primeiro_link_a.get("href")
                links.append(link)
            else:
                print("Nenhum link <a> encontrado dentro do primeiro filho <li>")
        else:
            print("Nenhum primeiro filho <li> encontrado dentro do <ul>")
else:
    print(f"A solicitação falhou com o código de status {response.status_code}")

for l in links:
    response = requests.get(l)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        print(soup)
    print(l)
