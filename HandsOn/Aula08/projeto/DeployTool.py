#!usr/bin/python 
# -*- coding: utf-8 -*-
from Modulos.DockerModulo import DockerModulo
from Modulos.SSHModulo import SSHModulo
import json

if __name__ == "__main__":
	try:
		with open("deployment.json","r") as f:
			job_json = json.loads(f.read())


		docker = DockerModulo()
		# container = docker.createContainer(job_json["name"])
		# docker.startContainer(container)

		ssh = SSHModulo()

		for c in job_json["commands"]:
			command = "docker exec %s %s" % (job_json["name"], c)
			ssh.execCommand(c)

		print "Deploy Finalizado com sucesso!"
	except Exception as e:
		print e