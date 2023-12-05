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

def print_to_file(edges, file_name):
    f = open(file_name, 'w')
    for elm in edges:
        f.write(f"{elm[0]} {elm[1]}\n")
    f.close()

if __name__ == '__main__':
    SMALL = 10**4
    MED = 10**5
    BIG = 10**6
    TEST = 5
    # generate_dataset('dataset/small_adjlist.graph', SMALL)
    # generate_dataset('dataset/medium_adjlist.graph', MED)
    # generate_dataset('dataset/big_adjlist.graph', BIG)
    generate_dataset('dataset/test_adjlist.graph', TEST)
    