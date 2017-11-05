# Import modules
import itertools as it

import networkx as nx
import pandas as pd

import utils as u


# Create empty graph
graph = nx.Graph()

# Load edge and node lists
edgelist = pd.read_csv('edgelist_wmata.csv')
nodelist = pd.read_csv('nodelist_wmata.csv')

# Add edges, nodes, and their attributes
graph = u.add_edges(graph, edgelist)
graph = u.add_nodes(graph, nodelist)

# Find nodes of odd degree and odd node pairs
odd_degree_nodes = u.find_odd_degree_nodes(graph)
odd_node_pairs = list(it.combinations(odd_degree_nodes, 2))

# Compute shortest distance between each pair of nodes in graph
distances = {}
for pair in odd_node_pairs:
    distances[pair] = nx.dijkstra_path_length(graph, pair[0], pair[1], weight='distance')

# Create complete graph
graph_complete = nx.Graph()
for nodes, dist in distances.items():
    graph_complete.add_edge(nodes[0], nodes[1], attr_dict={'distance': dist, 'weight': -dist})

# Compute minimum weight matching
matches = nx.algorithms.max_weight_matching(graph_complete, maxcardinality=True)

# Remove duplicates
matches = list(pd.unique([tuple(sorted([k, v])) for k, v in matches.items()]))

# Augment original graph with matches
# We need to make the augmented graph a MultiGraph so we can add parallel edges
for pair in matches:
    graph.add_edge(pair[0], pair[1],
                       attr_dict={'distance': nx.dijkstra_path_length(graph, pair[0], pair[1]),
                                  'trail': 'augmented'}
                       )
return graph_aug