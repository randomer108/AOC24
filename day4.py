import re
import pandas as pd

data = list(open("./data/day4.txt"))
data_rev = [line[::-1] for line in data]
data_down = []
for

def searchList(list):
    finds = re.findall(r'XMAS',str(list))
    return(len(finds))

answer=0
for line in data:
    answer +=searchList(line)

print(answer)