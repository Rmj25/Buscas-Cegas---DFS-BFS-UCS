adj_list = {
	"A":["C",""],
	"B":["E","D"],
	"C":["F","B"],
	"D":[],
	"E":["F"],
	"F":[],
}
color = {}
parent = {}
trav_time = {} 
dfs_transversal_output = []
time = 0;

for node in adj_list.keys():
	color[node] = "W"
	parent[node] = None
	trav_time[node] = [-1,-1]
	

def dfs(u):
	global time
	color[u] = "G"
	dfs_transversal_output.append(u)
	trav_time[u][0] = time
	time+=1
	
    for v in adj_list[u]:
	    if(color[v]=="W"):
		    parent[v] = u
		    dfs(v)
    color[u] = "B"
    trav_time[u][1] = time
    time+=1

for node in adj_list.keys():
	print(node,"->",trav_time[node])


dfs("A")
print(dfs_transversal_output)
	
		