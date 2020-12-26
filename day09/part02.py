#! /usr/bin/env python3

import sys
import math

class CheckSum:
    def __init__(self):
        self.numbers = []
        self.non = 25
        self.targetSum = 248131121
        self.ctsChunk = []
        self.tempSum = 0

    def setNon(self, non):
        self.non = non

    def getNon(self):
        return self.non

    def setTargetSum(self, num):
        self.targetSum = num

    def getTargetSum(self):
        return self.targetSum

    def loadList(self, line):
        # strip
        # convert to integer (some rather large numbers)
        # append to numbers
        self.numbers.append(int(line.strip('\n')))

    def findSum(self):
        tempSum = 0
        ctsChunk = []
        for num in self.numbers:
            tempSum += num
            ctsChunk.append(num)
            while tempSum > self.targetSum:
                # pop the first number off of ctsChunk
                # subtract that number from tempSum
                tempSum -= ctsChunk.pop(0)
            # if tempSum == targetSum
            if len(ctsChunk) > 1 and tempSum == self.targetSum:
                # return sum of first and last entries in ctsChunk
                first = min(ctsChunk)
                last = max(ctsChunk)
                print(ctsChunk)
                return first + last
        return -1 # failed

def main():

    cs = CheckSum()

    dataFile = 'sample.txt'
    cs.setNon(5)
    cs.setTargetSum(127)

    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
        cs.setNon(25)
        cs.setTargetSum(248131121)

    with open(dataFile, 'r') as df:
        for line in df:
            cs.loadList(line)
    
    print(cs.findSum())


if __name__ == '__main__':
    # run this file as a standalone script
    main()

    