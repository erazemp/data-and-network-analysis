import networkx as nx
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd


# function plot graph
def plot_passing_networks(G1, G2, match_id, save=False):
    pos1 = nx.spring_layout(G1)
    pos2 = nx.spring_layout(G2)
    nome2degree = dict(G1.degree)
    # edgewidth1 = [d['weight'] for (u, v, d) in G1.edges(data=True)]

    nx.draw(G1, pos=pos1, nodelist=list(nome2degree.keys()),
            node_size=[deg * 50 for deg in nome2degree.values()],
            node_color='red', edge_color='black',
            with_labels=True, font_weight='bold', alpha=0.75)
    if save:
        nx.write_gexf(G1, f'../results/plot_passing_networks_G1_{match_id}.gexf')
        plt.savefig(f'../results/plot_passing_networks_G1_{match_id}.png')
    plt.show()

    nome2degree = dict(G2.degree)
    # edgewidth2 = [d['weight'] for (u, v, d) in G2.edges(data=True)]

    nx.draw(G2, pos=pos2, nodelist=list(nome2degree.keys()),
            node_size=[deg * 50 for deg in nome2degree.values()],
            node_color='blue', edge_color='black',
            with_labels=True, font_weight='bold', alpha=0.75)
    if save:
        nx.write_gexf(G2, f'../results/plot_passing_networks_G2_{match_id}.gexf')
        plt.savefig(f'../results/plot_passing_networks_G2_{match_id}.png')
    plt.show()


# function plot centrality
def plot_centrality(players_centralities, names, cent_name, id_p, save=True,):
    sns.set_style('ticks')

    f, ax = plt.subplots(figsize=(10, 5))
    for player_centralities, player_name in zip(players_centralities, names):
        sns.distplot(pd.DataFrame(player_centralities, columns=['centrality'])['centrality'],
                     label=player_name)
    plt.grid(alpha=0.55)
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.xlabel(cent_name, fontsize=20)
    plt.ylabel('frequency', fontsize=20)
    ax.legend(loc=1, fontsize=18, frameon=True, shadow=True)
    f.tight_layout()
    if save:
        plt.savefig('../results/plot_' + id_p + '.png')
    plt.show()
