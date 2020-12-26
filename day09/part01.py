#! /usr/bin/env python3

import sys
import math

class CheckSum:
    def __init__(self):
        self.numbers = []
        self.non = 25

    def setNon(self, non):
        self.non = non

    def getNon(self):
        return self.non

    def loadPreamble(self, line):
        # strip
        # convert to integer (some rather large numbers)
        # append to numbers
        self.numbers.append(int(line.strip('\n')))

    def checkForSum(self, number):
        # check if the latest number is valid
        valid = False
        for num in self.numbers:
            otherNum = number - num
            if num != otherNum and otherNum in self.numbers:
                valid = True
                break
        return valid

    def loadNumber(self, line):
        valid = True
        # load another number
        newNumber = int(line.strip('\n'))
        # check for valid
        valid = self.checkForSum(newNumber)
        # append the new number
        self.numbers.append(newNumber)
        # pop off the front
        self.numbers.pop(0)
        return valid

def main():

    cs = CheckSum()

    cs.setNon(5)
    dataFile = 'sample.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
        cs.setNon(25)

    with open(dataFile, 'r') as df:
        for i in range(cs.getNon()):
            cs.loadPreamble(df.readline())
        for line in df:
            valid = cs.loadNumber(line)
            if not valid:
                print(line)
                break
    
if __name__ == '__main__':
    # run this file as a standalone script
    main()

    