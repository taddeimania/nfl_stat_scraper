import json
from django.db import models


class Season(models.Model):
    year = models.IntegerField()


class Team(models.Model):
    name = models.CharField(max_length=100)
    season = models.ForeignKey(Season)


class Player(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team)


class Stat(models.Model):

    def __str__(self):
        player_dict = {
            'player': self.player.name,
            'team': self.player.team.name,
            'season': self.player.team.season.year,
            'stats': self.__dict__
        }
        del player_dict['stats']['_state']
        del player_dict['stats']['_player_cache']
        return json.dumps(player_dict)

    player = models.ForeignKey(Player)
    games = models.IntegerField(default=0)
    games_started = models.IntegerField(default=0)
    rushes = models.IntegerField(default=0)
    rush_yards = models.IntegerField(default=0)
    average_rush = models.FloatField(default=0.0)
    long_rush = models.IntegerField(default=0)
    rush_touchdowns = models.IntegerField(default=0)
    rush_first_downs = models.IntegerField(default=0)
    stuff = models.IntegerField(default=0)
    yards_lost = models.IntegerField(default=0)
    fumbles = models.IntegerField(default=0)
    fumbles_lost = models.IntegerField(default=0)
    receptions = models.IntegerField(default=0)
    reception_yards = models.IntegerField(default=0)
    average_reception = models.FloatField(default=0.0)
    long_reception = models.IntegerField(default=0)
    reception_touchdowns = models.IntegerField(default=0)
    reception_first_downs = models.IntegerField(default=0)
    reception_yards_after_catch = models.IntegerField(default=0)
    reception_targets = models.IntegerField(default=0)
    kickoff_returns = models.IntegerField(default=0)
    kickoff_return_yards = models.IntegerField(default=0)
    kickoff_return_average = models.FloatField(default=0.0)
    kickoff_return_long = models.IntegerField(default=0)
    kickoff_return_touchdowns = models.IntegerField(default=0)
    punt_returns = models.IntegerField(default=0)
    punt_return_yards = models.IntegerField(default=0)
    punt_return_average = models.FloatField(default=0.0)
    punt_return_long = models.IntegerField(default=0)
    punt_return_fair_catches = models.IntegerField(default=0)
    punt_return_touchdowns = models.IntegerField(default=0)
    pass_completions = models.IntegerField(default=0)
    pass_attempts = models.IntegerField(default=0)
    pass_percentage = models.FloatField(default=0.0)
    pass_yards = models.IntegerField(default=0)
    pass_yards_per_attempt = models.FloatField(default=0.0)
    pass_touchdowns = models.IntegerField(default=0)
    pass_interceptions = models.IntegerField(default=0)
    pass_first_downs = models.IntegerField(default=0)
    pass_sacked = models.IntegerField(default=0)
    pass_rating = models.FloatField(default=0.0)
    one_to_twenty_nine = models.CharField(max_length=5, default='0-0')
    thirty_to_thirty_nine = models.CharField(max_length=5, default='0-0')
    forty_to_fourty_nine = models.CharField(max_length=5, default='0-0')
    fifty_plus = models.CharField(max_length=5, default='0-0')
    field_goals = models.CharField(max_length=5, default='0-0')
    extra_points = models.CharField(max_length=5, default='0-0')
    field_goal_percentage = models.FloatField(default=0.0)
    average_attempt = models.FloatField(default=0.0)
    average_miss = models.FloatField(default=0.0)
    field_goal_long = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    punts = models.IntegerField(default=0)
    punt_yards = models.IntegerField(default=0)
    punt_average = models.FloatField(default=0.0)
    punt_long = models.IntegerField(default=0)
    punt_in_twenty = models.IntegerField(default=0)
    punt_in_ten = models.IntegerField(default=0)
    punt_fair_catches = models.IntegerField(default=0)
    punt_touchbacks = models.IntegerField(default=0)
    punt_blocks = models.IntegerField(default=0)
    punts_returned = models.IntegerField(default=0)
    punts_returned_yards = models.IntegerField(default=0)
    punts_returned_touchdowns = models.IntegerField(default=0)
    punt_returned_net = models.FloatField(default=0.0)
    tackles = models.IntegerField(default=0)
    tackles_assist = models.IntegerField(default=0)
    sacks = models.FloatField(default=0.0)
    def_stuff = models.FloatField(default=0.0)
    forced_fumble = models.IntegerField(default=0)
    fumble_recover = models.IntegerField(default=0)
    pass_defended = models.IntegerField(default=0)
    interception = models.IntegerField(default=0)
    interception_yards = models.IntegerField(default=0)
    defensive_touchdowns = models.IntegerField(default=0)


