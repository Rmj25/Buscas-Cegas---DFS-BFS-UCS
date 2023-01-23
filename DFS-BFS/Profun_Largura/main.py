"""
Primeiro trabalho da disciplina IA aplicada a automacao
O aluno devera: 
	1 - Usar a funcao EspacoEstado para "ler" o problema
	2 - Instanciar a classe ProblemaBusca     

"""

from wutil import ProblemaBusca

# def EspacoEstado():
# 	graph = {
# 		1:[2,3,5],
# 		2:[4],
# 		3:[5],
# 		4:[5,6],
# 		5:[6],
# 		6:[]
		
# 	}
# 	return graph


# def EspacoEstado():
# 	graph = {
# 		"A":["C","B"],
# 		"B":["E","D"],
# 		"C":["F","B"],
# 		"D":[],
# 		"E":["F"],
# 		"F":[],
		
# 	}
#  	return graph
# def EspacoEstado():
# 	graph = {
# 		"A":["B","D"],
# 		"B":["A","C"],
# 		"C":["D"],
# 		"D":["A","E","F"],
# 		"E":["D","F","G"],
# 		"F":["B","D"],
# 		"G":["E","H"],
# 		"H":["G","F"],
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

  
# def EspacoEstado():
# 	graph = {
# 		"s":{"D","E","P"},
# 		"A":{},
# 		"B":{"A"},
# 		"C":{"A"},
# 		"D":{"B","C","E"},
# 		"E":{"H","R"},
# 		"F":{"C","g"},
# 		"g":{},
# 		"H":{"P","Q"},

# 		"P":{"Q"},
# 		"Q":{},
# 		"R":{"F"},
		
# 	}
# 	return graph


def EspacoEstado():
	graph = {
		"s":{"A","B","D"},
		"A":{"C","D"},
 		"B":{"D"},
 		"C":{"g","D"},
 		"D":{"g"},
 		"g":{}
	}
	return graph


def main():
	grafo = EspacoEstado()
	algoritmo = ProblemaBusca()
	estadoFinal = "g"

	#Insira o seu código aqui!
	
	algoritmo.buscaEmProfundidade(grafo,estadoFinal)
	algoritmo.buscaEmLargura(grafo,estadoFinal)

if __name__ == '__main__':
	main()
