import requests       # Importa a biblioteca para fazer requisições HTTP (conectar com a API)

# Configurações de acesso da API OpenWeatherMap
api_key = 'a2a8977c55fe716258461383122d8200'    #Chave API da conta do site OpenWeatherMap
city = 'Amazonas'   # Define a cidade/estado para a consulta


# Monta a URL de requisição utilizando f-strings para injetar as variáveis
# 'units=metric' define a temperatura em Celsius e 'lang=pt_br' traz a descrição em português
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br'


# Realiza a requisição do tipo GET para a API
response = requests.get(url)


# Verifica se a requisição foi bem-sucedida (Status Code 200 significa "OK")
if response.status_code == 200:
    data = response.json()      # Converte a resposta do servidor para o formato JSON (dicionário em Python)

    # Extrai as informações específicas de dentro do dicionário retornado
    temperature = data['main']['temp']          # Obtém a temperatura atual
    description = data['weather'][0]['description']          # Obtém a descrição do clima

    # Exibe os dados formatados para o usuário
    print(f'A temperatura em {city} é {temperature}ºC. Tempo: {description}.')


# Trata os possíveis erros caso a requisição falhe (ex: cidade não encontrada ou chave inválida)
else:
    print('Um erro ocorreu ao pesquisar a temperatura.')
    print(f'Status Code: {response.status_code}')       # Exibe o código do erro (ex: 404, 401)
    print(f'Resposta do Servidor: {response.text}')     # Exibe os detalhes do erro retornados pela API