"""
Primeiro trabalho da disciplina IA aplicada a automacao
O aluno devera: 
	1 - Usar a funcao EspacoEstado para "ler" o problema
	2 - Instanciar a classe ProblemaBusca     

"""

from wutil import ProblemaBusca

# def EspacoEstado():
# 	graph = {
# 		1:[5,3,2],
# 		2:[4],
# 		3:[5],
# 		4:[6,5],
# 		5:[6],
# 		6:[]
# 	}
# 	return graph
# def EspacoEstado():
# 	graph = {
# 		"s":["D","B","A"],
# 		"A":["C"],
# 		"B":["D"],
# 		"C":["g","D"],
# 		"D":["g"],
# 		"g":[]
# 	}
# 	return graph

# def EspacoEstado():
# 	graph = {
# 		1:[10,6,5],
# 		2:[],
# 		3:[2],
# 		4:[2],
# 		5:[6,4,3],
# 		6:[12,9],
# 		7:[8,4],
# 		8:[],
# 		9:[11,10],
# 		10:[11],
# 		11:[],
# 		12:[7]
# 	}
# 	return graph

def EspacoEstado():
	graph = {
		"s":["P","E","D"],
		"A":[],
		"B":["A"],
		"C":["A"],
		"D":["E","C","B"],
		"E":["R","H"],
		"F":["g","C"],
		"g":[],
		"H":["Q","P"],

		"P":["Q"],
		"Q":[],
		"R":["F"]
	}
	return graph
def main():
	grafo = EspacoEstado()
	algoritmo = ProblemaBusca()
	estadoFinal = 'g'
	
	solucao1 = algoritmo.buscaEmProfundidade(grafo,estadoFinal)
	solucao2 = algoritmo.buscaEmLargura(grafo,estadoFinal)

	print("DFS->",solucao1,"\nBFS->",solucao2)
	
	#Insira o seu código aqui!

if __name__ == '__main__':
	main()
