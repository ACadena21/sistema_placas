from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulación de base de datos (por ahora)
placas = [
    {"placa": "ABC123", "estado": "robado"},
    {"placa": "XYZ789", "estado": "no robado"}
]

@app.route("/")
def home():
    return "Servidor activo 🚀"

@app.route("/buscar_placa/<placa>", methods=["GET"])
def buscar_placa(placa):
    for p in placas:
        if p["placa"] == placa:
            return jsonify(p)
    return jsonify({"mensaje": "Placa no encontrada"}), 404

if __name__ == "__main__":
    app.run()
