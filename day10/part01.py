#! /usr/bin/env python3

import sys

class Jolt:
    def __init__(self):
        self.adapters = []
        self.chain = []
        self.count = []

    def loadAdapters(self, line):
        self.adapters.append(int(line.strip('\n')))

    def connect(self):
        # initialize the previous jolt level to 0
        pAdapter = 0
        # initialize the count
        self.count.append(0)
        self.count.append(0)
        self.count.append(1) # for built-in
        # sort the adapters
        self.adapters.sort()
        # for each adapter in adapters
        for adapter in self.adapters:
            # measure the difference between adapter and previous
            diff = int(adapter - pAdapter) - 1
            # allocate the difference to ones, twos or threes
            if diff >= 0 and diff <= 2:
                self.count[diff] += 1
            else:
                print("diff",diff,"out of range for adapter: ",adapter)
            # update previous
            pAdapter = adapter
        
        print(self.count[0], self.count[2])
        return self.count[0] * self.count[2]



def main():

    j = Jolt()

    # read in the data
    dataFile = 'sample.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    with open(dataFile, 'r') as df:
        for line in df:
            j.loadAdapters(line)

    # maybe something else
    print(j.connect())

if __name__ == '__main__':
    # run this file as a standalone script
    main()
