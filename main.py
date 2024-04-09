''' 
Input: A weighted graph (undirected)
Output: A Minimum spanning tree of the graph 
 (a subset of the edges in the graph which connects all vertices together with no cycles and minimizing the total edge cost)
'''

'''
Data structure: Min Priority queue for edges (with an edge look like (cost, start, end))
Pseudocode:
1. Start the algorithm on any node S
2. Mark S as visited
3. Iterate over all edges of S, add them to the PQ
4. While the PQ is not empty and a MST has not been formed (not all vertices have been visited)

'''

#graph building
import networkx as nx
import heapq as hq


# Connected graph
G = nx.Graph()

G.add_edge("a", "b", weight=6)
G.add_edge("a", "c", weight=2)
G.add_edge("c", "d", weight=1)
G.add_edge("c", "e", weight=7)
G.add_edge("c", "f", weight=9)
G.add_edge("a", "d", weight=3)
G.add_edge("b", "g", weight=4)
G.add_edge("g", "c", weight=5)
G.add_edge("b", "d", weight=1)
G.add_edge("h", "f", weight=1)
G.add_edge("h", "d", weight=0.5)
G.add_edge("h", "c", weight=0.5)


# Function to add all edges of a node to the PQ
def add_edge(graph, nodeIndex, visited, queue):
    graph_nodes = list(graph.nodes())
    current_node = graph_nodes[nodeIndex]
    # Mark the current node as visited
    visited[nodeIndex] = True

    # Add all edges of the current node to the PQ that points to unvisited nodes
    edges = graph.edges(current_node)   # Get all edges of the current node
    for edge in edges:
        i = graph_nodes.index(edge[1])
        if visited[i] == False:
            edge_data = G.get_edge_data(current_node, edge[1])
            weight = edge_data["weight"]
            hq.heappush(queue, (weight, current_node, edge[1]))  # Add the edge to the PQ in the form of (weight, start, end)

# Function to find the MST of a graph
def Prims(graph, s = 0):
    num_nodes = graph.number_of_nodes()     # Number of nodes in the graph
    edge_number = num_nodes - 1     # Number of edges in the MST
    cost = 0        # Total cost of the MST
    nodes_list = list(graph.nodes())    # List of all nodes in the graph
    visited = [False for i in graph.nodes()]    # Mark all nodes as unvisited
    queue = []      # Priority queue for edges
    MST = []        # List to store the edges of the MST

    add_edge(graph, s, visited, queue) # Add the first node's edges to the PQ
    
    while len(queue) > 0 and len(MST) < edge_number:
        edge = hq.heappop(queue)    # Get the edge with the smallest weight
        next_node = nodes_list.index(edge[2])     # Get the index of the end node of the edge

        if visited[next_node]:
            continue
        
        MST.append(edge)    # Add the edge to the MST
        cost += edge[0]     # Add the weight of the edge to the total cost
        add_edge(graph, next_node, visited, queue)    # Add the edges of the end node to the PQ

    if len(MST) != edge_number:
        return "Graph is not connected", -1
    
    return MST, cost


# Test the algorithm (Graph is connected)
MST, cost = Prims(G)
print(MST)
print(cost)

# Test the algorithm (Graph is not connected)
P = nx.Graph()

P.add_edge("a", "b", weight=6)
P.add_edge("a", "c", weight=2)
P.add_edge("c", "d", weight=1)
P.add_edge("c", "f", weight=9)
P.add_edge("a", "d", weight=3)
P.add_edge("b", "g", weight=4)
P.add_edge("g", "c", weight=5)
P.add_edge("b", "d", weight=1)
P.add_edge("h", "f", weight=1)
P.add_edge("h", "d", weight=0.5)
P.add_edge("h", "c", weight=0.5)
P.add_edge("i", "j", weight=0.5)

MST, cost = Prims(P)
print(MST)
print(cost)
