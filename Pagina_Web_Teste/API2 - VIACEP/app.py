from flask import Flask, render_template, jsonify, request
import requests as rq

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_cep', methods=['POST'])
def buscar_cep():
    cep = request.form.get('cep')
    formato = '/json/'
    url = 'https://viacep.com.br/ws/'
    response = rq.get(url + cep + formato)

    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            return jsonify(data)
        else:
            return jsonify({'erro': 'CEP não encontrado'})
    else:
        return jsonify({'erro': 'Erro na requisição. Status Code: {}'.format(response.status_code)})

if __name__ == '__main__':
    app.run(debug=True)
