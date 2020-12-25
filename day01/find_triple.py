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

class FindTriple:
    def __init__(self, desiredSum):
        self.desiredSum = desiredSum  # the desired sum of two of the numbers
        self.numbers = [] # the map of numbers

    def loadNumbers(self, number):
        # put the number in the map
        self.numbers.append(number)

    def checkList(self):
        # basic check
        if len(self.numbers) < 3:
            return False

        # sort to support advancing from both sides to find a middle (third) value
        self.numbers.sort()

        # initialize top, bottom, and found
        top = len(self.numbers) - 1      
        bottom = 0 
        found = False

        # while not found
        while not found:

            # escape valve
            if top <= bottom:
                print("exhausted the search")
                break

            # set up the next search for the third number in between left and right
            left = bottom
            right = top
            mid = round((left + right) / 2)
            leftNumber = self.numbers[left]
            rightNumber = self.numbers[right]
            midNumber = self.numbers[mid]
            targetNumber = self.desiredSum - leftNumber - rightNumber

            tooBig = targetNumber < self.numbers[left+1]

            print(leftNumber, ", ", rightNumber, ", ", targetNumber, ", ", tooBig)

            # binary search in between the current left and right
            while not tooBig and mid > left and mid < right:
                if midNumber < targetNumber:
                    left = mid
                    leftNumber = self.numbers[left]
                elif midNumber > targetNumber:
                    right = mid
                    rightNumber = self.numbers[right]
                else:
                    # midNumber == targetNumber
                    print("multiplication: ", leftNumber * midNumber * rightNumber)
                    found = True
                    break

                mid = round((left + right) / 2)
                midNumber = self.numbers[mid]

            # done searching
            print(left, ", ", mid, ", ", right, ", ", bottom, ", ", top)
            testSum = self.numbers[bottom] + self.numbers[mid] + self.numbers[top]
            if testSum > self.desiredSum:
                # too big
                print("too big")
                top = top - 1
            elif testSum < self.desiredSum:
                # too small
                print("too small")
                bottom = bottom + 1
            else:
                print("found it.  why are we here?")
                break
        
        return found

def main():
    dataFile = 'sample_data.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    print("using data file: ", dataFile)
    
    ft = FindTriple(2020)
    df = open(dataFile, 'r')
    for line in df:
        ft.loadNumbers(int(line.strip('\n')))
    df.close()

    ft.checkList()


# run main if this is run as a script
if __name__ == "__main__":
    # run this
    main()