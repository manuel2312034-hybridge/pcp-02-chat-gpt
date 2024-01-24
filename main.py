from flask import Flask, request

app = Flask(__name__)

@app.route('/healthcheck')
def hola_mundo():
    return {"message": 'ok'}

@app.route('/prompt', methods=['POST'])
def obtenerDatos():
    input_json = request.get_json(force=True)
    return input_json

if __name__ == '__main__':
    app.run(debug=True, port=5050)

