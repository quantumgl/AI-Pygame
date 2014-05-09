# score_manager.py
#Score Manager

ENEMY_SCORE = 300
RUPEE_SCORE = 500

scores = {
    "ENEMY": ENEMY_SCORE,
    "RUPEE": RUPEE_SCORE
}


def calculate_score(score_type):
    return scores[score_type]






