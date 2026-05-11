from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_word():

    """
    Endpoint que exibe uma mensagem que todos os Devs já conheceram
    """
    return {'Hello' : 'Word'}

@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    """
    Endpoint para ver os cardápios dos restaurantes
    """
    response = requests.get(url)

    if response.status_code == 200:

        dados_json = response.json()
        
        if restaurante is None:
            return {'Dados': dados_json}
        
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    'item': item['Item'],
                    'price': item['price'],
                    'description': item['description']
                })
        return {'Restaurantes': restaurante, 'Cardapio:': dados_restaurante}

    else:
        print(f'Erro: {response.status_code} - {response.text}')