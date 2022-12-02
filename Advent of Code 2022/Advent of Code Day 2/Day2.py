#The winner of the whole tournament is the player with the highest score. 
#Your total score is the sum of your scores for each round. 
#The score for a single round is the score for the shape you selected 
#(1 for Rock, 2 for Paper, and 3 for Scissors) 
#plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

A = 1
B = 2
C = 3
X = "Rock"
Y = "Paper"
Z = "Scissors" 
shape = A or B or C 
Lost = 0 
Draw = 3 
Won = 6 
outcome = Won or Draw or Lost 

total_score = shape + outcome
rps = []
with open(r'C:\Users\cneukuckatz\OneDrive - ISACA\Documents\CNEUK GH Repo\Advent of Code 2022\Advent of Code Day 2\Day2 .txt') as file1:
    while True:
        line = file1.readline()
        shape + outcome
        print (total_score)
        break

    