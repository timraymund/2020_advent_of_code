#! /usr/bin/env python3

import sys
import math
import re

class Seat:
    def __init__(self):
        self.maxID = -1     # maximum row*8 + seat
        self.rowseats = []  # data read in
        self.p = re.compile('[^FB]')
        self.IDs = []
    
    def loadPasses(self, line):
        self.rowseats.append(line.strip('\n'))

    def findMaxID(self):
        for rs in self.rowseats:
            m = self.p.search(rs)
            if m:
                r = rs[:m.start()]
                s = rs[m.start():]
            else:
                r = rs
                s = ''
            # print(r, s)

            rl = list(r)
            rMin = 0
            rMax = 127
            rv = math.floor((rMin + rMax) / 2)
            for c in rl:
                if c == 'F':
                    rMax = rv
                elif c == 'B':
                    rv += 1
                    rMin = rv
                else:
                    print("what row is this? ",c)
                
                rv = math.floor((rMin + rMax) / 2)
            rv = rMin
            
            sl = list(s)
            sMin = 0
            sMax = 7
            sv = math.floor((sMin + sMax) / 2)
            for c in sl:
                if c == 'L':
                    sMax = sv
                elif c == 'R':
                    sv += 1
                    sMin = sv
                else:
                    print("what seat is this? ", c)
                
                sv = math.floor((sMin + sMax) / 2)
            sv = sMin

            currentID = rv * 8 + sv
            # print(rv, sv, currentID)
            if currentID > self.maxID:
                self.maxID = currentID
            
            self.IDs.append(currentID)

        return self.maxID

    def findSeatID(self):
        self.IDs.sort()
        pID = self.IDs[0]
        for cID in self.IDs:
            if cID - pID == 2:
                break
            else:
                pID = cID
        
        return pID+1

def main():
    fileName = 'sample_data.txt'
    if len(sys.argv) > 1:
        fileName = sys.argv[1]

    seat = Seat()

    with open(fileName, 'r') as df:
        for line in df:
            seat.loadPasses(line)

    # produce results
    print(seat.findMaxID())

    print(seat.findSeatID())

if __name__ == '__main__':
    # run this file as a script
    main()

