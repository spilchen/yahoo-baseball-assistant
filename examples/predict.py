#!/bin/python

"""Predict the stats for the players currently on your roster

Usage:
  predict.py <json> <week>

  <json>  The name of the JSON that has bearer token.  This can be generated
          from init_oauth_env.py.
  <week>  Week number to predict for.
"""
from docopt import docopt
from yahoo_oauth import OAuth2
from yahoo_fantasy_api import league, game, team
from yahoo_baseball_assistant import hitting


if __name__ == '__main__':
    args = docopt(__doc__, version='1.0')
    sc = OAuth2(None, None, from_file=args['<json>'])
    gm = game.Game(sc, 'mlb')
    league_id = gm.league_ids(year=2019)
    lg = league.League(sc, league_id[0])
    team_key = lg.team_key()
    my_tm = team.Team(sc, team_key)
    bldr = hitting.Builder()
    df = bldr.roster_predict(my_tm.roster(args['<week>']))
    print(df)
