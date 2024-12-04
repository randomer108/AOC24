import re
import pandas as pd
from itertools import combinations
data = list(open("./data/day2.txt"))

data= [re.findall(r'(\d+)\s*',line) for line in data]



def check(row):
    d=list(map(int,row))
    diffs = [j-i for i, j in zip(d[:-1], d[1:])]
    ans = 0
    if all(x < 0 for x in diffs) and min(diffs)>-4:
        ans = 1

    if all(x > 0 for x in diffs) and max(diffs)<4:
        ans=1

    return(ans)

answers = [check(line) for line in data]
print(sum(answers))


def checksubsets(row):
    
    row=list(map(int,row))
    rows=list(combinations(row, len(row) - 1))

    ans=0
    for row in rows:
        ans=max(ans,check(row))
    return(ans)

answers2 = [checksubsets(line) for line in data]
print(sum(answers2))