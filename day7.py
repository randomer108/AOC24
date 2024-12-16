import re
import numpy as np
from itertools import product

data = list(open("./data/day7.txt"))
correct = []

def check(d):
    check = False
    answer= int(re.findall(r'(\d*):',d)[0])
    numbers = re.sub(r'\d*: ','',d).split(' ')
    numbers = [int(x) for x in numbers]
    options = list(product(['0', '1','2'], repeat=len(numbers)))

    for Op in options:
        A=0
        for n,op in zip(numbers,Op):
            if op =='0':
                A=A+n
            if op =='1':
                A=A*n
            if op =='2':
                A = str(A)
                n = str(n)
                A = int(A+n)
        if A ==answer:
            correct.append(answer)
            break

for d in data:
    check(d)

print(sum(correct))




    


