from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# DATOS DE TU BASE DE DATOS (CAMBIA ESTO)
DB_HOST = "dpg-d66i6ma4d50c738sfe50-a"
DB_NAME = "sistema_placas"
DB_USER = "sistema_placas_user"
DB_PASSWORD = "EAyyreoArG8VG7a6aTUxsf7SGuSCVgbh"
DB_PORT = "5432"

def conectar_bd():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

@app.route("/")
def home():
    return "Servidor activo 🚀"

@app.route("/consultar", methods=["GET"])
def consultar_placa():
    placa = request.args.get("placa")

    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute("SELECT estado FROM vehiculos WHERE placa = %s", (placa,))
    resultado = cursor.fetchone()

    cursor.close()
    conn.close()

    if resultado:
        return jsonify({"placa": placa, "estado": resultado[0]})
    else:
        return jsonify({"placa": placa, "estado": "no registrada"})

if __name__ == "__main__":
    app.run()
