import statistics

import networkx as nx
from collections import defaultdict
import json

from src.plot_graph import plot_passing_networks
from src.resutls import get_results
from src.social_network_analysis import social_network_analysis_digraph, social_network_analysis_graph
from src.statistical_analysis import statistical_analysis_season_max, statistical_analysis_season_min


def load_data(nations):
    # loading the events data
    events = {}
    for nation in nations:
        with open('../data/events/events_%s.json' % nation, encoding='utf-8') as json_data:
            events[nation] = json.load(json_data)

    # loading the match data
    matches = {}
    for nation in nations:
        with open('../data/matches/matches_%s.json' % nation, encoding='utf-8') as json_data:
            matches[nation] = json.load(json_data)

    # loading the players data
    players = {}
    with open('../data/players.json', encoding='utf-8') as json_data:
        players = json.load(json_data)

    # loading the competitions data
    competitions = {}
    with open('../data/competitions.json', encoding='utf-8') as json_data:
        competitions = json.load(json_data)

    # loading the competitions data
    teams = {}
    with open('../data/teams.json', encoding='utf-8') as json_data:
        teams = json.load(json_data)

    return events, matches, players, competitions, teams


# get list id_match_for team id
def match_list(nations, matches, team_Id, measures):
    for nation in nations:
        for match in matches[nation]:
            for match_team_Id in match['teamsData']:
                if team_Id == match_team_Id:
                    measures.list_match_wyId.append(match['wyId'])
    return measures


# get list of player_for team id
def player_list(players, team_Id):
    list_player = []
    for player in players:
        if player['currentTeamId'] == team_Id:
            player_id = player['wyId']
            player_short_name = player['shortName'].encode('ascii', 'strict').decode('unicode-escape')
            player_team = [player_id, player_short_name]
            list_player.append(player_team)
    return list_player


# function for generete passing network for a match
def passing_networks(nations, matches, competitions, events, match_id, measures):
    match_result = ''
    team1_name = ''
    team2_name = ''
    # take the names of the two teams of the match
    competition_name = "World_Cup"
    for nation in nations:
        for match in matches[nation]:
            if match['wyId'] == match_id:
                match_result = match['label']
                print(match['label'])
                for competition in competitions:
                    if competition['wyId'] == match['competitionId']:
                        competition_name = "World_Cup"  # name in data wrong --> needs to be hardcoded for world cup
                if (match['label'].split('-')[0].split(' ')[0] == "Australia" or
                        match['label'].split('-')[0].split(' ')[0] == "Peru" or
                        match['label'].split('-')[0].split(' ')[0] == "Denmark" or
                        match['label'].split('-')[0].split(' ')[0] == "Argentina" or
                        match['label'].split('-')[0].split(' ')[0] == "Uruguay" or
                        match['label'].split('-')[0].split(' ')[0] == "Belgium" or
                        match['label'].split('-')[0].split(' ')[0] == "Croatia"):
                    team1_name = match['label'].split(' -')[0]
                    team2_name = match['label'].split('- ')[1].split(', ')[0]

                else:
                    team1_name = match['label'].split('-')[0].split(' ')[0]
                    team2_name = match['label'].split('- ')[1].split(', ')[0]

    # take the events Pass of the match
    match_events = []
    for ev_match in events[competition_name]:
        if ev_match['matchId'] == match_id:
            if ev_match['eventName'] == 'Pass':
                match_events.append(ev_match)

    sender = ''
    team2pass2weight = defaultdict(lambda: defaultdict(int))
    for event, next_event in zip(match_events, match_events[1:]):
        try:
            if event['eventName'] == 'Pass' and accurate_pass in [tag['id'] for tag in event['tags']]:
                for player in players:
                    if player['wyId'] == event['playerId']:
                        sender = player['shortName'].encode('ascii', 'strict').decode('unicode-escape')
                if next_event['teamId'] == event['teamId']:
                    for player in players:
                        if player['wyId'] == next_event['playerId']:
                            receiver = player['shortName'].encode('ascii', 'strict').decode('unicode-escape')
                            for team in teams:
                                if team['wyId'] == next_event['teamId']:
                                    team2pass2weight[team['name']][(sender, receiver)] += 1
        except KeyError:
            pass

    # crete networkx graphs
    list_weight = []
    G1, G2 = nx.DiGraph(name=team1_name), nx.DiGraph(name=team2_name)
    for (sender, receiver), weight in team2pass2weight[team1_name].items():
        G1.add_edge(sender, receiver, weight=weight)
    for (sender, receiver), weight in team2pass2weight[team2_name].items():
        list_weight.append(weight)
        G2.add_edge(sender, receiver, weight=weight)
    measures.list_pass.append(sum(list_weight))

    return G1, G2, match_result, measures


