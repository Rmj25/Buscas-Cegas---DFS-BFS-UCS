import array
import heapq
import random
import sys

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
		estadosFilhosLista =[]
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
		
	def buscaCustoUniforme(self,grafo,estadoFinal):
		"""
		Procura primeiro o nó de menor custo total

		O algoritmo deve retornar o caminho para o estado objetivo
		"""
		
		#Crie um objeto para a correta estrutura de dados
		fifo = FilaPriorizada() #estrutura de dados First In First Out - instanciando uma Fila
		visited = {} #demarca os nós visitados 
		parent = {} #recebe os pais dos nós filhos
		custo_caminho = {}#recebe os custos
		estadoInicial = self.pegaEstadoInicial(grafo)
    
		for node in grafo: #inicializa com os nós do grafo as listas criadas 
			visited[node] = False
			parent[node] = None
			
		custo_caminho = {estadoInicial:0}
		ucs_transversal_output = [] #cria uma lista para os nós da busca serem enfileirados
		u = estadoInicial
		visited[estadoInicial] = True
			
		fifo.push(estadoInicial,custo_caminho) #enfileira o primeiro nó
		while not fifo.isEmpty(): #enquanto a fila do fringe não estiver vazia continue a busca 
			u = fifo.pop()#pega o primeiro da fila
			print(custo_caminho)
			proximos = self.pegaProximosEstados(grafo,u) #pega os nós vizinhos
			p_custos = self.pegaCustoProximosEstados(grafo,u)
			ucs_transversal_output.append(u) #empilha os nós de busca
			if(u==estadoFinal):
				break
			print(ucs_transversal_output)
			print(proximos,p_custos)
			for c,v in zip(p_custos,proximos):  #loop dos nós vizinhos
				if not visited[v]:
					visited[v] = True
					if v in ucs_transversal_output:
						if(custo_caminho[v]>=c+custo_caminho[u]):
							custo_caminho.update({v :c + custo_caminho[u]})
							parent[v] = u
						else:
							custo_caminho.update({v:custo_caminho[v]})
					else:
						custo_caminho.update({v :c + custo_caminho[u]})
						parent[v] = u #setando o nó pai
					fifo.push(v,custo_caminho[v])#empilha o nó visitado
				else:
						if(custo_caminho[v]>=c+custo_caminho[u]):
							custo_caminho.update({v :c + custo_caminho[u]})
							parent[v] = u
						else:
							custo_caminho.update({v:custo_caminho[v]})
						fifo.push(v,custo_caminho[v])#empilha o nó visitado
		print("\nVisitados pelo fringe da fila de prioridade: \n",ucs_transversal_output)
		
		path = [] #Caminho até o Estado Final
		filho = estadoFinal 
		path.append(filho) #empilha a solução no caminho
		pai = parent[filho]
		path.append(pai)
		while not(pai==estadoInicial): #empilha todos os nós pais que fazem o caminho até o nó inicial 
			filho = parent[pai] #pega o nó pai de seu respectivo filho
			pai = filho
			path.append(pai) #empilha no caminho
		print("\nCaminho encontrado foi: ->",path," #UCS#")	#imprime a solução	
		#Insira o seu codigo aqui!
