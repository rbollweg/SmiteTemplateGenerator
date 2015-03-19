__author__ = 'The Gibs'

import datetime
import urllib
import hashlib
import json
import time
import re

from smiteapp import convert_to_template

from dateutil import parser


class Session:
    devKey = "1403"  # devKey goes here
    authKey = "621263D5C3CE480AAE3814EDCCDA7AC8"  # authKey goes here
    timestamp = ""
    urlPrefix = "http://api.smitegame.com/smiteapi.svc/";
    signature = ""
    session = ""

    def generate_signature(self):
        self.signature = generate_MD5_Hash((self.devKey + "createsession" + self.authKey + self.timestamp))

    def generate_session_url(self):
        return self.urlPrefix + "createsessionjson/" + self.devKey + "/" + self.signature + "/" + self.timestamp


class Player:
    def __init__(self, kills_player, assists, deaths, playerName, final_match_level,
                 gold_earned, Refrence_name, item_Active1, item_Active2, item_Purch_1, item_Purch_2,
                 item_Purch_3, item_Purch_4, item_Purch_5, item_Purch_6):
        self.kills_player = kills_player
        self.assists = assists
        self.deaths = deaths
        if "[" in playerName:
            playerName_without_team = re.search("\[.*\](.*)", playerName).group(1)
            self.playerName = playerName_without_team
        else:
            self.playerName = playerName
        self.final_match_level = final_match_level
        self.gold_earned = gold_earned
        self.Reference_Name = Refrence_name.replace("_", " ")
        self.item_Active_1 = item_Active1
        self.item_Active_2 = item_Active2
        self.item_Purch_1 = item_Purch_1
        self.item_Purch_2 = item_Purch_2
        self.item_Purch_3 = item_Purch_3
        self.item_Purch_4 = item_Purch_4
        self.item_Purch_5 = item_Purch_5
        self.item_Purch_6 = item_Purch_6

class Team:

    def __init__(self, name, score, win_status, bans):
        self.players = []
        self.gold = int(0)
        self.total_kills = int(0)
        self.total_deaths = int(0)
        self.total_assists = int(0)
        self.name = name
        self.score = score
        self.win_status = win_status
        self.bans = bans


