from generate_tree import get_adj_list_for_dp
import time, tracemalloc

# Implementasi Dynamic Programming, referensi: https://www.geeksforgeeks.org/vertex-cover-problem-dynamic-programming-solution-for-tree/

def dfs(adj, dp, src, par):
    for child in adj[src]:
        if child != par:
            dfs(adj, dp, child, src)
 
    for child in adj[src]:
        if child != par:
            dp[src][0] = dp[child][1] + dp[src][0]
            dp[src][1] = dp[src][1] + min(dp[child][1], dp[child][0])
 
 
def minSizeVertexCover(adj, N):
    dp = [[0, 0] for i in range(N+1)]
    for i in range(1, N+1):
        dp[i][0] = 0
        dp[i][1] = 1
 
    dfs(adj, dp, 1, -1)
 
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
    print(f"running time: {(end-start)*1000} ms") 
    print(f"peak memory: {peak} B")
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
    print(f"running time: {(end-start)*1000} ms")  
    print(f"peak memory: {peak} B")
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
    print(f"running time: {(end-start)*1000} ms") 
    print(f"peak memory: {peak} B")
    print('-------------------------------------------')


def main():
    execute_small()
    execute_medium()
    execute_big()

if __name__ == '__main__':
    main()