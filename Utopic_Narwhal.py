def dfs(graph, visited, current):
    visited[current] = True
    for neighbor in graph[current]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

def main():
    # Read input
    N, M = map(int, input().split())
    
    # Initialize graph as adjacency list
    graph = [[] for _ in range(N)]
    
    # Read edges
    for _ in range(M):
        u, v = map(int, input().split())
        # Decrement to convert to 0-indexed
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph
    
    # Initialize visited array
    visited = [False] * N
    
    # Count connected components
    connected_components = 0
    for i in range(N):
        if not visited[i]:
            connected_components += 1
            dfs(graph, visited, i)
    
    # Print the answer
    print(connected_components)

if __name__ == "__main__":
    main()