class Page(models.Model):
    page = models.CharField(max_length=100)


stat_attr_map = {
    'Player': 'player',
    'Kicking_50+': 'fifty_plus',
    'Receiving_TD': 'reception_touchdowns',
    'Rushing_Yds Lost': 'yards_lost',
    'Punting_In 10': 'punt_in_ten',
    'Passing_Att': 'pass_attempts',
    'Passing_Pct': 'pass_percentage',
    'Rushing_Fm Lost': 'fumbles_lost',
    'G': 'games',
    'Kicking_XP-Att': 'extra_points',
    'Punting_Long': 'punt_long',
    'Defense_Stf': 'def_stuff',
    'Passing_Yards': 'pass_yards',
    'Kicking_1-29': 'one_to_twenty_nine',
    'Receiving_Target': 'reception_targets',
    'Rushing_TD': 'rush_touchdowns',
    'Kicking_30_39': 'thirty_to_thirty_nine',
    'Returns_Yards': 'kickoff_return_yards',
    'Defense_Int Yds': 'interception_yards',
    'Defense_FF': 'forced_fumble',
    'Kicking_40_49': 'forty_to_fourty_nine',
    'Punting_Net': 'punt_returned_net',
    'Passing_1st': 'pass_first_downs',
    'Passing_Int': 'pass_interceptions',
    'Rushing_Fmbl': 'fumbles',
    'Passing_TD': 'pass_touchdowns',
    'Rushing_Avg': 'average_rush',
    'Punting_Ret': 'punts_returned',
    'Passing_Rate': 'pass_rating',
    'Returns_KOR': 'kickoff_returns',
    'Defense_Int': 'interception',
    'Kicking_FG-Att': 'field_goals',
    'Kicking_Long': 'field_goal_long',
    'Receiving_Long': 'long_reception',
    'Punting_Yards': 'punts_returned_yards',
    'Returns_FC': 'punt_return_fair_catches',
    'Punting_In 20': 'punt_in_twenty',
    'Receiving_1st': 'reception_first_downs',
    'Defense_FR': 'fumble_recover',
    'Rushing_1st': 'rush_first_downs',
    'Passing_Comp': 'pass_completions',
    'Rushing_Long': 'long_rush',
    'GS': 'games_started',
    'Defense_PD': 'pass_defended',
    'Returns_Punt_Avg': 'punt_return_average',
    'Returns_PR': 'punt_returns',
    'Passing_Yards/Att': 'pass_yards_per_attempt',
    'Kicking_FG Pct': 'field_goal_percentage',
    'Receiving_Yards': 'reception_yards',
    'Punting_Punts': 'punts',
    'Returns_TD': 'kickoff_return_touchdowns',
    'Returns_Punt_TD': 'punt_return_touchdowns',
    'Returns_Avg': 'kickoff_return_average',
    'Rushing_Rush': 'rushes',
    'Defense_TD': 'defensive_touchdowns',
    'Rushing_Stuff': 'stuff',
    'Kicking_Avg Miss': 'average_miss',
    'Passing_Sacked': 'pass_sacked',
    'Receiving_Avg': 'average_reception',
    'Receiving_YAC': 'reception_yards_after_catch',
    'Rushing_Yards': 'rush_yards',
    'Returns_Long': 'kickoff_return_long',
    'Returns_Punt_Long': 'punt_return_long',
    'Defense_Sck': 'sacks',
    'Kicking_Points': 'points',
    'Punting_Avg': 'punt_average',
    'Punting_TB': 'punt_touchbacks',
    'Punting_FC': 'punt_fair_catches',
    'Punting_Blkd': 'punt_blocks',
    'Receiving_Rec': 'receptions',
    'Defense_Tk': 'tackles',
    'Punting_TD': 'punts_returned_touchdowns',
    'Returns_Punt_Yards': 'punt_return_yards',
    'Kicking_Avg Att': 'average_attempt',
    'Defense_Ast': 'tackles_assist'
}