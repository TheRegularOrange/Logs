def selectionSort(a):
    for i in range(len(a)):
        m = min(range(i, len(a)), key=a.__getitem__)
        a[i], a[m] = a[m], a[i]
    return a

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted array:", selectionSort(arr))



import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start], heap = 0, [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

for node, d in dijkstra(graph, 'A').items():
    print(f"{node}: {d}")
