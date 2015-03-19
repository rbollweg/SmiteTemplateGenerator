__author__ = 'The Gibs'

import re
import time
import datetime


def convert_match_to_template(match):
    template = str()
    header = "{{Scoreboard|" + match.team1.name + "|" + match.team2.name + "\n" + "|" + match.game_name + "={{Scoreboard/Game"

    teams = "|team1=" + match.team1.name + "|team2=" + match.team2.name
    winner = "|winner="
    if match.team1.win_status == "Winner":
        winner += "1"
    else:
        winner += "2"
    scores = "|t1score="
    if match.team1.score:
        scores += match.team1.score
    else:
        if match.team1.win_status == "Winner":
            scores += "1"
        else:
            scores += "0"
    scores += "|t2score="
    if match.team2.score:
        scores += match.team2.score
    else:
        if match.team2.win_status == "Winner":
            scores += "1"
        else:
            scores += "0"


    tournament_name = "|tournament=" + match.tournament_name
    date = "|date=" + match.date_played + "|GMT=" + match.time_played
    vod_link = "|vodlink="
    stats_link = "|statslink=https://account.hirezstudios.com/smitegame/match-details.aspx?match=" + match.matchID
    picks_and_bans_page = "|picksandbanspage="

    team1bans = str()
    for i in range(0, match.team1.bans.__len__()):
        team1bans += "|t1b" + str(i + 1) + "=" + match.team1.bans[i]
    team2bans = str()
    for i in range(0, match.team2.bans.__len__()):
        team2bans += "|t2b" + str(i + 1) + "=" + match.team2.bans[i]

    duration = "|gamelength=" + str(match.duration) + ":00"
    DST = "|dst=" + match.daylight_savings_time
    #To Do: Add PST

    team1_stats = "|t1k=" + str(match.team1.total_kills) + "|t1t=" + match.blue_towers + "|t1p=" + match.blue_phoenixes + "|t1g=" + str(match.team1.gold)
    team2_stats = "|t2k=" + str(match.team2.total_kills) + "|t2t=" + match.red_towers + "|t2p=" + match.red_phoenixes + "|t2g=" + str(match.team2.gold)

    team1_players = str()
    for i in range(0, match.team1.players.__len__()):
        player_string = convert_player_info_to_template("blue", i, match.team1.players[i])
        team1_players += player_string + '\n'
    team2_players = str()
    for i in range(0, match.team2.players.__len__()):
        player_string = convert_player_info_to_template("red", i, match.team2.players[i])
        team2_players += player_string + '\n'

    footer = "}}\n}}"

    template += header + "\n" + teams + winner + scores + "\n" + tournament_name + date + DST + "\n" + vod_link + "\n" + stats_link + "\n" + picks_and_bans_page + "\n" + team1bans + "\n" + team2bans + "\n" + duration + "\n" + team1_stats + "\n" + team2_stats + "\n" + team1_players + team2_players + footer
    return template


def convert_player_info_to_template(team_color, player_number, player):
    player_intro = "|" + team_color + str(player_number + 1) + "={{Scoreboard/Player|name=" + player.playerName + "|god=" + player.Reference_Name
    player_match_stats = "|level=" + str(player.final_match_level) + "|k=" + str(player.kills_player) + "|d=" + str(player.deaths) + "|a=" + str(player.assists) + "|gold=" + str(player.gold_earned)
    player_actives = "|active1=" + player.item_Active_1 + "|active2=" + player.item_Active_2
    player_items = "|item1=" + player.item_Purch_1 + "|item2=" + player.item_Purch_2 + "|item3=" + \
                   player.item_Purch_3 + "|item4=" + player.item_Purch_4 + "|item5=" + player.item_Purch_5 + "|item6=" + player.item_Purch_6
    player_string = player_intro + player_match_stats + player_actives + player_items + " }}"
    return player_string
