from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [{"id": 1, "nome": "Bow-Z", "email": "bowz@email.com"}]

@app.route('/')
def home():
    return jsonify({"mensagem": "API do Bow-Z online 😎"}), 200

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    novo_usuario = request.json
    novo_usuario["id"] = len(usuarios) + 1
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    for user in usuarios:
        if user["id"] == id:
            user.update(request.json)
            return jsonify(user), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    for user in usuarios:
        if user["id"] == id:
            usuarios.remove(user)
            return jsonify({"mensagem": "Usuário deletado"}), 200
    return jsonify({"erro": "Usuário não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
