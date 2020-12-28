#! /usr/bin/env python3

import sys
import math

class Nav:
    def __init__(self):
        self.position = [0,0] # east, north
        self.orientation = 90 # facing east
        self.start = [0,0] # east, north
        self.actions = []

    def loadAction(self,line):
        action = line.strip('\n')
        cmd = action[:1]
        value = int(action[1:])
        self.actions.append([cmd,value])

    def drive(self):
        # for each action
        for [cmd, value] in self.actions:
            if cmd == 'N': # move north
                self.position[1] += value
            elif cmd == 'S': # move east
                self.position[1] -= value
            elif cmd == 'E': # move east
                self.position[0] += value
            elif cmd == 'W': # move west
                self.position[0] -= value
            elif cmd == 'L': # rotate left
                self.orientation -= value
                self.orientation = self.orientation % 360
            elif cmd == 'R': # rotate right
                self.orientation += value
                self.orientation = self.orientation % 360
            elif cmd == 'F':
                self.position[0] += int(math.sin(math.radians(self.orientation)) * value)
                self.position[1] += int(math.cos(math.radians(self.orientation)) * value)
            else: 
                print("invalid action: ", cmd, value)
        
            # diagnostic
            print(cmd, value, self.position)

    def getPosition(self):
        return self.position
    
    def getDistance(self):
        distance = abs(self.position[0] - self.start[0]) + abs(self.position[1] - self.start[1])
        return distance

def main():
    nav = Nav()

    dataFile = 'sample.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    with open(dataFile,'r') as df:
        for line in df:
            nav.loadAction(line)

    # do something else
    nav.drive()

    print(nav.getDistance())

if __name__ == '__main__':
    # run this file as a standalone script
    main()
