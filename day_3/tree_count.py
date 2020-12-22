#!/usr/bin/env python3

import sys

class TreePath:
    def __init__(self):
        self.treeMap = []
    
    def loadMapRow(self, line):
        # parse the map row out of the line
        row = line.strip('\n')

        # append it into the treeMap
        self.treeMap.append(row)

    def countTrees(self, right, down):
        # assume upper left start location
        x = 0
        y = 0

        nRows = len(self.treeMap)
        nCols = len(self.treeMap[0])

        # initialize count
        count = 0

        # while there are map rows
        while y < nRows:
            # check for a tree and increment the count
            if self.treeMap[y][x] == '#':
                count += 1
                # row = list(self.treeMap[y])
                # row[x] = 'X'
                # self.treeMap[y] = "".join(row)
            # else:
            #     row = list(self.treeMap[y])
            #     row[x] = 'O'
            #     self.treeMap[y] = "".join(row)
            
            # move right and down, wrapping map rows as needed
            y += down
            x = (x + right) % nCols
        
        # diagnostic
        # for row in self.treeMap:
        #     print(row)

        # return the count
        return count

def main():
    dataFile = 'sample_data.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    print("Using data file: ", dataFile)

    treePath = TreePath()

    df = open(dataFile, 'r')
    for line in df:
        treePath.loadMapRow(line)
    df.close()

    print(treePath.countTrees(3, 1))

    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    result = 1
    for [right, down] in slopes:
        result *= treePath.countTrees(right, down)

    print(result)


if __name__ == '__main__':
    # run this
    main()
