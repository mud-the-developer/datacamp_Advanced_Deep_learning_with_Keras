# Predict
games_tourney['pred'] = model.predict([games_tourney['team_1'],
games_tourney['team_2'],
games_tourney['home']])