class Match:
    signature = ""


    def __init__(self, session, matchID, game_name, team1, team2, blue_score, red_score, blue_towers, blue_phoenixes, red_towers, red_phoenixes, tournament_name, daylight_savings_time):
        self.daylight_savings_time = daylight_savings_time
        self.tournament_name = tournament_name
        self.game_name = game_name
        self.matchID = matchID
        self.blue_towers = blue_towers
        self.blue_phoenixes = blue_phoenixes
        self.red_towers = red_towers
        self.red_phoenixes = red_phoenixes
        self.signature = generate_MD5_Hash(
            session.devKey + "getmatchdetails" + session.authKey + session.timestamp)
        match_request = urllib.request.urlopen(
            session.urlPrefix + "getmatchdetailsjson/" + session.devKey + "/" + self.signature + "/" + session.session + "/" + session.timestamp + "/" + matchID)
        match_return = match_request.read().decode("utf-8")
        match_json = json.loads(match_return)

        team1_bans = []
        team2_bans = []
        team1_bans.append(match_json[0].get("Ban1").replace("_", " "))
        team2_bans.append(match_json[0].get("Ban2").replace("_", " "))
        team1_bans.append(match_json[0].get("Ban3").replace("_", " "))
        team2_bans.append(match_json[0].get("Ban4").replace("_", " "))
        team1_bans.append(match_json[0].get("Ban5").replace("_", " "))
        team2_bans.append(match_json[0].get("Ban6").replace("_", " "))
        team1_Win_Status = match_json[0].get("Win_Status")
        team2_Win_Status =match_json[5].get("Win_Status")
        self.team1 = Team(team1, red_score, team1_Win_Status, team1_bans)
        self.team2 = Team(team2, blue_score, team2_Win_Status, team2_bans)
        test = parser.parse(match_json[0].get("Entry_Datetime"))
        self.date_played = test.strftime("%m/%d/%Y")
        self.time_played = test.strftime("%H:%M")
        self.duration = match_json[0].get("Minutes")

        for i in range(0,5):
            player = match_json[i]
            kills_player = player.get("Kills_Player")
            assists = player.get("Assists")
            deaths = player.get("Deaths")
            playerName = player.get("playerName")
            final_match_level = player.get("Final_Match_Level")
            gold_earned = player.get("Gold_Earned")
            Reference_Name = player.get("Reference_Name")
            item_Active_1 = player.get("Item_Active_1")
            item_Active_2 = player.get("Item_Active_2")
            item_Purch_1 = player.get("Item_Purch_1")
            item_Purch_2 = player.get("Item_Purch_2")
            item_Purch_3 = player.get("Item_Purch_3")
            item_Purch_4 = player.get("Item_Purch_4")
            item_Purch_5 = player.get("Item_Purch_5")
            item_Purch_6 = player.get("Item_Purch_6")
            player_info = Player(kills_player, assists, deaths, playerName, final_match_level,
                   gold_earned, Reference_Name, item_Active_1, item_Active_2, item_Purch_1, item_Purch_2,
                   item_Purch_3, item_Purch_4, item_Purch_5, item_Purch_6)
            self.team1.players.append(player_info)

        for i in range(5,10): #I'm really lazy
            player = match_json[i]
            kills_player = player.get("Kills_Player")
            assists = player.get("Assists")
            deaths = player.get("Deaths")
            playerName = player.get("playerName")
            final_match_level = player.get("Final_Match_Level")
            gold_earned = player.get("Gold_Earned")
            Reference_Name = player.get("Reference_Name")
            item_Active_1 = player.get("Item_Active_1")
            item_Active_2 = player.get("Item_Active_2")
            item_Purch_1 = player.get("Item_Purch_1")
            item_Purch_2 = player.get("Item_Purch_2")
            item_Purch_3 = player.get("Item_Purch_3")
            item_Purch_4 = player.get("Item_Purch_4")
            item_Purch_5 = player.get("Item_Purch_5")
            item_Purch_6 = player.get("Item_Purch_6")
            player_info = Player(kills_player, assists, deaths, playerName, final_match_level,
                   gold_earned, Reference_Name, item_Active_1, item_Active_2, item_Purch_1, item_Purch_2,
                   item_Purch_3, item_Purch_4, item_Purch_5, item_Purch_6)
            self.team2.players.append(player_info)

        for player in self.team1.players:
            self.team1.gold += int(player.gold_earned)
            self.team1.total_kills += int(player.kills_player)
            self.team1.total_assists += int(player.assists)
            self.team1.total_deaths += int(player.deaths)

        for player in self.team2.players:
            self.team2.gold += player.gold_earned
            self.team2.total_kills += player.kills_player
            self.team2.total_assists += player.assists
            self.team2.total_deaths += player.deaths




def generate_MD5_Hash(input):
    hash = hashlib.md5()
    hash.update(input.encode('utf-8'))
    return hash.hexdigest()


def spider(matchID, game_name, team1, team2, red_score, blue_score, blue_towers, blue_phoenixes, red_towers, red_phoenixes, tournament_name, daylight_savings_time):

    s = Session()
    s.timestamp = datetime.datetime.strftime(datetime.datetime.utcnow(), '%Y%m%d%H%M%S')
    s.generate_signature()
    session_request = urllib.request.urlopen(s.generate_session_url())
    session_return = session_request.read().decode("utf-8")
    session_json = json.loads(session_return)
    s.session = session_json["session_id"]
    match = Match(s, matchID, game_name, team1, team2, red_score, blue_score, blue_towers, blue_phoenixes, red_towers, red_phoenixes, tournament_name, daylight_savings_time)
    template = convert_to_template.convert_match_to_template(match)
    return template