import networkx as nx

def make_adj_list_from_dataset(filename):
    G = nx.read_adjlist(filename, nodetype=int)
    adj = dict(G.adjacency())
    lst = [[]]
    for i in range(1,len(adj.keys())+1):
        lst.append(list(adj[i].keys()))
    print(G)
    return lst

def get_adj_list_for_dp(filename):
    adj = make_adj_list_from_dataset(filename)
    return adj

def get_graph_bnb(filename, type):
    G = nx.read_adjlist(filename, nodetype=int)
    N = 0
    if type == 'small':
        N = 10**4
        for i in range(71, N+1):
            G.remove_node(i)
    elif type == 'medium':
        N = 10**5
        for i in range(81, N+1):
            G.remove_node(i)
    elif type == 'big':
        N = 10**6
        for i in range(101, N+1):
            G.remove_node(i)
    print(G)
    return G

def get_graph_bnb_testing():
    G = nx.read_adjlist('dataset/testing_adjlist.graph', nodetype=int)
    return G