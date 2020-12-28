#! /usr/bin/env python3

import sys
from operator import itemgetter
from math import gcd

class BusFinder:
    def __init__(self):
        self.earliestTime = 0
        self.soonestTIme = 0
        self.busIDs = []
        self.maxPlusTime = 0

    def loadEarliestTime(self,line):
        self.earliestTime = int(line.strip('\n'))
        self.soonestTime = self.earliestTime * 1000

    def loadBusIDs(self,line):
        tempIDs = []
        temp = (line.strip('\n')).split(',')
        plusTime = 0
        for id in temp:
            if id != 'x':
                tempIDs.append([int(id), plusTime])
            plusTime += 1
        self.busIDs = tempIDs # sorted(tempIDs, key=itemgetter(0))
        self.maxPlusTime = plusTime
        print(self.busIDs)

    def compute_lcm(self, a):
        lcm = a[0]
        for i in a[1:]:
            lcm = lcm * i // gcd(lcm, i)
        return lcm

    def findMagicTime(self):
        timestamp = 0
        matched_buses = [self.busIDs[0][0]]
        while True:
            timestamp += self.compute_lcm(matched_buses)
            # print(timestamp)
            for [id, plusTime] in self.busIDs:
                if (timestamp + plusTime) % id == 0:
                    if id not in matched_buses:
                        matched_buses.append(id)
            if len(matched_buses) == len(self.busIDs):
                break
        return timestamp

"""         # get the last bus
        [lastID, lastPlusTime] = self.busIDs[len(self.busIDs) - 1]

        # find the min mult factor (don't want smaller bus IDs at negative time)
        # take the last plusTime-1 / last bus id
        # initial mult factor is the result + 1
        minFactor = 1
        # current time is the mult factor * last bus id
        currentTime = minFactor * lastID

        found = False
        while not found:
            found = True
            # iterate backwards through the list of busIDs
            for i in range(len(self.busIDs)-2,-1,-1):
                [id, plusTime] = self.busIDs[i]
                # testTime = last bus plusTime - bus id plusTime
                testTime = currentTime - (lastPlusTime - plusTime)
                # if testTime mod bus id is not zero
                if testTime < 0 or testTime % id != 0:
                    found = False
                    # increment the mult factor
                    minFactor += 1
                    # current time is the mult factor * last bus id
                    currentTime = minFactor * lastID
                    break
        
        # everyone is happy
        return currentTime - lastPlusTime """


def main():
    bf = BusFinder()

    dataFile = 'sample.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    
    with open(dataFile, 'r') as df:
        bf.loadEarliestTime(df.readline())
        for line in df:
            bf.loadBusIDs(line)
            print(bf.findMagicTime())

if __name__ == '__main__':
    # run this file as a standalone script
    main()
