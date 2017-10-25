# Import modules
import networkx as nx
import pandas as pd

# Create empty graph
graph = nx.Graph()

# Load edge list
edgelist = pd.read_csv('edgelist_wmata.csv')

# Add edges and edge attributes
for _, row in edgelist.iterrows():
    graph.add_edge(row['node1'], row['node2'], attr_dict=dict(row[['node' not in c for c in row.index]]))

# TODO: Debug seemingly incorrectly called method in graph object
nodelist = pd.read_csv('https://gist.githubusercontent.com/brooksandrew/f989e10af17fb4c85b11409fea47895b/raw/a3a8da0fa5b094f1ca9d82e1642b384889ae16e8/nodelist_sleeping_giant.csv')

for i, nlrow in nodelist.iterrows():
    graph.add_node[nlrow['id']] = nlrow[1:].to_dict()
