from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from gpt3 import generate_response

app = Flask(__name__)


@app.route("/product", methods=['POST'])
def index():
    try:
        original = request.json['voice']
        print(original)
        generated = generate_response(original)
        return jsonify({
            'mensaje': 'registro exitoso',
            # 'generated': generated,
            'original': original,

            "Nombre": generated[0],
            "Marca": generated[1],
            "Supermercado": generated[2],
            "Departamento": generated[3],
            "Cantidad": generated[4],
            "Unidad": generated[5],
            "Precio": generated[6],
            "Anotaciones": generated[7]
        })
    except:
        return jsonify({'mensaje': 'registro fallido'})


def not_found(error):
    return "404 not founf"


if __name__ == "__main__":
    app.register_error_handler(404, not_found)
    app.run(debug=True, port="4000", host="localhost")
