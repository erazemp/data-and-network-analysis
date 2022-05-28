import networkx as nx
import statistics
from numpy import var
import json


# function for calculate metrics for sna in digraph
def social_network_analysis_digraph(G, match_result, match_id, remove_nodes, measures):
    list_num_edge = []

    G.remove_edges_from(nx.selfloop_edges(G))

    if remove_nodes:
        if G.has_node('P. Pogba'):
            G.remove_node('P. Pogba')

        if G.has_node('A. Griezmann'):
            G.remove_node('A. Griezmann')

        if G.has_node('N. Kanté'):
            G.remove_node('N. Kanté')

    info_graph = nx.info(G)
    print('info G')
    print(info_graph)

    # edges
    print('edges analysis')
    # weight
    print(G.edges.data())
    number_of_edge = G.number_of_edges()
    print(number_of_edge)
    list_num_edge.append(number_of_edge)

    # degree
    print('degree')
    degree_team = dict(G.degree)
    print(degree_team)
    highest = max(degree_team.values())
    smallest = min(degree_team.values())

    degree = sorted([d for n, d in G.degree()], reverse=True)

    avarage_degree = statistics.mean(degree)
    print("Average degree")
    print("%.2f" % avarage_degree)
    measures.list_degree_avg.append(avarage_degree)

    for player, value in degree_team.items():
        if value == highest:
            measures.listplayer_max_degree.append([player, value])
        if value == smallest:
            measures.listplayer_min_degree.append([player, value])

    # in_degree
    print('In_degree')
    in_degree_team = dict(G.in_degree)
    print(in_degree_team)
    highest_in_degree = max(in_degree_team.values())
    smallest_in_degree = min(in_degree_team.values())
    # variance
    var_in_degree = var(list(in_degree_team.values()))
    print(var_in_degree)

    for player, value in in_degree_team.items():
        if value == highest_in_degree:
            measures.listplayer_max_in_degree.append([player, value])
        if value == smallest_in_degree:
            measures.listplayer_min_in_degree.append([player, value])

    # out_degree
    print('Out_degree')
    out_degree_team = dict(G.out_degree)
    print(out_degree_team)
    highest_out_degree = max(out_degree_team.values())
    smallest_out_degree = min(out_degree_team.values())
    var_out_degree = var(list(out_degree_team.values()))
    print(var_out_degree)

    for player, value in out_degree_team.items():
        if value == highest_out_degree:
            measures.listplayer_max_out_degree.append([player, value])
        if value == smallest_out_degree:
            measures.listplayer_min_out_degree.append([player, value])

    # density
    density = nx.density(G)
    print('density')
    print("%.2f" % density)
    measures.list_density.append(density)

    # edge_connetivity
    edge_connectivity = nx.edge_connectivity(G)
    print('edge_connectivity')
    print(nx.edge_connectivity(G))
    measures.list_edge_connectivity_avg.append(edge_connectivity)

    # Centrality Degree
    degree_centrality = dict(nx.degree_centrality(G))
    print(degree_centrality)
    highest_degree_centrality = max(degree_centrality.values())
    smallest_degree_centrality = min(degree_centrality.values())

    for player, value in degree_centrality.items():
        if value == highest_degree_centrality:
            measures.listplayer_max_centrality_degree.append([player, value])
        if value == smallest_degree_centrality:
            measures.listplayer_min_centrality_degree.append([player, value])

    # avarage_degree_centrality
    avarage_degree_centrality = statistics.mean(degree_centrality.values())
    print("average degree centrality")
    print("%.2f" % avarage_degree_centrality)

    # in_degree_centrality
    in_degree_centrality = dict(nx.in_degree_centrality(G))
    print('in_degree_centrality')
    print(in_degree_centrality)
    variance_indegree = var(list(in_degree_centrality.values()))
    print(variance_indegree)
    highest_indegree_centrality = max(in_degree_centrality.values())
    smallest_indegree_centrality = min(in_degree_centrality.values())

    for player, value in in_degree_centrality.items():
        if value == highest_indegree_centrality:
            measures.listplayer_max_centrality_indegree.append([player, value])
        if value == smallest_indegree_centrality:
            measures.listplayer_min_centrality_indegree.append([player, value])

    # out_degree_centrality
    out_degree_centrality = dict(nx.out_degree_centrality(G))
    print('out_degree_centrality')
    print(out_degree_centrality)
    highest_outdegree_centrality = max(out_degree_centrality.values())
    smallest_outdegree_centrality = min(out_degree_centrality.values())
    variance_outdegree = var(list(out_degree_centrality.values()))
    print(variance_outdegree)
    for player, value in out_degree_centrality.items():
        if value == highest_outdegree_centrality:
            measures.listplayer_max_centrality_outdegree.append([player, value])
        if value == smallest_outdegree_centrality:
            measures.listplayer_min_centrality_outdegree.append([player, value])

    print(nx.node_connectivity(G))
    # closeness
    closeness_centrality = dict(nx.closeness_centrality(G))
    print('closeness_centrality')
    print(closeness_centrality)
    # var closeness
    print('variance closeness')
    variance_closeness = var(list(closeness_centrality.values()))
    print(variance_closeness)
    # mean closeness
    print('closeness avg')
    avg_closeness = statistics.mean(list(closeness_centrality.values()))
    print(avg_closeness)
    highest_closeness_centrality = max(closeness_centrality.values())
    smallest_closeness_centrality = min(closeness_centrality.values())

    for player, value in closeness_centrality.items():
        if value == highest_closeness_centrality:
            measures.listplayer_max_closeness_centrality.append([player, value])
        if value == smallest_closeness_centrality:
            measures.listplayer_min_closeness_centrality.append([player, value])

    # betweenness
    betweenness_centrality = dict(nx.betweenness_centrality(G))
    print('betweenness_centrality')
    print(betweenness_centrality)
    avg_b = statistics.mean(list(betweenness_centrality.values()))
    print(avg_b)
    highest_betweenness_centrality = max(betweenness_centrality.values())
    smallest_betweenness_centrality = min(betweenness_centrality.values())

    for player, value in betweenness_centrality.items():
        if value == highest_betweenness_centrality:
            measures.listplayer_max_betweenness_centrality.append([player, value])
        if value == smallest_betweenness_centrality:
            measures.listplayer_min_betweenness_centrality.append([player, value])

    # PageRank
    pagerank = dict(nx.pagerank(G))
    print('pagerank')
    print(pagerank)
    highest_pagerank = max(pagerank.values())
    smallest_pagerank = min(pagerank.values())

    for player, value in pagerank.items():
        if value == highest_pagerank:
            measures.listplayer_max_pagerank.append([player, value])
        if value == smallest_pagerank:
            measures.listplayer_min_pagerank.append([player, value])

    # k-core
    print('max k-core')
    max_kcore = max(nx.core_number(G).values())
    print(max_kcore)

    # clustering coefficient
    clustering_coefficient = dict(nx.clustering(G))
    print('clustering coefficient')
    print(clustering_coefficient)
    print('average clustering')
    avg_clustering = (nx.average_clustering(G))
    print(avg_clustering)
    highest_clustering_coefficient = max(clustering_coefficient.values())
    smallest_clustering_coefficient = min(clustering_coefficient.values())

    for player, value in clustering_coefficient.items():
        if value == highest_clustering_coefficient:
            measures.listplayer_max_clustering_coefficient.append([player, value])
        if value == smallest_clustering_coefficient:
            measures.listplayer_min_clustering_coefficient.append([player, value])

    # clustering coefficient avg
    measures.list_avg_clustering = []
    for item in clustering_coefficient.values():
        measures.list_avg_clustering.append(item)

    avarage_clustering_coefficient = statistics.mean(measures.list_avg_clustering)
    measures.list_clustering_avg.append(avarage_clustering_coefficient)

    print('avarage_clustering coefficient')
    print("%.2f" % avarage_clustering_coefficient)

    print('assortativity')
    assortativity = nx.degree_assortativity_coefficient(G)
    print(assortativity)
    pearson = nx.degree_pearson_correlation_coefficient(G)
    print(pearson)
    # function to add to JSON
    data_match = {'match_id': match_id,
                  'label_match': match_result,
                  'info': info_graph,
                  'density': density,
                  'degree': degree_team,
                  'avarage_degree': avarage_degree,
                  'in_degree': in_degree_team,
                  'out_degree': out_degree_team,
                  'degree_centrality': degree_centrality,
                  'avarage_degree_centrality': avarage_degree_centrality,
                  'in_degree_centrality': in_degree_centrality,
                  'out_degree_centrality': out_degree_centrality,
                  'closeness_centrality': closeness_centrality,
                  'betweenness_centrality': betweenness_centrality,
                  'pagerank': pagerank,
                  'edge_connectivity': edge_connectivity,
                  'max-k-core': max_kcore,
                  'clustering_coefficient': clustering_coefficient,
                  'avarage_clustering_coefficient': avarage_clustering_coefficient,
                  }
    with open('../results/sna_match_' + str(match_id) + '.json', 'w', encoding='utf-8') as f:
        json.dump(data_match, f, indent=4)

    return measures, list_num_edge


