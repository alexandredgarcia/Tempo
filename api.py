import requests

api_key = 'a2a8977c55fe716258461383122d5667'
city = 'Amazonas'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt_br'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']

    print(f'A temperatura em {city} é {temperature}ºC. Tempo: {description}.')

else:
    print('Um erro ocorreu ao pesquisar a temperatura.')
    print(f'Status Code: {response.status_code}')
    print(f'Resposta do Servidor: {response.text}')