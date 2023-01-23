"""
Primeiro trabalho da disciplina IA aplicada a automacao
O aluno devera: 
	1 - Usar a funcao EspacoEstado para "ler" o problema
	2 - Instanciar a classe ProblemaBusca     

"""
from wutil import ProblemaBusca

# def EspacoEstado():
# 	graph = {
# 		1:{5:5,3:3,2:2},
# 		2:{4:4},
# 		3:{5:4},
# 		4:{6:2,5:1},
# 		5:{6:5},
# 		6:{}
# 	}
# 	return graph

# def EspacoEstado():
# 	graph = {
# 		"s":{"A":2,"B":3,"D":5},
# 		"A":{"C":4},
# 		"B":{"D":4},
# 		"C":{"g":2,"D":1},
# 		"D":{"g":5},
# 		"g":{}
# 	}
# 	return graph
	  
def EspacoEstado():
	graph = {
		"s":{"D":3,"E":9,"P":1},
		"A":{},
		"B":{"A":2},
		"C":{"A":2},
		"D":{"B":1,"C":8,"E":2},
		"E":{"H":8,"R":2},
		"F":{"C":3,"g":2},
		"g":{},
		"H":{"P":4,"Q":4},

		"P":{"Q":15},
		"Q":{},
		"R":{"F":2}
	}
	return graph

def main():
	grafo = EspacoEstado()
	algoritmo = ProblemaBusca()
	estadoFinal = "g"

	
	#Insira o seu codigo aqui
	algoritmo.buscaCustoUniforme(grafo,estadoFinal)


if __name__ == '__main__':
	main()
