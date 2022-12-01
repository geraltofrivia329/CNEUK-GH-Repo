#cal = open(r'C:\Users\cneukuckatz\OneDrive - ISACA\Documents\CNEUK GH Repo\Advent of Code 2022\Day1.txt','r') 
#for c in cal.readlines():
    #print(c, end = '')
#for c in cal.readlines():
calorieList = []
with open(r'C:\Users\cneukuckatz\OneDrive - ISACA\Documents\CNEUK GH Repo\Advent of Code 2022\Day1.txt') as file1:
    tempSum = 0
    while True:
        line = file1.readline()
        if line == '':
            calorieList.append(tempSum)
            break
        elif line == '\n':
            calorieList.append(tempSum)
            tempSum = 0
        else:
            line = line.strip('\n')
            tempSum += int(line)

calorieList.sort()
print('Part 1 ->', calorieList[-1])
print('Part 2 ->', sum(calorieList[-3:]))