from generate_tree import get_adj_list_for_dp, dp_testing
import time, tracemalloc

def addEdge(adj, x, y):
    adj[x].append(y)
    adj[y].append(x)
 
 
def dfs(adj, dp, src, par):
    for child in adj[src]:
        if child != par:
            dfs(adj, dp, child, src)
 
    for child in adj[src]:
        if child != par:
            # not including source in the vertex cover
            dp[src][0] = dp[child][1] + dp[src][0]
 
            # including source in the vertex cover
            dp[src][1] = dp[src][1] + min(dp[child][1], dp[child][0])
 
 
def minSizeVertexCover(adj, N):
    dp = [[0 for j in range(2)] for i in range(N+1)]
    for i in range(1, N+1):
        # 0 denotes not included in vertex cover
        dp[i][0] = 0
 
        # 1 denotes included in vertex cover
        dp[i][1] = 1
 
    dfs(adj, dp, 1, -1)
 
    # printing minimum size vertex cover
    print('result:', min(dp[1][0], dp[1][1]))

def execute_small():
    print('------------ DP SMALL ---------------------')
    adj = get_adj_list_for_dp('dataset/small_adjlist.graph')
    start = time.time()
    tracemalloc.start()
    minSizeVertexCover(adj, len(adj)-1)
    curr, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()
    print(f"running time: {end-start} ms")
    print(f"peak memory: {peak/(2**20)} MB")
    print('-------------------------------------------\n')

def execute_medium():
    print('------------ DP MEDIUM ---------------------')
    adj = get_adj_list_for_dp('dataset/medium_adjlist.graph')
    start = time.time()
    tracemalloc.start()
    minSizeVertexCover(adj, len(adj)-1)
    curr, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()
    print(f"running time: {end-start} ms") 
    print(f"peak memory: {peak/(2**20)} MB")
    print('-------------------------------------------\n')

def execute_big():
    print('------------ DP BIG ---------------------')
    adj = get_adj_list_for_dp('dataset/big_adjlist.graph')
    start = time.time()
    tracemalloc.start()
    minSizeVertexCover(adj, len(adj)-1)
    curr, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()
    print(f"running time: {end-start} ms")
    print(f"peak memory: {peak/(2**20)} MB")
    print('-------------------------------------------')

# def execute_test():
#     print('------------ DP TEST ---------------------')
#     adj = dp_testing('dataset/small_adjlist.graph', 'small')
#     start = time.time()
#     tracemalloc.start()
#     minSizeVertexCover(adj, len(adj)-1)
#     curr, peak = tracemalloc.get_traced_memory()
#     tracemalloc.stop()
#     end = time.time()
#     print(f"running time: {end-start} ms")
#     print(f"peak memory: {peak/(2**20)} MB")
#     print('-------------------------------------------\n')

def main():
    execute_small()
    execute_medium()
    execute_big()

if __name__ == '__main__':
    main()