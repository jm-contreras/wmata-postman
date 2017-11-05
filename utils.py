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
