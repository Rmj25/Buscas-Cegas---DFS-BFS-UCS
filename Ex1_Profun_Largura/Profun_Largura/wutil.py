import array
import numpy as np

class Fila:
	"""
	Funções para usar um estrutura de dados tipo FIFO
	"""
	def __init__(self):
		self.list =[]

	def push(self,item):
		#Coloca o 'item' na fila
		self.list.insert(0,item)

	def pop(self):
		#Le e remove o primeiro item colocado ainda na fila.
		return self.list.pop()
	
	def isEmpty(self):
		#Retorna verdadeiro se a fila está vazia
		return len(self.list) == 0

class Pilha:
	"""
	Funções para usar uma estrutura de dados tipo LIFO
	"""
	def __init__(self):
		self.list = []
	
	def push(self,item):
		"Coloco o 'item' na pilha"
		self.list.append(item)

	def pop(self):
		"Le e remove o elemento no topo da pilha"
		return self.list.pop()

	def isEmpty(self):
		"Retorna verdadeiro se a pilha está vazia"
		return len(self.list) == 0

class ProblemaBusca:

	def pegaEstadoInicial(self,grafo):
		"""
		Retorna o estado inicial do problema de busca
		"""
		estados = list(grafo.keys())
		estadoInicial = estados[0]
			
		return estadoInicial


	def pegaProximosEstados(self,grafo,atual):
		"""
		Retorna os nós filhos do estado atual
		"""
		return grafo.get(atual)

	def buscaEmProfundidade(self,grafo,estadoFinal):
		"""
		Procura primeiro os nós mais profundos na árvore de busca

		O algoritmo deve retornar o caminho para o estado objetivo
		"""

		#Crie um objeto para a correta estrutura de dados
		pilha = Pilha()
		estadoInicial = self.pegaEstadoInicial(grafo)
		pilha.push([estadoInicial])
		while (not pilha.isEmpty()):
			caminhoPilha = pilha.pop()
			estado = caminhoPilha[-1] #pega o último elemento
			if estado == estadoFinal:
				break

			proximos = self.pegaProximosEstados(grafo,estado)
			for elementos in proximos:
				pilha.push(caminhoPilha+[elementos])
		return caminhoPilha

	def buscaEmLargura(self,grafo,estadoFinal):
		"""
		Procura primeiro o nós mais rasos na arvore de busca

		O algoritmo deve retornar o caminho para o estado objetivo
		"""

		fila = Fila()
		estadoInicial = self.pegaEstadoInicial(grafo)
		fila.push([estadoInicial])
		while (not fila.isEmpty()):
			caminhoFila = fila.pop()
			estado = caminhoFila[-1] #pega o último elemento
			if estado == estadoFinal:
				break

			proximos = self.pegaProximosEstados(grafo,estado)
			proximos = proximos[-1::-1]
			for elementos in proximos:
				fila.push(caminhoFila+[elementos])
		return caminhoFila

