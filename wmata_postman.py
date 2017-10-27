# Import modules
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
