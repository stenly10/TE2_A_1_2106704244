import operator
import time, tracemalloc
from generate_tree import get_graph_bnb, get_graph_bnb_testing

# Implementasi B&B, referensi: https://github.com/sangyh/minimum-vertex-cover/blob/master/BnB_Edited.py

def BnB(G):
	OptVC = []
	CurVC = []
	Frontier = []
	neighbor = []

	UpperBound = G.number_of_nodes()

	CurG = G.copy()
	v = find_maxdeg(CurG)

	Frontier.append((v[0], 0, (-1, -1)))
	Frontier.append((v[0], 1, (-1, -1)))

	while Frontier!=[]:
		(vi,state,parent)=Frontier.pop()
		backtrack = False

		if state == 0:
			neighbor = CurG.neighbors(vi)
			for node in list(neighbor):
				CurVC.append((node, 1))
				CurG.remove_node(node)
		elif state == 1:
			CurG.remove_node(vi)
		else:
			pass

		CurVC.append((vi, state))
		CurVC_size = VC_Size(CurVC)

		if CurG.number_of_edges() == 0:
			if CurVC_size < UpperBound:
				OptVC = CurVC.copy()
				UpperBound = CurVC_size
			backtrack = True
				
		else:
			CurLB = Lowerbound(CurG) + CurVC_size

			if CurLB < UpperBound:
				vj = find_maxdeg(CurG)
				Frontier.append((vj[0], 0, (vi, state)))
				Frontier.append((vj[0], 1, (vi, state)))
			else:
				backtrack=True


		if backtrack==True:
			if Frontier != []:
				nextnode_parent = Frontier[-1][2]

				if nextnode_parent in CurVC:
					
					id = CurVC.index(nextnode_parent) + 1
					while id < len(CurVC):
						mynode, mystate = CurVC.pop()
						CurG.add_node(mynode)
						
						curVC_nodes = list(map(lambda t:t[0], CurVC))
						for nd in G.neighbors(mynode):
							if (nd in CurG.nodes()) and (nd not in curVC_nodes):
								CurG.add_edge(nd, mynode)

				elif nextnode_parent == (-1, -1):
					CurVC.clear()
					CurG = G.copy()
				else:
					print('error in backtracking step')


	return OptVC

def find_maxdeg(g):
	deglist = dict(g.degree())
	temp = deglist.items()
	v = max(temp, key=operator.itemgetter(1))
	return v

def Lowerbound(graph):
	lb=graph.number_of_edges() / find_maxdeg(graph)[1]
	lb=ceil(lb)
	return lb


def ceil(d):
    if d > int(d):
        return int(d) + 1
    else:
        return int(d)
    

def VC_Size(VC):
	sum = 0
	for element in VC:
		sum += element[1]
	return sum


def execute_small():
	print('------------ BNB SMALL ---------------------')
	G = get_graph_bnb('dataset/small_adjlist.graph', 'small')
	start = time.time()
	tracemalloc.start()
	Sol_VC = BnB(G)
	for element in Sol_VC:
		if element[1]==0:
			Sol_VC.remove(element)
	print("result:", len(Sol_VC))
	curr, peak = tracemalloc.get_traced_memory()
	tracemalloc.stop()
	end = time.time()
	print(f"running time: {(end-start)*1000} ms") 
	print(f"peak memory: {peak} B")
	print('-------------------------------------------\n')

def execute_medium():
	print('------------ BNB MEDIUM ---------------------')
	G = get_graph_bnb('dataset/medium_adjlist.graph', 'medium')
	start = time.time()
	tracemalloc.start()
	Sol_VC = BnB(G)
	for element in Sol_VC:
		if element[1]==0:
			Sol_VC.remove(element)
	print("result:", len(Sol_VC))
	curr, peak = tracemalloc.get_traced_memory()
	tracemalloc.stop()
	end = time.time()
	print(f"running time: {(end-start)*1000} ms") 
	print(f"peak memory: {peak} B")
	print('-------------------------------------------\n')

def execute_big():
	print('------------ BNB BIG ---------------------')
	G = get_graph_bnb('dataset/big_adjlist.graph', 'big')
	start = time.time()
	tracemalloc.start()
	Sol_VC = BnB(G)
	for element in Sol_VC:
		if element[1]==0:
			Sol_VC.remove(element)
	print("result:", len(Sol_VC))
	curr, peak = tracemalloc.get_traced_memory()
	tracemalloc.stop()
	end = time.time()
	print(f"running time: {(end-start)*1000} ms") 
	print(f"peak memory: {peak} B")
	print('-------------------------------------------')

def execute_test():
	print('------------ BNB TESTING ---------------------')
	G = get_graph_bnb_testing()
	start = time.time()
	tracemalloc.start()
	Sol_VC = BnB(G)
	for element in Sol_VC:
		if element[1]==0:
			Sol_VC.remove(element)
	print("result:", len(Sol_VC))
	curr, peak = tracemalloc.get_traced_memory()
	tracemalloc.stop()
	end = time.time()
	print(f"running time: {(end-start)*1000} ms") 
	print(f"peak memory: {peak} B")
	print('-------------------------------------------')


def main():
	execute_small()
	execute_medium()
	execute_big()
	execute_test()

if __name__ == '__main__':
	main()