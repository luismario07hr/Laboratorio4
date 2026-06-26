from flask import Flask, jsonify, request

app = Flask(__name__)

# simular datos 
clientes = {
    "101": {"id": 101, "nombre": "Carlos Melendez", "saldo": 150.50},
    "102": {"id": 102, "nombre": "Glenda Valle", "saldo": 320.00}
}

@app.get("/")
def inicio():
    return jsonify(
        {
            "mensaje": "Bienvenido a la API de clientes",
            "versión": "1.0",
            "endpoints": ["/clientes", "/clientes/<60>"]
        }
    )

@app.get("/clientes")
def obtener_clientes():
    return jsonify(list(clientes.values()))

@app.get("/clientes/<id>")
def obtener_cliente(id):
    cliente = clientes.get(id)
    if cliente:
        return jsonify(cliente)
    return jsonify({"error": "Cliente no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug = True)