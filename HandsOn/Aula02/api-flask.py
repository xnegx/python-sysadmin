#!usr/bin/python 
# -*- coding: utf-8 -*-

from flask import Flask
import json
from usuarios_blueprint import usuarios
from funcionarios_blueprint import funcionarios
from grupos_blueprint import grupos

app = Flask(__name__)
app.register_blueprint(usuarios)
app.register_blueprint(funcionarios)
app.register_blueprint(grupos)


@app.route("/")
def hello():
	return "Hello World!"


if __name__ == "__main__":
	# app.run() - modo normal
	app.run(debug=True)