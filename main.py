"""
API  - APlication Programing Interface!
 comunicação entre 2 servidores! - API
 calculo de Frete
 Trasações de cartão de crédito
 app para celulares!  Front-end ->  todas as requisições, são via json - API

API Suporta Varios formatos de arquivo, o pricipais são

1 - JSON
2 - XML
3 - YML

{} - um ojbeto
[] - um array

Exemplo ver arquivo pessoa.js
"""
import json
import requests 
from json.decoder import JSONDecoder
from json.encoder import JSONEncoder

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
response = requests.get("https://brasilapi.com.br/api/banks/v1")

lista = []
if response.status_code == 200:
  response = json.loads(response.content)
  for line in response:
    lista.append(line['name'].title())
else: 
  print(response.status_code)
listabancosord = bubbleSort(lista)
for banco in listabancosord:
  print(banco)

#with open('bancos.txt','w') as arquivo:
  #for valor in listabancosord:
    #arquivo.write(str(valor) + '\n')



"""Exercícios!

1 - Continuem o programa acima adicionando as seguintes funções:
  A -> rodenar a lista de Bancos em ordem alfabetica usando o booble sorte
  B -> Gravar a lista de Banco em um arquivo TXT
"""