# function for calculate metrics for sna in graph
def social_network_analysis_graph(G, match_id, measures):
    # function for add JSON code
    def write_json(data, filename='../results/sna_match_' + str(match_id) + '.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    if G.number_of_nodes() > 0:
        G = G.to_undirected()
        if nx.is_connected(G):
            clique = nx.find_cliques(G)
            for x in clique:
                print(x)
            from networkx.algorithms.approximation import clique
            max_clique = nx.graph_number_of_cliques(G)
            print('')
            print("Maximum clique number")
            print(max_clique)
            measures.list_max_clique.append(max_clique)
            # triangles
            triangles = nx.triangles(G)
            print("Triangles in team")
            print(triangles)
            num_triangles = (sum(list(nx.triangles(G).values())))
            print("Number of triangles")
            print(num_triangles)
            # transitivity
            transitivity = nx.transitivity(G)
            print("Transitivity")
            print("%.2f" % transitivity)
            measures.list_transitivity_avg.append(transitivity)

            with open('../results/sna_match_' + str(match_id) + '.json', encoding='utf-8') as json_file:
                data = json.load(json_file)

                data_match = {
                    'max clique number': max_clique,
                    'triangles for node': triangles,
                    'number_of_triangles': num_triangles,
                    'transitivity': transitivity,
                }
                # appending data
                data.update(data_match)
            write_json(data)

    return measures
