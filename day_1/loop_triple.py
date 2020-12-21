#!/usr/bin/env python3

""" 
I initially tried solving this by sorting the list, 
then incrementing bottom or decrementing top
depending on conditions based on the result of searching for a third value
inbetween the top and the bottom.  This approach worked with the sample data, 
but went wrong on the larger data set.

I then looked at what I might do by hand with a sorted list, and came up
with a nested loop (for first and second values) that finds a result or breaks
out when the residual is less than the second value.  This requires a map to
look up the third value at each iteration, something the first approach did not. 
"""


import sys # for command line arguments

class LoopTriple:
    def __init__(self, desiredSum):
        self.desiredSum = desiredSum  # the desired sum 
        self.numbersList = [] # the list of numbers
        self.numbersSet = set() # the set of numbers

    def loadnumbers(self, number):
        # put the number in the list
        self.numbersList.append(number)
        # put the number in the set
        self.numbersSet.add(number)

    def checkList(self):
        # basic check
        if len(self.numbersList) < 3:
            print("not enough numbers")
            return False

        # sort to support an interative approach
        self.numbersList.sort()

        # nested loop to iterate first and second number
        # if the residual is greater than the second
        # look up the third in the set
        # else break the inner loop

        for i in range(len(self.numbersList)):
            for j in range(i+1, len(self.numbersList)):
                thirdNumber = self.desiredSum - self.numbersList[i] - self.numbersList[j]
                if thirdNumber <= self.numbersList[j]:
                    break
                else:
                    if thirdNumber in self.numbersSet:
                        print("multiplication: ", self.numbersList[i] * self.numbersList[j] * thirdNumber)

        print("done looking")

def main():
    dataFile = 'sample_data.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    print("using data file: ", dataFile)
    
    lt = LoopTriple(2020)
    df = open(dataFile, 'r')
    for line in df:
        lt.loadnumbers(int(line.strip('\n')))
    df.close()

    lt.checkList()


# run main if this is run as a script
if __name__ == "__main__":
    # run this
    main()