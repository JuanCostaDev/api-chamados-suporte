# API de Chamados de Suporte

**Estudante:** Juan Carlos Oliveira da Costa  
**Curso:** Análise e Desenvolvimento de Sistemas, UFCA  
**Disciplina:** Programação para Web

## Objetivo

Este projeto é a base de uma API de chamados de suporte feita com Flask, com ambiente e dependências gerenciados pelo uv. Por enquanto existe só a rota inicial, que confirma que a API está no ar. O cadastro de chamados e o banco de dados ficam para as próximas atividades.

## Instalação das dependências

Com o uv instalado, rode o comando abaixo na pasta do projeto. Ele cria o ambiente virtual `.venv` e instala exatamente as versões registradas no `uv.lock`.

    uv sync --locked

## Como executar

Inicie o servidor com o comando abaixo. A API passa a responder na porta 5000.

    uv run flask --app app run --host=0.0.0.0 --port=5000

## Como acessar a rota inicial

Com o servidor rodando, abra `http://localhost:5000/` no navegador ou use o curl no terminal.

    curl -i http://localhost:5000/

A resposta vem com status `200`, cabeçalho `Content-Type` igual a `application/json` e este corpo.

    {
      "mensagem": "API de chamados em funcionamento"
    }