def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result

def dfs_recursive(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []

    if start not in visited:
        visited.add(start)
        result.append(start)
        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                dfs_recursive(graph, neighbor, visited, result)

    return result


graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'C', 'H'],
    'E': ['B', 'F'],
    'F': ['A'],
    'D': ['F'],
    'H': ['A']
}

cleaned_graph = {}
for node, neighbors in graph.items():
    cleaned_neighbors = []
    for neighbor in neighbors:
        if neighbor != node and neighbor not in cleaned_neighbors:
            cleaned_neighbors.append(neighbor)
    cleaned_graph[node] = cleaned_neighbors

print("Graph:", cleaned_graph)
print("\nDFS Iterative from 'A':", dfs(cleaned_graph, 'A'))
print("DFS Recursive from 'A':", dfs_recursive(cleaned_graph, 'A'))
print("\nDFS Iterative from 'C':", dfs(cleaned_graph, 'C'))
print("DFS Recursive from 'C':", dfs_recursive(cleaned_graph, 'C'))