class Measures:
    def __init__(self):
        # passing network
        self.list_match_wyId = []
        self.list_num_edge_1 = []
        self.list_num_edge_2 = []
        self.list_pass = []
        self.list_density = []

        # avg final in/out/degree
        self.list_degree_avg = []

        # avg final edge
        self.list_edge_connectivity_avg = []

        # avg clustering
        self.list_clustering_avg = []
        self.list_transitivity_avg = []
        self.list_max_clique = []
        self.list_betweenness_centrality = []

        # PLAYER LIST
        # MaxMin in/ou/degree
        self.listplayer_max_in_degree = []
        self.listplayer_max_out_degree = []
        self.listplayer_max_degree = []
        self.listplayer_min_in_degree = []
        self.listplayer_min_out_degree = []
        self.listplayer_min_degree = []

        # MaxMin list centrality in/out/degree
        self.listplayer_max_centrality_degree = []
        self.listplayer_max_centrality_outdegree = []
        self.listplayer_max_centrality_indegree = []
        self.listplayer_min_centrality_degree = []
        self.listplayer_min_centrality_outdegree = []
        self.listplayer_min_centrality_indegree = []

        # MaxMin self.list closeness centrality
        self.listplayer_max_closeness_centrality = []
        self.listplayer_min_closeness_centrality = []

        # MaxMin list betweenness_centrality
        self.listplayer_max_betweenness_centrality = []
        self.listplayer_min_betweenness_centrality = []

        # MaxMin clustering_coefficient
        self.listplayer_max_clustering_coefficient = []
        self.listplayer_min_clustering_coefficient = []

        # MaxMin pagerank
        self.listplayer_max_pagerank = []
        self.listplayer_min_pagerank = list()


if __name__ == '__main__':
    measures = Measures()

    # label of passes
    accurate_pass = 1801

    # get data
    nation = ["World_Cup"]
    events, matches, players, competitions, teams = load_data(nation)

    # get list of player_for team id
    list_player = player_list(players, 4418)

    # get matches from the FRANCE national team in the world cup: total of 7 matches
    measures = match_list(nation, matches, '4418', measures)
    for match_id in measures.list_match_wyId:
        print(match_id)
        G1, G2, match_result, measures = passing_networks(nation, matches, competitions, events, match_id, measures)
        # plot_passing_networks(G1, G2)
        if G1.name == "France":
            measures, measures.list_num_edge_1 = social_network_analysis_digraph(G1, match_result, match_id, False, measures)
            measures = social_network_analysis_graph(G1, match_id, measures)
        else:
            measures, measures.list_num_edge_2 = social_network_analysis_digraph(G2, match_result, match_id, False, measures)
            measures = social_network_analysis_graph(G2, match_id, measures)

    G1, G2, match_result, measures = passing_networks(nation, matches, competitions, events, '2058017', measures)
    social_network_analysis_digraph(G1, match_result, '2058017', False, measures)
    social_network_analysis_graph(G1, '2058017', measures)
    plot_passing_networks(G1, G2, True)
    get_results(measures)