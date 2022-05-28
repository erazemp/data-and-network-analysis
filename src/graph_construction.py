import networkx as nx
import statistics
from collections import defaultdict
import numpy as np
import warnings
from numpy import var
import json
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
import pandas as pd

from src import social_network_analysis_digraph


def load_data(nations):
    # loading the events data
    events = {}
    for nation in nations:
        with open('../data/events/events_%s.json' % nation) as json_data:
            events[nation] = json.load(json_data)

    # loading the match data
    matches = {}
    for nation in nations:
        with open('../data/matches/matches_%s.json' % nation) as json_data:
            matches[nation] = json.load(json_data)

    # loading the players data
    players = {}
    with open('../data/players.json') as json_data:
        players = json.load(json_data)

    # loading the competitions data
    competitions = {}
    with open('../data/competitions.json') as json_data:
        competitions = json.load(json_data)

    # loading the competitions data
    teams = {}
    with open('../data/teams.json') as json_data:
        teams = json.load(json_data)

    return events, matches, players, competitions, teams


# get list id_match_for team id
def match_list(nations, matches, team_Id):
    for nation in nations:
        for match in matches[nation]:
            for match_team_Id in match['teamsData']:
                if team_Id == match_team_Id:
                    list_match_wyId.append(match['wyId'])
    return list_match_wyId


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
def passing_networks(nations, matches, competitions, events, match_id):
    # take the names of the two teams of the match
    competition_name = None
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
                        match['label'].split('-')[0].split(' ')[0] == "uruguay" or
                        match['label'].split('-')[0].split(' ')[0] == "Belgium" or
                        match['label'].split('-')[0].split(' ')[0] == "Croatia"):
                    team1_name = match['label'].split(' -')[0]
                    team2_name = match['label'].split('- ')[1].split(' ,')[0]

                else:
                    team1_name = match['label'].split('-')[0].split(' ')[0]
                    team2_name = match['label'].split('- ')[1].split(' ,')[0]

    # take the events Pass of the match
    match_events = []
    for ev_match in events[competition_name]:
        if ev_match['matchId'] == match_id:
            if ev_match['eventName'] == 'Pass':
                match_events.append(ev_match)

    team2pass2weight = defaultdict(lambda: defaultdict(int))
    for event, next_event in zip(match_events, match_events[1:]):
        try:
            if event['eventName'] == 'Pass' and ACCURATE_PASS in [tag['id'] for tag in event['tags']]:
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
    list_pass.append(sum(list_weight))

    return G1, G2, match_result


if __name__ == '__main__':
    # label of passes
    ACCURATE_PASS = 1801

    # get data
    nation = ["World_Cup"]
    events, matches, players, competitions, teams = load_data(nation)

    # Passing network
    list_match_wyId = []
    list_num_edge = []
    list_num_edge1 = []
    list_num_edge_G = []
    list_pass = []
    list_density = []

    # get list of player_for team id
    list_player = player_list(players, 4418)

    # gemerate passing network for a selected match: #wyid --> match id of world cup matches
    # to je bol test da deluje kreiranje enenga grafa na podlagi match_id
    G1, G2, match_result = passing_networks(nation, matches, competitions, events, match_id='2058017')
    a = 0
    # avg clustering
    list_clustering_avg = []
    list_transitivity_avg = []
    list_max_clique = []
    list_betweenness_centrality = []

    # PLAYER LIST
    # MaxMin in/ou/degree
    listplayer_max_in_degree = []
    listplayer_max_out_degree = []
    listplayer_max_degree = []
    listplayer_min_in_degree = []
    listplayer_min_out_degree = []
    listplayer_min_degree = []

    # get matches from the FRANCE national team in the world cup: total of 7 matches
    match_l = match_list(nation, matches, team_Id='4418')
    for match_id in match_l:
        print(match_id)
        G1, G2, match_result = passing_networks(nation, matches, competitions, events, match_id=match_id)
        # plot_passing_networks(G1, G2)
        if (G1.name == "France"):
            list_num_edge = social_network_analysis_digraph(G1, match_result, match_id)
            social_network_analysis_graph(G1, match_id)
        else:
            list_num_edge1 = social_network_analysis_digraph(G2, match_result, match_id)
            social_network_analysis_graph(G2, match_id)
