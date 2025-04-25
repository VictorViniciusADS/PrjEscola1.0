from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    """
    Example endpoint returning a greeting message.
    ---
    responses:
      200:
        description: A successful response
        examples:
          application/json: {"message": "Hello, World!"}
    """
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)




# filepath: c:\Users\victo\OneDrive\Desktop\PrjEscola\app\app.py
from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)

# Configuração do template OpenAPI
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API da Escola",
        "description": "Documentação da API da Escola usando Flasgger",
        "version": "1.0.0"
    },
    "host": "localhost:5000",  # Atualize conforme necessário
    "basePath": "/",
    "schemes": ["http"],
}

# Inicializar o Swagger com o template
swagger = Swagger(app, template=swagger_template)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    """
    Example endpoint returning a greeting message.
    ---
    responses:
      200:
        description: A successful response
        examples:
          application/json: {"message": "Hello, World!"}
    """
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)