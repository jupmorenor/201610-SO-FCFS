'''
Created on 5/04/2016
@author: Juan Pablo Moreno - 20111020059
'''
from random import randint

class Proceso(object):
	
	def __init__(self, nom, ll):
		self.nombre = nom
		self.rafaga = randint(2, 15)
		self.llegada = ll
		self.comienzo = None
		self.finalizacion = 0
		self.estado = "listo"
		self.actualizado = False
		
	def iniciar(self, com):
		self.estado = "ejecutando"
		if self.comienzo == None:
			self.comienzo = com
		
	def finalizar(self, fin):
		self.estado = "terminado"
		self.finalizacion = fin
	
	def bloquear(self):
		self.estado = "bloqueado"
	
	def alistar(self):
		self.estado = "listo"
	
	def ejecutar(self):
		self.rafaga -= 1
			
	def listo(self):
		return self.estado == "listo"
	
	def bloqueado(self):
		return self.estado == "bloqueado"
	
	def terminado(self):
		return self.estado == "terminado"
	
	def ejecutando(self):
		return self.estado == "ejecutando"


class ProcesoPriorizable(Proceso):
	
	def __init__(self, nom, ll):
		super(ProcesoPriorizable, self).__init__(nom, ll)
		self.prioridad = randint(1,4)
		self.edad = randint(15, 20)
	
	def envejecer(self):
		self.edad -= 1
		
	def priorizar(self):
		self.prioridad -= 1
		if self.prioridad > 1:
			self.edad = randint(20, 25)

class ProcesoPriorizableMulticolas(ProcesoPriorizable):
	
	def __init__(self, nom, ll):
		super(ProcesoPriorizableMulticolas, self).__init__(nom, ll)
		self.prioridad = 1
		self.edad = 0
	
	def priorizar(self):
		self.prioridad -= 1
		if self.prioridad > 1:
			self.edad = randint(10, 30)
	
	def degradar(self):
		self.prioridad += 1
		self.edad = randint(10, 30)

		