def findMinEdge(edges):
    # Initialize variables to store minimum edge and weight
    minEdge = None
    minWeight = float('inf')

    # Iterate through edges to find the minimum
    for v, weight in edges.items():
        if weight < minWeight:
            minEdge = v
            minWeight = weight

    return minEdge, minWeight

def prim(graph):
    # Initialize an empty set to hold the vertices in the minimum spanning tree
    mst = set()

    # Select the first vertex to start the tree
    startVertex = list(graph.keys())[0]
    mst.add(startVertex)

    # Initialize the set of edges to consider
    edges = graph[startVertex]

    # Iterate until all vertices are in the minimum spanning tree
    while len(mst) < len(graph):
        # Find the minimum edge in the set of edges
        minEdge, minWeight = findMinEdge(edges)

        # Add the vertex to the minimum spanning tree
        mst.add(minEdge)

        # Add the edges connected to the vertex to the set of edges to consider
        for v, weight in graph[minEdge].items():
            if v not in mst:
                edges[v] = weight

        # Remove the minimum edge from the set of edges to consider
        del edges[minEdge]

    # Return the minimum spanning tree as a list
    return list(mst)

# Define the graph as an adjacency list
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

# Call the prim function with the graph
minimum_spanning_tree = prim(graph)

# Print the minimum spanning tree
print(minimum_spanning_tree)
