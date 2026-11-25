# API de Chamados de Suporte

**Estudante:** Juan Carlos Oliveira da Costa  
**Curso:** Análise e Desenvolvimento de Sistemas, UFCA  
**Disciplina:** Programação para Web

## Objetivo

Esta API registra chamados de suporte em memória. Ela permite cadastrar um chamado, listar todos e consultar um deles pelo identificador. Os dados somem quando o servidor é reiniciado, o que é esperado nesta etapa. O projeto usa Flask, com as dependências gerenciadas pelo uv.

## Instalação das dependências

Com o uv instalado, rode o comando abaixo na pasta do projeto. Ele cria o ambiente virtual `.venv` e instala exatamente as versões registradas no `uv.lock`.

    uv sync --locked

## Como executar

Inicie o servidor com o comando abaixo. A API passa a responder em `http://localhost:5000`.

    uv run flask --app app run --host=0.0.0.0 --port=5000

## Endpoints

### GET /

Confirma que a API está no ar. Retorna status `200` e o objeto abaixo.

    {"mensagem": "API de chamados em funcionamento"}

### POST /chamados

Cadastra um chamado. O corpo da requisição é um JSON com os campos `titulo`, `descricao`, `solicitante` e `prioridade`. A API gera o `id`, define o `status` como `aberto` e responde com status `201` e o chamado criado.

### GET /chamados

Retorna status `200` e um array com todos os chamados. Sem chamados cadastrados, o array vem vazio.

### GET /chamados/{id}

Retorna status `200` e o chamado com o identificador informado. Quando ele não existe, a resposta é `404` com o objeto abaixo.

    {"mensagem": "Chamado não encontrado"}

## Exemplo de cadastro

Requisição.

    curl -i -X POST http://localhost:5000/chamados \
      -H "Content-Type: application/json" \
      -d '{"titulo": "Impressora sem conexão", "descricao": "A impressora do laboratório não aparece na rede.", "solicitante": "Ana", "prioridade": "media"}'

Resposta com status `201`.

    {
      "id": 1,
      "titulo": "Impressora sem conexão",
      "descricao": "A impressora do laboratório não aparece na rede.",
      "solicitante": "Ana",
      "prioridade": "media",
      "status": "aberto"
    }