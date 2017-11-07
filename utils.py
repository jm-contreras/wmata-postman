import networkx as nx
import pandas as pd


def add_edges(g, el):

    for _, row in el.iterrows():
        g.add_edge(row['node1'], row['node2'], attr_dict=dict(row[['node' not in c for c in row.index]]))

    return g


def add_nodes(g, nl):

    for __, row in nl.iterrows():
        g.add_node(row['id'], attr_dict=dict(row[['x', 'y']]))

    return g


def find_odd_degree_nodes(g):

    return [v for v, d in g.degree if d % 2 == 1]


def find_shortest_distances(pairs, graph):

    distances = {}

    for p in pairs:
        distances[p] = nx.dijkstra_path_length(graph, p[0], p[1], weight='distance')

    return distances


def build_complete_graph(distances):

    graph = nx.Graph()

    for nodes, dist in distances.items():
        graph.add_edge(nodes[0], nodes[1], attr_dict={'distance': dist, 'weight': -dist})

    return graph


def compute_min_weight_matches(graph):

    # Compute minimum weight matching, removing duplicates
    matches = nx.algorithms.max_weight_matching(graph, maxcardinality=True)

    # Remove duplicates
    return list(pd.unique([tuple(sorted([k, v])) for k, v in matches.items()]))


def augment_graph_with_matches(graph, matches):

    # Make augmented graph MultiGraph to add parallel edges
    graph_augmented = nx.MultiGraph(graph.copy())

    for pair in matches:
        distance = nx.dijkstra_path_length(graph, pair[0], pair[1])
        graph_augmented.add_edge(pair[0], pair[1], attr_dict={'distance': distance, 'edge': 'augmented'})

    return graph_augmented
