import requests as rq
url = 'https://viacep.com.br/ws/'
cep = input("Digite o CEP desejado: ")
format = '/json/'
r = rq.get( url + cep + format)
if (r.status_code == 200)
  print(/n'JSON' , r.json()/n)

else:
 print(' Nao encontrado')