# TasksListAPI
API REST feita em Python com Flask para um sistema web de lista de tarefas. Armazena dados em uma database PostgreSQL.

O sistema é capaz de realizar criação, consulta, edição e remoção de tarefas, respeitando todos componentes do CRUD.

## Back-End

O presente repositório se trata do back-end do sistema. Trata-se de uma API REST integrada com CORS, desenvolvida em Python com o microframework Flask.
A API gerencia os dados de cada tarefa (id, título, descrição, status e data da publicação).

## Front-end do projeto

A interface gráfica para a aplicação desenvolvida encontra-se no seguinte repositório: https://github.com/ValmirNogFilho/TasksList

## Dependências

O projeto faz uso das dependências que podem ser consultadas no arquivo 'requirements.txt' do repositório. O arquivo pode ser gerado pelo seguinte comando  no terminal:

`pip freeze > requirements.txt`

## Instalação

Para execução local da API, tendo o Python instalado, entre no diretório do projeto pelo terminal e ative o ambiente virtual de desenvolvimento do Python, com o comando:

`venv\Scripts\Activate`, caso esteja usando um sistema Windows.

Em seguinda, execute o programa a partir do comando `python run.py`. O servidor será aberto em `http://127.0.0.1:5000`.
