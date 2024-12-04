import re
import pandas as pd
from itertools import combinations
data = list(open("./data/day3.txt"))

string=''.join(data)


mulls= re.findall(r'mul\(\d+,\d+\)',string)
nums= [list(map(int,re.findall(r'(\d+)',line))) for line in mulls]

prods = [n[0]*n[1] for n in nums]
print(sum(prods))

# 2
mullDoDont= re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)',string)

answer2 = 0
On=True
for command in mullDoDont:
    if command == "do()":
        On=True
    if command == "don\'t()":
        On =False

    if On and re.search('mul',command)!=None:
        nums = list(map(int,re.findall(r'(\d+)',command)))
        answer2 +=nums[0]*nums[1] 
        
print("Answer 2: " +str(answer2))