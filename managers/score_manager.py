# score_manager.py
#Score Manager

ENEMY_SCORE = 300
RUPEE_SCORE = 500

scores = {
    "ENEMY": ENEMY_SCORE,
    "RUPEE": RUPEE_SCORE,
}

my_scores = {
    "ENEMY": 300,
    "MONEY": 1000,
    "LASER": 1000,
    "HP": 200,
    "DEFENSE": 100
}


def calculate_score(score_type):
    return my_scores[score_type]






