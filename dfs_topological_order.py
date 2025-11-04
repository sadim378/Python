from collections import defaultdict

# Add edge function
def add_edge(graph, u, v):
    graph[u].append(v)

# DFS based topological sort
def dfs_topo(node, visited, stack, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_topo(neighbor, visited, stack, graph)
    stack.append(node)

# Main
n = int(input("Enter number of nodes: "))
e = int(input("Enter number of edges: "))

graph = defaultdict(list)
print("Enter edges (u v) meaning u -> v:")
for _ in range(e):
    u, v = map(int, input().split())
    add_edge(graph, u, v)

visited = [False] * (n + 1)
stack = []

for node in range(1, n + 1):
    if not visited[node]:
        dfs_topo(node, visited, stack, graph)

print("\nTopological Order of traversal:")
print(stack[::-1])
