def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

def bfs(graph, node):
    visited, queue = set([node]), [node]
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    n = int(input("Enter number of nodes: "))
    graph = {i: [int(input(f"Enter edge for node {i}: ")) for _ in range(int(input(f"Enter number of edges for node {i}: ")))] for i in range(1, n+1)}

    print("DFS:")
    dfs(graph, 1)
    print("\nBFS:")
    bfs(graph, 1)

if __name__ == "__main__":
    main()
