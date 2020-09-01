# Using Python 3
# https://open.kattis.com/problems/pet

if __name__ == "__main__":

    contestant_scores = [list()]*5
    for i in range(5):
        contestant_scores[i] = [int(x) for x in input().split(" ")]

    scores = [sum(lst) for lst in contestant_scores]
    winner = scores.index(max(scores))

    print(winner+1, scores[winner])
