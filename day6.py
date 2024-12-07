import re
import pandas as pd
import numpy as np

data = list(open("./data/day6.txt"))
data = [re.sub(r'\n','',x).split() for x in data]
data=[list(x[0]) for x in data]
data = np.array(data)



class pointer:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.direction=0
        self.history=[(self.x,self.y)]
        self.keepOnWalking=True
        self.next=None
        self.the_view =None

    def scan(self):
        if self.direction==0:
            self.next = [self.x,self.y-1]
        if self.direction==90:
            self.next = [self.x+1,self.y]
        if self.direction==180:
            self.next = [self.x,self.y+1]
        if self.direction==270:
            self.next = [self.x-1,self.y]
    
        self.the_view = data[self.next[1],self.next[0]]


    def action(self):
        if self.the_view=='.' or self.the_view=='^':
            self.history.append((self.x,self.y))
            self.move()
        if self.the_view =='#':
            self.direction = (self.direction +90)%360

    
    def move(self):
        self.x=self.next[0]
        self.y=self.next[1]

    def check_done(self):
        if self.x==0 or self.x== len(data[0]) or self.y==0 or self.y==len(data)-1:
            self.keepOnWalking=False



start = tuple(np.argwhere(data=='^')[0])
guard = pointer(start[1],start[0])

while guard.keepOnWalking:
    guard.scan()
    guard.action()
    #print(f'saw {guard.the_view}, went {guard.direction} now at {guard.x},{guard.y}')
    guard.check_done()


print(len(set(guard.history))+1)
