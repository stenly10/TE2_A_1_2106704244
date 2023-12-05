import networkx as nx
import random
def generate_dataset(file_name, n_nodes):
    g = nx.Graph()
    if n_nodes == 1:
        g.add_node(1)
    else:
        i = 1
        j = 1
        while j<n_nodes:
            j += 1
            g.add_edge(i, j)
            i = random.randint(1,j)
    nx.write_adjlist(g, file_name)

if __name__ == '__main__':
    SMALL = 10**4
    MED = 10**5
    BIG = 10**6
    generate_dataset('dataset/small_adjlist.graph', SMALL)
    generate_dataset('dataset/medium_adjlist.graph', MED)
    generate_dataset('dataset/big_adjlist.graph', BIG)
    