import json
import statistics

from src.statistical_analysis import statistical_analysis_season_max, statistical_analysis_season_min


def get_results(measures):
    print('\nmax_degree_centrality_avg')
    max_degree_centrality_avg = statistical_analysis_season_max(measures.listplayer_max_centrality_degree)
    print('\n max_in_degree_centrality_avg')
    max_in_degree_centrality_avg = statistical_analysis_season_max(measures.listplayer_max_centrality_indegree)
    print('\n max_out_degree_cetrality_avg')
    max_out_degree_centrality_avg = statistical_analysis_season_max(measures.listplayer_max_centrality_outdegree)

    print('\nmin_degree_centrality_avg')
    min_degree_centrality_avg = statistical_analysis_season_min(measures.listplayer_min_centrality_degree)
    print('\n min_indegree_centrality_avg')
    min_indegree_centrality_avg = statistical_analysis_season_min(measures.listplayer_min_centrality_indegree)
    print('\n min_outdegree_centrality_avg')
    min_outdegree_centrality_avg = statistical_analysis_season_min(measures.listplayer_min_centrality_outdegree)

    print('\nlistplayer_max_closeness_centrality')
    max_closeness_centrality_avg = statistical_analysis_season_max(measures.listplayer_max_closeness_centrality)

    print('\n listplayer_min_closeness_centrality')
    min_closeness_centrality_avg = statistical_analysis_season_min(measures.listplayer_min_closeness_centrality)
    for element in measures.listplayer_min_betweenness_centrality:
        print(element[0])
        if element[1] == 0.0:
            measures.listplayer_min_betweenness_centrality.remove(element)
            v = -1
            measures.listplayer_min_betweenness_centrality.append([element[0], v])
    print('\nlistplayer_max_betweenness_centrality')
    max_betweenness_centrality_avg = statistical_analysis_season_max(measures.listplayer_max_betweenness_centrality)
    print('\n listplayer_min_betweenness_centrality')
    min_betweenness_centrality_avg = statistical_analysis_season_min(measures.listplayer_min_betweenness_centrality)

    print('\nlistplayer_max_clustering_coefficient')
    max_clustering_coefficient_avg = statistical_analysis_season_max(measures.listplayer_max_clustering_coefficient)
    print('\n listplayer_min_betweenness_centrality')
    min_clustering_coefficient_avg = statistical_analysis_season_min(measures.listplayer_min_clustering_coefficient)

    print('\nlistplayer_max_pagerank')
    max_pagerank_avg = statistical_analysis_season_max(measures.listplayer_max_pagerank)
    print('\n listplayer_min_pagerank')
    min_pagerank_avg = statistical_analysis_season_min(measures.listplayer_min_pagerank)

    data_tournament = {
        'max_degree_centrality_avg': max_degree_centrality_avg,
        'max_indegree_centrality_avg': max_in_degree_centrality_avg,
        'max_outdegree_centrality_avg': max_out_degree_centrality_avg,

        'min_degree_centrality_avg': min_degree_centrality_avg,
        'min_indegree_centrality_avg': min_indegree_centrality_avg,
        'min_outdegree_centrality_avg': min_outdegree_centrality_avg,

        'max_closeness_centrality_avg': max_closeness_centrality_avg,
        'min_closeness_centrality_avg': min_closeness_centrality_avg,

        'max_betweenness_centrality_avg': max_betweenness_centrality_avg,
        'min_betweenness_centrality_avg': min_betweenness_centrality_avg,

        'max_clustering_coefficient_avg': max_clustering_coefficient_avg,
        'min_clustering_coefficient_avg': min_clustering_coefficient_avg,

        'max_pagerank_avg': max_pagerank_avg,
        'min_pagerank_avg': min_pagerank_avg
    }

    with open('../results/sna_tournament_player_france.json', 'w') as f:
        json.dump(data_tournament, f, indent=4)

    print('avg density')
    avg_density = statistics.mean(measures.list_density)
    print(avg_density)

    print('avg degree')
    avg_degree = statistics.mean(measures.list_degree_avg)
    print(avg_degree)

    print('edge connectivity avg')
    avg_edge_connectivity = statistics.mean(measures.list_edge_connectivity_avg)
    print(avg_edge_connectivity)

    print(' list_clustering_avg ')
    avg_clustering_global = statistics.mean(measures.list_clustering_avg)
    print(avg_clustering_global)

    print(' max_clique ')
    avg_max_clique = statistics.mean(measures.list_max_clique)
    print(avg_max_clique)

    print(' transivity ')
    avg_transivity = statistics.mean(measures.list_transitivity_avg)
    print(avg_transivity)

    list_num_edge_2 = measures.list_num_edge1 + measures.list_num_edge
    avg_edge_G = statistics.mean(list_num_edge_2)
    max_edge = max(list_num_edge_2)
    min_edge = min(list_num_edge_2)
    print("Statistics passing")
    print("avg: %.2f" % avg_edge_G, 'min:', min_edge, 'max:', max_edge)