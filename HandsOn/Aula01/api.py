#!usr/bin/python 
# -*- coding: utf-8 -*-

import requests
import json

########  CONSULTA ###########
url = 'http://localhost:5000/usuarios/3/'

resultado = json.loads(requests.get (url).text)
print resultado

for key, value in resultado.iteritems():
	print key, value

########  INCLUIR ###########
# url = "http://localhost:5000/usuarios/"
# data = json.dumps ({"nome":"everton", "email":"negramones@gmail.com"})
# headers = {"Content-Type":"application/json"}
# print requests.post(url, data=data,headers=headers).text

########  ATUALIZAR ###########
# url = "http://localhost:5000/usuarios/7/"
# data = json.dumps ({"nome":"everton j. da silva", "email":"negramones@gmail.com"})
# headers = {"Content-Type":"application/json"}

# print requests.put(url, data=data,headers=headers).text

########  DELETAR ###########

# url = "http://localhost:5000/usuarios/7/"
# headers = {"Content-Type":"application/json"}

# print requests.delete(url).text
