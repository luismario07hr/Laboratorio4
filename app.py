from flask import Flask, jsonify, request

app = Flask(__name__)

productos = {
    101: {"id": 101, "nombre": "Teclado Mecánico RGB", "precio": 45.00, "stock": 15},
    102: {"id": 102, "nombre": "Monitor Gamer 24''", "precio": 189.99, "stock": 8}
}

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a la API de Catálogo de Productos",
        "version": "1.0",
        "endpoints": [
            "GET /productos", 
            "GET /productos/<id>", 
            "POST /productos", 
            "PUT /productos/<id>", 
            "DELETE /productos/<id>"
        ]
    })
    
@app.get("/productos")
def obtener_productos():
    return jsonify(list(productos.values()))

@app.get("/productos/<int:id>")
def obtener_producto(id):
    producto = productos.get(id)
    if producto:
        return jsonify(producto)
    return jsonify({"error": "Producto no encontrado"}), 404

@app.post("/productos")
def agregar_producto():
    nuevo_producto = request.get_json()
    
    if not nuevo_producto or "nombre" not in nuevo_producto or "precio" not in nuevo_producto or "stock" not in nuevo_producto:
        return jsonify({"error": "Los campos 'nombre', 'precio' y 'stock' son obligatorios"}), 400
    
    if not isinstance(nuevo_producto["precio"], (int, float)) or not isinstance(nuevo_producto["stock"], int):
        return jsonify({"error": "El 'precio' debe ser un número y el 'stock' debe ser un número entero"}), 400
    
    id_producto = max(productos.keys(), default=100) + 1
    
    producto_creado = {
        "id": id_producto,
        "nombre": nuevo_producto["nombre"],
        "precio": float(nuevo_producto["precio"]),
        "stock": int(nuevo_producto["stock"])
    }
    
    productos[id_producto] = producto_creado
    return jsonify(producto_creado), 201

@app.put("/productos/<int:id>")
def actualizar_producto(id):
    producto = productos.get(id)
    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404
        
    datos_actualizados = request.get_json()
    if not datos_actualizados:
        return jsonify({"error": "Se requieren datos para actualizar"}), 400
        
    if "nombre" in datos_actualizados:
        producto["nombre"] = datos_actualizados["nombre"]
    
    if "precio" in datos_actualizados:
        if not isinstance(datos_actualizados["precio"], (int, float)):
            return jsonify({"error": "El precio debe ser un valor numérico"}), 400
        producto["precio"] = float(datos_actualizados["precio"])
        
    if "stock" in datos_actualizados:
        if not isinstance(datos_actualizados["stock"], int):
            return jsonify({"error": "El stock debe ser un valor entero"}), 400
        producto["stock"] = int(datos_actualizados["stock"])
        
    return jsonify(producto), 200

@app.delete("/productos/<int:id>")
def eliminar_producto(id):
    if id in productos:
        del productos[id]
        return jsonify({"mensaje": f"Producto {id} eliminado correctamente del catálogo"}), 200
        
    return jsonify({"error": "Producto no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
