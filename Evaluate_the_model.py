# Evaluate the model on the games_tourney_test dataset
print(model.evaluate(games_tourney_test[['home','seed_diff','prediction']],
games_tourney_test['score_diff'],
verbose=False))