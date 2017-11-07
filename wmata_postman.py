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
distances = u.find_shortest_distances(odd_node_pairs, graph)

# Create complete graph
graph_complete = u.build_complete_graph(distances)

# Compute minimum weight matching, removing duplicates
matches = u.compute_min_weight_matches(graph_complete)

# Augment original graph with matches
graph_augmented = u.augment_graph_with_matches(graph, matches)
