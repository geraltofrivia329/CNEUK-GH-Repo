# Day 4 pairs. 2-4 = 234 and 6-8 = 678
# In How many assignment pairs does one range fully contain the other?

x = open(r"C:\Users\cneukuckatz\OneDrive - ISACA\Documents\CNEUK GH Repo\Advent of Code 2022\Advent of Code Day 4\Day4.txt", "r").read().splitlines()


t = 0


for i in x:

    a,b=i.split(",")

    aa, aaa = [int(r) for r in a.split("-")]
    bb, bbb = [int(r) for r in b.split("-")]


    if (aa <= bb and aaa >= bbb ) or (bb<=aa and bbb>=aaa):
        t+=1


print(t)
     