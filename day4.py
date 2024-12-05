import re
import pandas as pd
import numpy as np

data = list(open("./data/day4.txt"))
data = [re.sub(r'\n','',x) for x in data]
data = np.array(data)

answer=0 
for row,ROW in enumerate(data): 
    ROW=str(ROW)
    for col,element in enumerate(ROW):
        if element == 'X':
            # Right
            if col<137:
                if data[row][col+1]=='M' and data[row][col+2]=='A' and data[row][col+3]=='S':
                    answer+=1

            # Left
            if col>2:
                if data[row][col-1]=='M' and data[row][col-2]=='A' and data[row][col-3]=='S':
                    answer+=1
            
            # Up
            if row>2:
                if data[row-1][col]=='M' and data[row-2][col]=='A' and data[row-3][col]=='S':
                    answer+=1
            # Down
            if row<137:
                if data[row+1][col]=='M' and data[row+2][col]=='A' and data[row+3][col]=='S':
                    answer+=1
            
            #diag_right up
            if col<137 and row>2:
                if data[row-1][col+1]=='M' and data[row-2][col+2]=='A' and data[row-3][col+3]=='S':
                    answer+=1

             #diag right down
            if col<137 and row<137:
                if data[row+1][col+1]=='M' and data[row+2][col+2]=='A' and data[row+3][col+3]=='S':
                    answer+=1

            #diag left down
            if col>2 and row<137:
                if data[row+1][col-1]=='M' and data[row+2][col-2]=='A' and data[row+3][col-3]=='S':
                    answer+=1

            #diag left up
            if col>2 and row>2:
                if data[row-1][col-1]=='M' and data[row-2][col-2]=='A' and data[row-3][col-3]=='S':
                    answer+=1
print(answer)

# 2
answer=0 
# Imagine picking an A and going clockwise from top right, collecting the corners around the A. You'll get 4 elements: i,j,k,l.
# Only certain combos of i,j,k,l are valid, in that they will make an X-mas.
# (pen and paper - note that the order needs to be MMSS or a "shift" of that like SMMS. Cannot be SMSM as that would spell {SAS + MAM} instead of {MAS/SAM + MAS/SAM})
valid= [['M','M','S','S'],
        ['M','S','S','M'],
        ['S','S','M','M'],
        ['S','M','M','S'],
        ]

for row,ROW in enumerate(data): 
    for col,element in enumerate(ROW):
        if element == 'A':
            if col>0 and col<139 and row>0 and row<139:
                # go clockwise from top right getting the corers around the A.
                i = data[row-1][col+1]
                j = data[row+1][col+1]
                k = data[row+1][col-1]
                l = data[row-1][col-1]
                
                if [i,j,k,l] in valid:
                    answer+=1             #diag right down
           
print(answer)