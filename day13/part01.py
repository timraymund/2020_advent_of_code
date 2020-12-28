#! /usr/bin/env python3

import sys

class BusFinder:
    def __init__(self):
        self.earliestTime = 0
        self.busIDs = []
        self.soonestTime = 0
        self.soonestBus = 0

    def loadEarliestTime(self,line):
        self.earliestTime = int(line.strip('\n'))
        self.soonestTime = self.earliestTime * 1000

    def loadBusIDs(self,line):
        temp = (line.strip('\n')).split(',')
        for id in temp:
            if id != 'x':
                self.busIDs.append(int(id))

    def findBus(self):
        # for each ID
        for id in self.busIDs:
            # let prior be divide earliest time -1 by bus ID
            prior = int((self.earliestTime - 1) / id)
            # next available time = bus ID * (prior + 1)
            nextTime = id * (prior + 1)
            # if next available time is less than the current minimum next time
            if nextTime < self.soonestTime:
                # min bus ID = bus ID
                self.soonestBus = id
                # current minimum next time = next available time
                self.soonestTime = nextTime
            # return (min bus ID * (current minimum next time - earliest time))
        return (self.soonestBus * (self.soonestTime - self.earliestTime))


def main():
    bf = BusFinder()

    dataFile = 'sample.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    
    with open(dataFile, 'r') as df:
        bf.loadEarliestTime(df.readline())
        bf.loadBusIDs(df.readline())

    print(bf.findBus())

if __name__ == '__main__':
    # run this file as a standalone script
    main()
