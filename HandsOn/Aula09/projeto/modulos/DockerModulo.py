#!usr/bin/python 
# -*- coding: utf-8 -*-
from docker import Client

cli = Client(base_url="http://192.168.0.2:2376", version="auto")


class DockerModulo:
	def __init__(self):
		try:
			self.cli = Client(base_url="http://192.168.0.2:2376", version="auto")
		except Exception as e:
			raise Exception(e)


	def getContainers(self,todos=True):
		try:
			return [c for c in self.cli.containers(all=todos) ] 
		except Exception as e:
			raise Exception(e)

	def startContainer(self,id):
		return self.cli.start(container=id)

	def stopContainer(self,id):
		return self.cli.stop(container=id)


	def removeContainer(self,id):
		self.cli.stop(container=id)
		return self.cli.remove_container(id)

	def createContainer(self,nome,hn,img):
		try:
			container = self.cli.create_container(name=nome,hostname=hn,
				image=img,detach=True, stdin_open=True,tty=True)
			self.cli.start(container=container.get("Id"))
			return container
		except Exception as e:
			raise Exception(e)

	def inspectContainer(self,container_id):
		try:
			container = self.cli.inspect_container(container_id)
			return container
		except Exception as e:
			raise Exception(e)






if __name__ == "__main__":

	try:
		manager = DocketManager()

		for c in manager.getContainers():
			print c
	except Exception as e:
		print "Falhou: %s" % e


