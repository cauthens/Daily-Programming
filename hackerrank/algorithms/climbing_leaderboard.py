# 6 - 5 - 2017
# https://www.hackerrank.com/challenges/climbing-the-leaderboard

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
score_set = [scores[0]]
y = scores[0]
for x in scores:
    if x != y:
        score_set.append(x)
        y = x
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
# your code goes here

for a0 in alice:
    rank = 1
    for score in score_set:
        if a0 == score:
            print(score_set.index(a0)+1)
            break
        elif a0 < score:
            rank += 1
        elif a0 > score:
            print(rank)
            break
    else:
        print(rank)
    score_set = score_set[:rank-1]
