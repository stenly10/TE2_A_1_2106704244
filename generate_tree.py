import networkx as nx

def make_adj_list_from_dataset(filename):
    G = nx.read_adjlist(filename, nodetype=int)
    adj = dict(G.adjacency())
    lst = [[]]
    for i in range(1,len(adj.keys())+1):
        lst.append(list(adj[i].keys()))
    return lst

def get_adj_list_for_dp(filename):
    adj = make_adj_list_from_dataset(filename)
    return adj

def get_graph_bnb(filename, type):
    G = nx.read_adjlist(filename, nodetype=int)
    N = 0
    if type == 'small':
        N = 10**4
        for i in range(101, N+1):
            G.remove_node(i)
    elif type == 'medium':
        N = 10**5
        for i in range(301, N+1):
            G.remove_node(i)
    elif type == 'big':
        N = 10**6
        for i in range(901, N+1):
            G.remove_node(i)
    print(G)
    
    return G

def bnb_testing():
    G = nx.read_adjlist('dataset/test_adjlist.graph', nodetype=int)
    return G
# def bnb_testing(filename, type):
#     G = nx.read_adjlist(filename, nodetype=int)
#     if type == 'small':
#         N = 10**4
#         for i in range(101, N+1):
#             G.remove_node(i)
#     adj = dict(G.adjacency())
#     lst = []
#     for i in range(0,len(adj.keys())):
#         lst.append(list(adj[i+1].keys()))
#     print(lst)
#     file = open('dataset/test_adjlist.txt', 'w')
#     for i in range(len(lst)):
#         tmp = [i+1] + lst[i] + ['\n']
#         file.write(" ".join([str(i) for i in tmp]))
    
#     return lst

if __name__ == '__main__':
    bnb_testing('dataset/small_adjlist.graph', 'small')
