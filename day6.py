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

        self.history_orientation=[(self.x,self.y,self.direction)]
        self.loopyloos = []

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

    def castClairvoyance(self):
        if self.the_view=='.':  # ignore ^ as it says to ignore start position
            direction_temp = (self.direction +90)%360
            if direction_temp==0:
                next_temp = [self.x,self.y-1]
            if direction_temp==90:
                next_temp = [self.x+1,self.y]
            if direction_temp==180:
                next_temp = [self.x,self.y+1]
            if direction_temp==270:
                next_temp = [self.x-1,self.y]

            temp_position = (next_temp[1],next_temp[0],direction_temp)
            if temp_position in self.history_orientation:
                 self.loopyloos.append((self.next[0],self.next[1]))
                



    def action(self):
        if self.the_view=='.' or self.the_view=='^':
            self.move()
            self.history.append((self.x,self.y))
            self.history_orientation.append((self.x,self.y,self.direction))


        if self.the_view =='#':
            self.direction = (self.direction +90)%360
            self.history.append((self.x,self.y))
            self.history_orientation.append((self.x,self.y,self.direction))

    
    def move(self):
        self.x=self.next[0]
        self.y=self.next[1]

    def check_done(self):
        if self.x==0 or self.x== len(data[0])-1 or self.y==0 or self.y==len(data)-1:
            self.keepOnWalking=False



start = tuple(np.argwhere(data=='^')[0])
guard = pointer(start[1],start[0])


while guard.keepOnWalking:
    guard.scan()
    guard.castClairvoyance() 
    guard.action()
    guard.check_done()

print(len(set(guard.history)))

#2

print(f' The number of scary loops is: {len(set(guard.loopyloos))}')
print(set(guard.loopyloos))