from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.ensure_ascii = False

chamados = []
proximo_id = 1


@app.get("/")
def inicio():
    return jsonify({"mensagem": "API de chamados em funcionamento"})


@app.post("/chamados")
def cadastrar_chamado():
    global proximo_id
    dados = request.get_json()
    chamado = {
        "id": proximo_id,
        "titulo": dados["titulo"],
        "descricao": dados["descricao"],
        "solicitante": dados["solicitante"],
        "prioridade": dados["prioridade"],
        "status": "aberto",
    }
    chamados.append(chamado)
    proximo_id += 1
    return jsonify(chamado), 201


@app.get("/chamados")
def listar_chamados():
    return jsonify(chamados)


@app.get("/chamados/<int:id_chamado>")
def consultar_chamado(id_chamado):
    for chamado in chamados:
        if chamado["id"] == id_chamado:
            return jsonify(chamado)
    return jsonify({"mensagem": "Chamado não encontrado"}), 404