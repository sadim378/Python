graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'H'],
    'D': ['F'],
    'E': ['B', 'F'],
    'F': ['A'],
    'G': ['D'],
    'H': ['A', 'G']
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

print("DFS traversal starting from 'A':")
dfs(visited, graph, 'A')