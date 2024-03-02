import requests as rq

url = 'https://viacep.com.br/ws/'
cep = input("Digite o CEP desejado: ")
format = '/json/'

r = rq.get(url + cep + format)

if r.status_code == 200:
    data = r.json()
    print(data)
else:
    print('Erro na requisição. Status Code:', r.status_code)
