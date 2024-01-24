# TasksListAPI
API REST feita em Python com Flask para um sistema web de lista de tarefas. Armazena dados em uma database SQLite.

O sistema é capaz de realizar criação, consulta, edição e remoção de tarefas, respeitando todos componentes do CRUD.

## Back-End

O presente repositório se trata do back-end do sistema. Trata-se de uma API REST integrada com CORS, desenvolvida em Python com o microframework Flask
Por ser um programa de menor dimensão e escalabilidade, a API é conectada a um banco de dados em SQLite. A API gerencia os dados de cada tarefa (id, título, descrição, status e data da publicação).

## Front-end do projeto

A interface gráfica para a aplicação desenvolvida encontra-se no seguinte repositório: https://github.com/ValmirNogFilho/TasksList

## Dependências

O projeto faz uso das dependências que podem ser consultadas no arquivo 'requirements.txt' do repositório. O arquivo pode ser gerado pelo seguinte comando  no terminal:

`serverenv\Scripts\python.exe serverenv\Scripts\pip.exe freeze > requirements.txt`

## Instalação

Para execução local da API, tendo o Python instalado, entre no diretório do projeto e execute o arquivo `run.py`. O servidor será aberto em `http://127.0.0.1:5050`.
