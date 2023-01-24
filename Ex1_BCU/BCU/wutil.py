import array
import numpy as np
import heapq
import random
import sys

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

class FilaPriorizada:
	"""
	Implementa uma estrutura de dados de fila de prioridade. Cada item inserido possui uma prioridade. 
	"""
	def __init__(self):
		self.heap=[]
		self.contador = 0

	def push(self,item,prioridade):
		entrada = (prioridade,self.contador,item)
		heapq.heappush(self.heap,entrada)
		self.contador += 1
		
	def pop(self):
		"Le e remove o menor elemento"
		(_,_,item) = heapq.heappop(self.heap)
		return item
		
	def isEmpty(self):
		return len(self.heap) == 0

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
		buff = grafo.get(atual)
		estadosFilhosLista = []
		for estadosFilhos in buff.keys():
			estadosFilhosLista.append(estadosFilhos)
		return estadosFilhosLista

	def pegaCustoProximosEstados(self,grafo,atual):
		"""
		Retorna os custos para alcançar o nós filhos
		"""
		buff = grafo.get(atual)
		custosLista = []
		for custoFilho in buff.values():
			custosLista.append(custoFilho)
		return custosLista
		

	def buscaEmProfundidade(self,grafo,estadoFinal):
		"""
		Procura primeiro os nós mais profundos na árvore de busca

		O algoritmo deve retornar o caminho para o estado objetivo
		"""

		
	def buscaEmLargura(self,grafo,estadoFinal):
		"""
		Procura primeiro o nós mais rasos na arvore de busca

		O algoritmo deve retornar o caminho para o estado objetivo
		"""
		

	def buscaCustoUniforme(self,grafo,estadoFinal):
		"""
		Procura primeiro o nó de menor custo total

		O algoritmo deve retornar o caminho para o estado objetivo
		"""
		
		#Crie um objeto para a correta estrutura de dados
		estadoInicial = self.pegaEstadoInicial(grafo)
		filapri = FilaPriorizada()
		filapri.push([estadoInicial],0)
		c_total = {}
		c_total[estadoInicial] = 0
		while(not filapri.isEmpty()):
			caminho = filapri.pop()
			u = caminho[-1]
			if u == estadoFinal:
				break
			
			proximos = self.pegaProximosEstados(grafo,u)
			custos = self.pegaCustoProximosEstados(grafo,u)
			for elem,c in zip(proximos,custos):
				c_total[elem] = c + c_total[u]
				filapri.push(caminho+[elem],c_total[elem])
		return caminho
		#Insira o seu codigo aqui!
