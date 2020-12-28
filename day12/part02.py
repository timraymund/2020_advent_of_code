#! /usr/bin/env python3

import sys
import math

class Nav:
    def __init__(self):
        self.position = [0, 0] # initial ship east north
        self.waypoint = [10, 1] # initial way point east north (relative to ship)
        self.start = [0, 0] # initial position east north
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
                self.waypoint[1] += value
            elif cmd == 'S': # move east
                self.waypoint[1] -= value
            elif cmd == 'E': # move east
                self.waypoint[0] += value
            elif cmd == 'W': # move west
                self.waypoint[0] -= value
            elif cmd == 'L' or cmd == 'R': # rotate left or right
                if value == 0:
                    newE = self.waypoint[0] # east gets east
                    newN = self.waypoint[1] # north gets north
                elif (cmd == 'L' and value == 90) or (cmd == 'R' and value == 270):
                    newE = -self.waypoint[1] # east gets negative north
                    newN =  self.waypoint[0] # north gets east
                elif value == 180:
                    newE = -self.waypoint[0] # east gets negative north
                    newN = -self.waypoint[1] # north gets negative east
                elif (cmd == 'L' and value == 270) or (cmd == 'R' and value == 90):
                    newE =  self.waypoint[1] # east gets north
                    newN = -self.waypoint[0] # north gets negative east
                else:
                    print("Invalid rotation: ", cmd, value)
                    newE = self.waypoint[0] # east gets east
                    newN = self.waypoint[1] # north gets north
                
                # assign the new values
                self.waypoint[0] = newE
                self.waypoint[1] = newN
            elif cmd == 'F':
                self.position[0] += self.waypoint[0] * value
                self.position[1] += self.waypoint[1] * value
            else: 
                print("invalid action: ", cmd, value)
        
            # diagnostic
            print(cmd, value, self.position, self.waypoint)

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
