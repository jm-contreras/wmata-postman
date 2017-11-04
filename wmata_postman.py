# Import modules
import itertools as it
import networkx as nx
import pandas as pd


# Create empty graph
graph = nx.Graph()

# Load edge and node lists
edgelist = pd.read_csv('edgelist_wmata.csv')
nodelist = pd.read_csv('nodelist_wmata.csv')

# Add edges and edge attributes
for _, row in edgelist.iterrows():
    graph.add_edge(row['node1'], row['node2'], attr_dict=dict(row[['node' not in c for c in row.index]]))

# Add nodes and node attributes
for __, row in nodelist.iterrows():
    graph.add_node(row['id'], attr_dict=dict(row[['x', 'y']]))

# Find nodes of odd degree
nodes_odd_degree = [v for v, d in graph.degree if d % 2 == 1]

# Compute odd node pairs
odd_node_pairs = list(it.combinations(nodes_odd_degree, 2))

# Compute shortest distance between each pair of nodes in graph
distances = {}
for pair in odd_node_pairs:
    distances[pair] = nx.dijkstra_path_length(graph, pair[0], pair[1], weight='distance')
