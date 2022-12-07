with open((r'C:\Users\cneukuckatz\OneDrive - ISACA\Documents\CNEUK GH Repo\Advent of Code 2022\Advent of Code Day 3\Day3.txt')) as f:
    rucksacks = list(filter(None, f.read().split('\n')))  

priority_sum, groups_priority_sum = 0, 0    

# Part 1
for rucksack in rucksacks: 
    compartment_a,compartment_b  = rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):] 
    common_item = [i for i in compartment_a
    if i in compartment_b][0] 
    priority_sum += ord(common_item) - (38 if common_item.isupper() else 96)


# Part 2
for i in range(0, len(rucksacks), 3): 
    elf_group = rucksacks[i:i+3] 
    badge = [x for x in elf_group[0] if x in elf_group[1] and x in elf_group[2]][0] 
    groups_priority_sum += ord(badge) - (38 if badge.isupper() else 96)

print("The sum of priority item values is: "+str(priority_sum)) 
print("The sum of groups' priority item values is: "+str(groups_priority_sum))
    #lc = 'abcdefghijklmnopqrstuvwxyz'
    #uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #x = rounds.count(lc)
    #count_let = max(lc, key = rounds.count)
    #print(x)
    
    
