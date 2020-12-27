#! /usr/bin/env python3

import sys

class SeatRules:
    def __init__(self):
        self.seats = []

    def loadSeats(self, line):
        self.seats.append(list(line.strip('\n')))
    
    def seatTest(self, di, dj, ii, ij):
        # tests for occupied
        # outside the range is not occupied
        si = di
        sj = dj

        rowMin = 0
        seatMin = 0

        # print(" ")

        while True:
            # print("testing: ", si, sj)
            rowMax = len(self.seats)-1
            if si < rowMin or si > rowMax:
                return False
            seatMax = len(self.seats[si])-1
            if sj < seatMin or sj > seatMax:
                return False
            
            #while in range, L or . is not occupied
            seat = self.seats[si][sj]
            if seat == '#':
                return True
            if seat == 'L':
                return False
            #next seat in view
            si += ii
            sj += ij

    def checkEight(self, si, sj):
        # check all 8 surrounding seats
        # return number occupied
        nOcc = 0
        # upper mid
        if self.seatTest(si+1, sj, 1, 0):
            nOcc += 1
        # upper right
        if self.seatTest(si+1, sj+1, 1, 1):
            nOcc += 1
        # middle right
        if self.seatTest(si, sj+1, 0, 1):
            nOcc += 1
        # lower right
        if self.seatTest(si-1, sj+1, -1, 1):
            nOcc += 1
        # lower middle
        if self.seatTest(si-1, sj, -1, 0):
            nOcc += 1
        # lower left
        if self.seatTest(si-1, sj-1, -1, -1):
            nOcc += 1
        # middle left
        if self.seatTest(si, sj-1, 0, -1):
            nOcc += 1
        # upper left
        if self.seatTest(si+1, sj-1, 1, -1):
            nOcc += 1
        return nOcc

    def copySeats(self, oldSeats):
        seats = []
        for row in oldSeats:
            seats.append(row.copy())
        return seats

    def applyRules(self):
        seats = []
        changed = 0
        for i in range(len(self.seats)):
            temp = []
            for j in range(len(self.seats[i])):
                nOcc = self.checkEight(i,j)
                if self.seats[i][j] == 'L':
                    if nOcc == 0:
                        temp.append('#')
                        changed += 1
                    else:
                        temp.append('L')
                elif self.seats[i][j] == '#':
                    if nOcc >= 5:
                        temp.append('L')
                        changed += 1
                    else:
                        temp.append('#')
                else: # a floor '.'
                    temp.append('.')
            seats.append(temp.copy())

        self.seats = self.copySeats(seats)
        return changed

    def countSeats(self):
        count = 0
        for row in self.seats:
            for seat in row:
                if seat == '#':
                    count += 1
        return count
    
    def printSeats(self):
        for row in self.seats:
            print("".join(row))


def main():

    sr = SeatRules()

    dataFile = 'sample.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1] 
    with open(dataFile, 'r') as df:
        for line in df:
            sr.loadSeats(line)
    
    # do something else
    print("------------------")
    sr.printSeats()
    print(sr.countSeats())
    print(" ")

    changed = sr.applyRules()
    print("------------------")
    sr.printSeats()
    print(sr.countSeats())
    print(" ")
    
    while changed > 0:
        changed = sr.applyRules()
        print("------------------")
        sr.printSeats()
        print(sr.countSeats())
        print(" ")

    print("---- DONE ------")


if __name__ == '__main__':
    # run this file as a standalone script
    main()
