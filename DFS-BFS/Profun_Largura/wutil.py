import array

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
		if not self.isEmpty():
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
		color = {} #colore os vértices com White, Green ou Blue
		parent = {} # seta os nós pais
		dfs_transversal_output = [] #caminhos de busca --> percorre todo o grafo
		for node in grafo:  # loop para inicialização de nós no grafo
			color[node] = "W"
			parent[node] = None
		lifo = Pilha() #estrutura de dados Last In First Out -> instanciando uma pilha
		estadoInicial = self.pegaEstadoInicial(grafo) #pega o nó raiz
		lifo.push(estadoInicial) #empilha
		u = estadoInicial 
		while not lifo.isEmpty():
			u = lifo.pop() #desempilha e pega o nó para explorar
			proximos = self.pegaProximosEstados(grafo, u)
			color[u] = "G" #Colore o nó visitado.
			if not(u in dfs_transversal_output): 
				dfs_transversal_output.append(u) #empilha nos nós visitados.
			if(u == estadoFinal): #SAINDO DA BUSCA, POIS O ELEMENTO FOI ENCONTRADO
					break		
			
			k = 0 #variável auxiliar para saber se o nó tem vizinhos não visitados ou explorados 
			for v in proximos:
				if color[v] == "W" or color[v] == "G": #verifica se o nó é um nó final
					parent[v] = u
					lifo.push(v) #empilha no fringe
					k+=1
						
			if len(proximos) == 0 or k == 0:	#nó final encontrado
				color[u] = "B" #colore o nó com Blue
			else:
				u = v

			# if(u == estadoFinal): #SAINDO DA BUSCA, POIS O ELEMENTO FOI ENCONTRADO
			# 		break		
			
		print("\nCores: ",color) #imprime as cores dos nós
		print("\n{Nó : Pai do Nó}",parent) #imprime os pares com nós pais e filhos
		print("\nVisitados pelo fringe da pilha: \n",dfs_transversal_output) #imprime os nós visitados e desempilhados do fringe
		path = [] #Caminho até o Estado Final
		filho = estadoFinal 
		path.append(filho) #empilha a solução no caminho
		pai = parent[filho]
		path.append(pai)
		while not(pai==estadoInicial): #empilha todos os nós pais que fazem o caminho até o nó inicial 
			filho = parent[pai] #pega o nó pai de seu respectivo filho
			pai = filho
			path.append(pai) #empilha no caminhos
		print("\nCaminho encontrado foi: ->",path," #DFS# ")	#imprime a solução	
		#Insira o seu codigo aqui!
            


	def buscaEmLargura(self,grafo,estadoFinal):
		"""
		Procura primeiro o nós mais rasos na arvore de busca

		O algoritmo deve retornar o caminho para o estado objetivo
		"""
		#Crie um objeto para a correta estrutura de dados

		fifo = Fila() #estrutura de dados First In First Out - instanciando uma Fila

		visited = {} #demarca os nós visitados 
		level = {} #recebe o nível de cada exploração
		parent = {} #recebe os pais dos nós filhos
		estadoInicial = self.pegaEstadoInicial(grafo)
    
		for node in grafo: #inicializa com os nós do grafo as listas criadas 
			visited[node] = False
			parent[node] = None
			level[node] = -1
		
		bfs_transversal_output = [] #cria uma lista para os nós da busca serem enfileirados
		visited[estadoInicial] = True
		level[estadoInicial] = 0

		fifo.push(estadoInicial) #enfileira o primeiro nó
		while not fifo.isEmpty(): #enquanto a fila do fringe não estiver vazia continue a busca 
			u = fifo.pop() #pega o primeiro da fila
			proximos = self.pegaProximosEstados(grafo,u) #pega os nós vizinhos
			bfs_transversal_output.append(u) #empilha os nós de busca
			if(u == estadoFinal): #SAINDO DA BUSCA, POIS O ELEMENTO FOI ENCONTRADO
				break
			for v in proximos: #loop dos nós vizinhos
				if not visited[v]:
					visited[v] = True
					parent[v] = u #setando o nó pai
					level[v] = level[u] + 1 #encontrado o tamanho do nível de busca
					fifo.push(v) #empilha o nó visitado
		print("\nVisitados pelo fringe da fila: \n",bfs_transversal_output)
		
		path = [] #Caminho até o Estado Final
		filho = estadoFinal 
		path.append(filho) #empilha a solução no caminho
		pai = parent[filho]
		path.append(pai)
		while not(pai==estadoInicial): #empilha todos os nós pais que fazem o caminho até o nó inicial 
			filho = parent[pai] #pega o nó pai de seu respectivo filho
			pai = filho
			path.append(pai) #empilha no caminho
		print("\nCaminho encontrado foi: ->",path," #BFS#")	#imprime a solução	
		
