# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from gerar_resposta import gerar_resposta

app = Flask(__name__)
CORS(app)  # Permite acesso do React Native

@app.route("/api/perguntar", methods=["POST"])
def perguntar():
    data = request.get_json()
    mensagem = data.get("mensagem", "")
    resposta = gerar_resposta(mensagem)
    return jsonify({"resposta": resposta})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
