#!usr/bin/python 
# -*- coding: utf-8 -*-

import requests
import json

url = 'http://localhost:5000/usuarios/'

nome = "Rafael Medeiros"
email = "rafael.medeiros@dexter.com.br"

resultados = json.loads(requests.get(url).text)

for u in resultados["usuarios"]:
	if u['email'] == email:
		print "Usuario ja cadastrado"
		exit(1)


data = json.dumps({"nome":nome,"email":email})
headers = {"Content-Type":"application/json"}
print requests.post(url, data=data,headers=headers).text