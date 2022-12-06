from collections import Counter
with open(r'C:\Users\cneukuckatz\OneDrive - ISACA\Documents\CNEUK GH Repo\Advent of Code 2022\Advent of Code Day 3\Day3.txt') as f:
    rounds = f.read().split('\n')
    count = 0
    for line in rounds:
        words = line.split(" ")
        count += len(words)
    print (rounds)
    
    #lc = 'abcdefghijklmnopqrstuvwxyz'
    #uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #count_let = max(lc, key = rounds.count)
    
    
