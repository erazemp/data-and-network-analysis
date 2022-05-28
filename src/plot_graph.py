import networkx as nx
from matplotlib import pyplot as plt


# function plot graph
def plot_passing_networks(G1, G2, save=False):
    pos1 = nx.spring_layout(G1)
    pos2 = nx.spring_layout(G2)
    nome2degree = dict(G1.degree)
    # edgewidth1 = [d['weight'] for (u, v, d) in G1.edges(data=True)]

    nx.draw(G1, pos=pos1, nodelist=list(nome2degree.keys()),
            node_size=[deg * 50 for deg in nome2degree.values()],
            node_color='red', edge_color='black',
            with_labels=True, font_weight='bold', alpha=0.75)
    plt.show()

    nome2degree = dict(G2.degree)
    # edgewidth2 = [d['weight'] for (u, v, d) in G2.edges(data=True)]

    nx.draw(G2, pos=pos2, nodelist=list(nome2degree.keys()),
            node_size=[deg * 50 for deg in nome2degree.values()],
            node_color='blue', edge_color='black',
            with_labels=True, font_weight='bold', alpha=0.75)
    plt.show()

    if save:
        nx.write_gexf(G1, "G1.gexf")
        nx.write_gexf(G2, "G2.gexf")
