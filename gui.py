import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import networkx as nx
import random

# Prim's algorithm
def prim_algorithm(G):
    MST = nx.Graph()
    start_node = list(G.nodes())[0]  # Start from an arbitrary node
    visited = set([start_node])
    edges = list(G.edges(start_node, data=True))
    while len(visited) < len(G.nodes()):
        edges.sort(key=lambda x: x[2]['weight'])  # Sort edges by weight
        for edge in edges:
            if edge[1] not in visited:
                visited.add(edge[1])
                MST.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
                break
        edges = [edge for edge in G.edges(visited, data=True) if edge[1] not in visited]
    return MST

# Create a weighted graph function
def drawGraph(fig, nodes, connections):
    G = nx.Graph()

    for node in nodes:
        G.add_node(node)

    for edge in connections:
        node1, node2, weight = edge
        G.add_edge(node1, node2, weight=weight)

    MST = prim_algorithm(G)

    fig.clf()
    ax = fig.add_subplot(111)
    
    pos = nx.spring_layout(G, seed=7, k=0.5)  # positions for all nodes

    # Draw the original graph
    nx.draw_networkx_nodes(G, pos, node_size=700, ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=3, alpha=0.5, edge_color="grey", style="solid", ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif", ax=ax)

    # Highlight the edges in the minimum spanning tree
    nx.draw_networkx_edges(MST, pos, edgelist=MST.edges, width=3, alpha=0.9, edge_color="red", style="solid", ax=ax)

    ax.margins(0.08)
    ax.axis("off")

    # Update canvas
    canvas.draw()

# Function to handle button click event
def onDrawGraph():
    nodes = entry_nodes.get().split(',')
    connections = [conn.split('-') for conn in entry_connections.get().split(',')]
    connections = [(conn[0], conn[1], float(conn[2])) for conn in connections]
    drawGraph(fig, nodes, connections)

# Tkinter GUI initialization
m = tk.Tk()
m.title("Prim's Algorithm Visualization")
m.geometry("800x600")

# Title frame
title_frame = tk.Frame(m)
label = tk.Label(title_frame, text="Prim's Algorithm Visualization", font=("Arial", 20))
label.pack()
title_frame.pack(side="top", fill="x")

# Canvas
canvas_frame = tk.Frame(m)
fig = plt.Figure(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()
canvas_widget.config(highlightthickness=2, highlightbackground="black")
canvas_frame.pack(side="top", fill="both", expand=True)

# Input frame
input_frame = tk.Frame(m)
entry_nodes_label = tk.Label(input_frame, text="Enter nodes (comma-separated): ")
entry_nodes = tk.Entry(input_frame, width=50)
entry_connections_label = tk.Label(input_frame, text="Enter connections (node1-node2-weight, comma-separated): ")
entry_connections = tk.Entry(input_frame, width=50)
entry_nodes_label.grid(row=0, column=0)
entry_nodes.grid(row=0, column=1)
entry_connections_label.grid(row=1, column=0)
entry_connections.grid(row=1, column=1)
input_frame.pack(side="top", pady=10)

# Button
button_frame = tk.Frame(m)
draw = tk.Button(button_frame, text="Draw Graph", command=onDrawGraph)
draw.grid(row=0, column=0)
button_frame.pack(side="top")

# Tool bar
toolbar_frame = tk.Frame(m)
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame, pack_toolbar=False)
toolbar.update()
toolbar.pack(anchor="sw", fill=tk.X)
toolbar_frame.pack(side="top", fill="x")

m.mainloop()
