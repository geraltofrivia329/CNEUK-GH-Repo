# Day 4 pairs. 2-4 = 234 and 6-8 = 678
# In How many assignment pairs does one range fully contain the other?
import re
with open((r'C:\Users\cneukuckatz\OneDrive - ISACA\Documents\CNEUK GH Repo\Advent of Code 2022\Advent of Code Day 4\Day4.txt')) as f:
     x = list(filter(None, f.read().split('\n')))  
     y = re.findall('[0-9]', x)
     print (y)
     #for i in range (0, len(x)):
           #x[i] = int(x[i])
     #print (x)
     #y = x[1].split()
     #print(y)
     #for i in range(len(x)):
        #x[i] = int(x[i])
        #print(x)