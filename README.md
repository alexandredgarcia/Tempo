# Tempo

### 📝 App utilizando API externa

# 🌤️ Consulta de Clima com Python

Este é um projeto simples e funcional em Python desenvolvido para consultar as condições climáticas atuais de uma cidade específica, utilizando a API pública do **OpenWeatherMap**. 

O projeto foi criado com o objetivo de praticar conceitos fundamentais de desenvolvimento em Python, como consumo de APIs REST, manipulação de dados em formato JSON, tratamento de requisições HTTP e boas práticas de documentação para o GitHub.

## 🚀 Funcionalidades

- Conexão em tempo real com a API OpenWeatherMap.
- Consulta de temperatura atual em graus Celsius (`units=metric`).
- Descrição detalhada do clima traduzida para o português (`lang=pt_br`).
- Sistema básico de tratamento de erros e respostas do servidor (Status Code).

## 🛠️ Tecnologias e Ferramentas

- **Linguagem:** Python 3.14
- **IDE:** PyCharm 2025.3.2.1
- **Biblioteca principal:** `requests` (para comunicação HTTP)
- **API Externa:** [OpenWeatherMap API](https://openweathermap.org/)

## ⚙️ Como Executar o Projeto

### 1. Pré-requisitos
Antes de começar, você precisará ter o Python instalado em sua máquina. Além disso, é necessário instalar a biblioteca `requests`.

```bash
pip install requests

### 2. Clonando o Repositório

Abra o seu terminal e execute o comando abaixo para clonar o projeto:

```bash
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
cd nome-do-repositorio

### 3. Configurando a Chave de API
Para que o script funcione, é necessária uma chave de acesso (API Key) do OpenWeatherMap.

Cadastre-se gratuitamente em OpenWeatherMap.

Obtenha sua chave na seção "API Keys".

Substitua o valor da variável api_key no arquivo principal pelo seu token pessoal:

Python
api_key = 'SUA_CHAVE_AQUI'

### 4. Rodando o Script
Com o ambiente configurado, execute o arquivo Python:

Bash
python api.py

📈 Próximos Passos (Melhorias Futuras)
Como parte da minha evolução na trilha de aprendizado em Python, pretendo implementar as seguintes melhorias neste projeto:

[ ] Variáveis de Ambiente: Ocultar a chave da API utilizando a biblioteca python-dotenv para evitar a exposição de dados sensíveis no GitHub.

[ ] Interatividade: Permitir que o usuário digite o nome de qualquer cidade através do terminal usando input().

[ ] Interface Gráfica (GUI) / Web: Criar uma tela visual utilizando Tkinter ou um dashboard web simples com Streamlit.

💡 Este projeto faz parte do meu portfólio de estudos para transição de carreira e ingresso no mercado de desenvolvimento Python
