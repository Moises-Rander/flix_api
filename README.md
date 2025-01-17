# Flix-Api

**Flix-Api** é uma API desenvolvida com Django que permite gerenciar filmes, atores, gêneros e avaliações. Através dos endpoints, você pode realizar operações CRUD completas nas entidades de filmes, atores, gêneros e avaliações. A autenticação é feita via JWT, e o tratamento de dados internos é gerido com o uso de signals e serializers.

## 📌 Link de Produção

- Acesse a API em produção: [Flix-Api](https://moisesrander.pythonanywhere.com/api/v1/movies/)

## 🔧 Tecnologias Utilizadas

- **Django**: Framework web de alto nível para Python.
- **Python**: Linguagem de programação utilizada no desenvolvimento da API.
- **SQLite**: Banco de dados utilizado para persistência de dados.
- **Django ORM**: Ferramenta para abstração de consultas ao banco de dados.
- **JWT (JSON Web Tokens)**: Utilizado para autenticação segura de usuários.
- **GitHub**: Repositório do código-fonte.
- **PythonAnywhere**: Plataforma de hospedagem onde o projeto está em produção.

## ⚙️ Funcionalidades

A **Flix-Api** possui os seguintes recursos principais:

- **Movies**: Operações CRUD para filmes, incluindo criação, atualização, deleção e listagem.
- **Genres**: Gerenciamento de gêneros de filmes (CRUD completo).
- **Actors**: CRUD para atores, com associação aos filmes.
- **Reviews**: CRUD para avaliações de filmes, permitindo que os usuários possam avaliar os filmes.

Todos os dados são retornados em formato JSON.

### Endpoints Disponíveis

- **Movies**: `/api/v1/movies/`
- **Genres**: `/api/v1/genres/`
- **Actors**: `/api/v1/actors/`
- **Reviews**: `/api/v1/reviews/`

## 💻 Como Rodar o Projeto Localmente

### 1. Clonar o Repositório

```bash
git clone https://github.com/Moises-Rander/flix_api.git
cd flix-api
```
### 2.  Criar e Ativar um Ambiente Virtual

```bash
python3 -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
```
### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```
### 4. Configuração do Banco de Dados

A API utiliza SQLite como banco de dados. Para configurar o banco, basta rodar as migrações:

```bash
python manage.py migrate
```
### 5. Criar um Superusuário (opcional, para acessar o Django Admin)

```bash
python manage.py createsuperuser
```
### 6. Rodar o Servidor Local

```bash
python manage.py runserver
```
A API estará disponível em http://127.0.0.1:8000/.

## 🔑 Autenticação
A autenticação na API é feita através de JWT (JSON Web Tokens). Você deve incluir o token no cabeçalho da requisição:

```bash
Authorization: Bearer <seu_token>
```
Para obter um token, basta fazer login e obter o JWT.

## 🚀 Produção
O projeto está hospedado no PythonAnywhere, e pode ser acessado diretamente no seguinte link:
https://moisesrander.pythonanywhere.com/api/v1/movies/

## 📧 Contato
Se tiver alguma dúvida ou sugestão, entre em contato pelo e-mail: moisesrander@outlook.com
