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


#get list of player_for team id
def player_list(players, team_Id):
    for player in players:
            if player['currentTeamId'] == team_Id:
                player_id = player['wyId']
                player_short_name = player['shortName'].encode('ascii', 'strict').decode('unicode-escape')
                player_team = [player_id, player_short_name]
                list_player.append(player_team)
    return list_player



if __name__ == '__main__':
    # data

    # Passing network
    list_match_wyId = []
    list_num_edge = []
    list_num_edge1 = []
    list_num_edge_G = []
    list_pass = []
    list_density = []

    nation = ["World_Cup"]
    events, matches, players, competitions, teams = load_data(nation)
    match = match_list(nation, matches, team_Id=4418,)
    player = player_list(nation, players, team_Id=1625)
    a = 0
