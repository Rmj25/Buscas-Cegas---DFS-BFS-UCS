graph = {
	"s":{"A":2,"B":3,"D":5},
	"A":{"C":4},
 	"B":{"D":4},
 	"C":{"g":2,"D":1},
 	"D":{"g":5},
 	"g":{}
}
def path_cost(path):
    total_cost = 0
    for (node,cost) in path:
        total_cost += cost
    return total_cost,path[-1][0]
pa = [("s",0),("D",5),("g",5)]
print(path_cost(pa))

def UCS(graph, start, goal):
    visited = []
    queue = [[(start,0)]]
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2,cost))
                queue.append(new_path)
solution = UCS(graph,"s","g")
print("Solução é: ",solution)
print("Custo da solução:", path_cost(solution)[0])