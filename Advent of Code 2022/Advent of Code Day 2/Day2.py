#The winner of the whole tournament is the player with the highest score. 
#Your total score is the sum of your scores for each round. 
#The score for a single round is the score for the shape you selected 
#(1 for Rock, 2 for Paper, and 3 for Scissors) 
#plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

with open(r'C:\Users\cneukuckatz\OneDrive - ISACA\Documents\CNEUK GH Repo\Advent of Code 2022\Advent of Code Day 2\Day2 ') as f:
    rounds = f.read().split('\n')

def AOC_2022_day2_pt1(rounds):
    outcomes = {'A X': 3 + 1, 'A Y': 6 + 2, 'A Z': 0 + 3, 
                'B X': 0 + 1, 'B Y': 3 + 2, 'B Z': 6 + 3, 
                'C X': 6 + 1, 'C Y': 0 + 2, 'C Z': 3 + 3}
    score = sum(outcomes[i] for i in rounds)
    return score

def AOC_2022_day2_pt2(rounds):
    outcomes = {'A X': 0 + 3, 'A Y': 3 + 1, 'A Z': 6 + 2, 
                'B X': 0 + 1, 'B Y': 3 + 2, 'B Z': 6 + 3, 
                'C X': 0 + 2, 'C Y': 3 + 3, 'C Z': 6 + 1}
    score = sum(outcomes[i] for i in rounds)
    return score

print(AOC_2022_day2_pt1(rounds))
print(AOC_2022_day2_pt2(rounds))

    