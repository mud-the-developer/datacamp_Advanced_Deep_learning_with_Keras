# Evaluate the model on the tournament test data
print(model.evaluate(games_tourney_test[['seed_diff','pred']], games_tourney_test[['score_1','score_2']], verbose=False))