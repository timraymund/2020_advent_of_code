#!/usr/bin/env python3

class FindPair:
    def __init__(self, desiredSum):
        self.desiredSum = desiredSum  # the desired sum of two of the numbers
        self.numberMap = {}

    def checkNumber(self, number):
        # add the number to the dict
        if number not in self.numberMap.keys():
            self.numberMap[number] = 1
        else:
            self.numberMap[number] += 1

        # potential pair value 
        otherNumber = self.desiredSum - number

        # check for the pair value
        if otherNumber in self.numberMap.keys():
            print("found a pair")
            print(number, " ", otherNumber)
            if otherNumber == number:
                if self.numberMap[number] > 1:
                    print("more than one of these")
                else:
                    print("only one of these so far")
            print("pair multiplied: ", number*otherNumber)
            return True
        else:
            # not the pair
            return False


def main():
    fp = FindPair(2020)
    df = open('data.txt', 'r')

    for line in df:
        if fp.checkNumber(int(line.strip('\n'))):
            break

    df.close()







# run main if this is run as a script
if __name__ == "__main__":
    # run this
    main()