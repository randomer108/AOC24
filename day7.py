import re
import numpy as np

data = list(open("./data/day7.txt"))
correct = []

def check(d):
    check = False
    answer= int(re.findall(r'(\d*):',d)[0])
    numbers = re.sub(r'\d*: ','',d).split(' ')
    numbers = [int(x) for x in numbers]
    options = [list(format(i, f'0{len(numbers)}b')) for i in range(2**len(numbers))]

    for Op in options:
        A=0
        for n,op in zip(numbers,Op):
            if op =='0':
                A=A+n
            if op =='1':
                A=A*n
        if A ==answer:
            correct.append(answer)
            break


for d in data:
    check(d)

print(sum(correct))



