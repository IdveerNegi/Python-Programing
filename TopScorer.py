# Sorting the top scorer player.

from collections import defaultdict
def orangecap(match):
    top_score = defaultdict(int)
    for player in match:
        for top_scores in match[player]:
            top_score[top_scores] += match[player][top_scores]
    x = sorted(top_score.items(), key=lambda x: x[1], reverse=True)
    return x[0]

d =orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
print(d)

              
