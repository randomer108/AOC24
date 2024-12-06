import re
import pandas as pd
import numpy as np

data = list(open("./data/day5.txt"))

orderings = [re.sub('\n','',x) for x in data if re.findall('\|',x)!=[]]
orderings = [[int(re.findall(r'(\d+)\|',x)[0]),int(re.findall(r'\|(\d+)',x)[0])] for x in orderings]

pages = [re.sub('\n','',x) for x in data if re.findall('\|',x)==[]][1:]
pages = [x.split(',') for x in pages]
pages = [[int(x) for x in page] for page in pages]



correct = []
correct_middles = []
for page in pages:
    booly = True
    rules = [x for x in orderings if x[0] in page and x[1] in page]

    for rule in rules:
        if page.index(rule[1])<=page.index(rule[0]):
            booly=False
    if booly: correct.append(page)
    if booly: correct_middles.append(page[len(page)//2])

print(sum(correct_middles))

#2
wrong = [x for x in pages if x not in correct]
corrected=[]
for page in wrong:
    rules = [x for x in orderings if x[0] in page and x[1] in page]

    page2 = page.copy() # The page we'll edit
    page_check=[]

    while page2 !=page_check:
        page_check=page2.copy() # Update page to the last version of page2,to see if page 2 changes in this iteration.
        for rule in rules:
            if page2.index(rule[1])<=page2.index(rule[0]):
                page2[page2.index(rule[0])] = rule[1]
                page2[page2.index(rule[1])] = rule[0]
        
    corrected.append(page2[len(page2)//2])

print(sum(corrected))