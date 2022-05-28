import networkx as nx
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd


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
    if save:
        nx.write_gexf(G1, "G1.gexf")
        plt.savefig('../results/plot_passing_networks_G1.png')
    plt.show()

    nome2degree = dict(G2.degree)
    # edgewidth2 = [d['weight'] for (u, v, d) in G2.edges(data=True)]

    nx.draw(G2, pos=pos2, nodelist=list(nome2degree.keys()),
            node_size=[deg * 50 for deg in nome2degree.values()],
            node_color='blue', edge_color='black',
            with_labels=True, font_weight='bold', alpha=0.75)
    if save:
        plt.savefig('../results/plot_passing_networks_G2.png')
        nx.write_gexf(G2, "G2.gexf")
    plt.show()


# function plot centrality
def plot_centrality(players_centralities, names):
    sns.set_style('ticks')

    f, ax = plt.subplots(figsize=(10, 5))
    for player_centralities, player_name in zip(players_centralities, names):
        sns.distplot(pd.DataFrame(player_centralities, columns=['centrality'])['centrality'],
                     label=player_name)
    plt.grid(alpha=0.5)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('centrality', fontsize=25)
    plt.ylabel('frequency', fontsize=25)
    lab = ax.legend(loc=1, fontsize=18, frameon=True, shadow=True)
    f.tight_layout()
    plt.show()
