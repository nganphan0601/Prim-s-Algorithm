''' 
Input: A weighted graph (undirected)
Output: A Minimum spanning tree of the graph 
 (a subset of the edges in the graph which connects all vertices together with no cycles and minimizing the total edge cost)
'''

'''
Data structure: Min Priority queue for edges (with an edge look like (start, end, cost))
Pseudocode:
1. Start the algorithm on any node S
2. Mark S as visited
3. Iterate over all edges of S, add them to the PQ
4. While the PQ is not empty and a MST has not been formed (not all vertices have been visited)

'''

#graph building
import networkx as nx
import tkinter as tk
import heapq as hq

