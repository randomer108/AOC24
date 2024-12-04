import re
import pandas as pd
d = list(open("./data/day1.txt"))

L= [re.findall(r'(\d+)\s',line)[0]for line in d]
R= [re.findall(r'(\d+)',line)[1] for line in d]
L=sorted(map(int,L))
R=sorted(map(int,R))

ans=0
for l,r in zip(L, R):
    ans+=abs(l-r)

print(ans)

###2

ans2=0
for l in L:
    ans2+= l*R.count(l)

print(ans2)