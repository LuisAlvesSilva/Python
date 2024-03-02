from flask import Flask, render_template, request
import calendar
import datetime
import pytz
import requests
import time

app = Flask(__name__)

API_KEY = "db83ccbd24ab3e0a43d2898582412ab0"

def get_weather(city):
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"
    response = requests.get(link)
    data = response.json()
    description = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15
    return description, temperature

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selecao = request.form['selecao']
        cidade = request.form['cidade']
        if selecao == "calendario":
            tipo_calendario = request.form['tipo_calendario']
            ano = int(request.form['ano'])
            mes = int(request.form['mes'])

            if tipo_calendario == "anual":
                cal = calendar.calendar(ano)
                return render_template('index.html', calendario=cal)
            elif tipo_calendario == "mensal":
                cal = calendar.month(ano, mes)
                return render_template('index.html', calendario=cal)
            else:
                return render_template('index.html', mensagem="Opção Inválida")

        elif selecao == "horas":
            description, temperature = get_weather(cidade)
            fusoHorario = pytz.timezone("America/Sao_Paulo")
            data_hora = datetime.datetime.now(fusoHorario)
            hora_atual = data_hora.strftime("%H:%M:%S")
            return render_template('index.html', cidade=cidade, hora_atual=hora_atual, description=description, temperature=temperature)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
