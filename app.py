import requests 
import json
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

print(response)

if response.status_code == 200:

    dados_json = response.json()
    
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })


else:
    print(f'O erro foi {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items(): #Podemos fazer um laço for de nome do restaurante, 
    #dados in dados_restaurante.itens. Desse modo, pegamos apenas os itens, pois não queremos a informação do restaurante em específico agora.
    #Podemos nomear esse arquivo. Na linha de baixo, após os dois-pontos, podemos dizer que o nome_do_arquivo será 
    #igual a uma f-string com o {nome_do_restaurante} que queremos e a extensão .json.
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    
    #Para conseguir criar esse arquivo, existe um comando Python que é with open, que permite manipular os arquivos também dentro da aplicação.
    #Devemos passar duas informações para o with open().
    #Primeiro, qual é o nome do arquivo? Podemos passar a variável nome_do_arquivo, que é o arquivo que criamos anteriormente.
    #Segundo, o que queremos fazer com esse arquivo? Por exemplo, queremos escrever ou ler? Um dos modos que permite a escrita é representado pela letra w, que vem do verbo write (escrever).
    #Por convenção, podemos chamar esse arquivo de arquivo_restaurante, usando um apelido. Após os parênteses, digitamos as arquivo_restaurante.
    #Para finalizar, o que vamos fazer? Queremos criar um JSON. Para isso, precisamos importar o json.
    #Não precisa instalar, já temos o json. No início do arquivo, podemos fazer um import json.
    #Após dois-pontos de with open, vamos indicar ao JSON que queremos criar esse arquivo. Para isso, colocamos json.dump() no singular.
    #Entre parênteses, vamos passar três informações. Primeiro, quais são os dados que queremos exibir? Nesse, vamos colocar os dados que recebemos do for.
    #Após uma vírgula, colocamos o nome do arquivo que estamos trabalhando, que é o arquivo_restaurante.
    #E, por último, a identação para ficar organizado. Vamos colocar um indent igual a 4.
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:

        json.dump(dados, arquivo_restaurante, indent=4)

        