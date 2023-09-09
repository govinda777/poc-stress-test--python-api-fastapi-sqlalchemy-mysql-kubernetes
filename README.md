# POC Stress Test: Python API com FastAPI, SQLAlchemy, MySQL e Kubernetes

Uma Prova de Conceito (POC) para avaliar a resistência e desempenho de uma pilha tecnológica específica sob condições de carga elevada.

![GitHub stars](https://img.shields.io/github/stars/govinda777/poc-stress-test--python-api-fastapi-sqlalchemy-mysql-kubernetes)
![GitHub forks](https://img.shields.io/github/forks/govinda777/poc-stress-test--python-api-fastapi-sqlalchemy-mysql-kubernetes)

## Descrição

Uma Prova de Conceito (POC) para avaliar a resistência e desempenho de uma pilha tecnológica específica sob condições de carga elevada.

## Pilha Tecnológica

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework moderno e rápido para construir APIs com Python.
- **SQLAlchemy**: Biblioteca ORM para interação com bancos de dados.
- **MySQL**: Sistema de gerenciamento de banco de dados relacional.
- **Kubernetes**: Plataforma de orquestração de contêineres.

## Estrutura do Projeto

- `/src`: Diretório contendo o código-fonte do projeto.

## Como Executar

*Instruções sobre como configurar e executar o projeto devem ser adicionadas aqui.*

## Contribuições

Sinta-se à vontade para contribuir com o projeto! Abra uma issue ou envie um Pull Request.


## Atalhos

* Listar os serviços

kubectl get services

* Listar os pods

kubectl get pods

* Mostra os detalhes do pod

kubectl describe pod mysql-deployment-79b7d97df4-8r2lq

* Mostra os logs dos pods

kubectl logs mysql-deployment-79b7d97df4-8r2lq

Peço desculpas pela confusão anterior. Vou fornecer uma descrição detalhada com base na estrutura atual do seu repositório:

---

# Arquitetura do Projeto

Uma visão geral da estrutura do projeto e uma breve descrição de cada diretório e arquivo:

```
/src
|-- main.py  # Ponto de entrada da aplicação. Configura e inicializa a API FastAPI.

|-- /infrastructure  # Diretório que contém configurações e inicializações relacionadas à infraestrutura, como banco de dados.
|   |-- database.py  # Configuração e inicialização da base de dados.

|-- /user  # Lógica e entidades relacionadas ao domínio do usuário.
|   |-- /exception  # Diretório para tratar exceções específicas do domínio do usuário.
|   
|   |-- /model  # Define os modelos e esquemas relacionados ao domínio do usuário.
|   |   |-- /request  # Esquemas para validação de dados de entrada nas rotas do usuário.
|   |   |   |-- user_create_request.py  # Esquema para validar dados de entrada ao criar um novo usuário.
|   |   |-- /response  # Esquemas para formatar a resposta das rotas do usuário.
|   |   |-- user_mapper.py  # Funções para mapear entre entidades e esquemas.
|   |   |-- user.py  # Define a entidade do usuário.
|   
|   |-- user_controller.py  # Define as rotas e controladores relacionados ao domínio do usuário.
|   |-- user_repository.py  # Define o repositório do usuário, responsável por interagir com o banco de dados.
|   |-- user_service.py  # Define os serviços relacionados ao usuário, que contêm a lógica de negócios.
```

---
