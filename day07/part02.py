#! /usr/bin/env python3

import sys
import re


class Bags:
    def __init__ (self):
        self.graph = {}
        self.numberOfBags = 0
        self.bagP = re.compile('bag') # bag
        self.bagS = re.compile(r'\d+') # <number> in <number> <bag>

    def bagRules(self, line):
        # clean up the input
        line = line.strip('\n')

        # convert line of input into a key and an array of values, 
        # perhaps tuples of bag and frequency
        #
        # <bag> bags contain {"no other bags." | <number> <bag> {"bag"|"bags"} (',' for more, '.' for end)}

        # get the initial <bag>
        [bag, theRest] = line.split(' bags contain ')
        
        tempValue = []
        if 'no other' in theRest:
            # leaf bag - leave tempValue as is
            pass
        else:
            # split up the list of neighbors on commas
            neighbors = theRest.split(', ')
            # iterate through the array of '<number> <bag> (bag|bags)(, |\.)'
            for nextBag in neighbors:
                # find the caboose
                mP = self.bagP.search(nextBag)
                if mP:
                    # strip off the caboose
                    nextBag = nextBag[:mP.start()-1]
                else:
                    print("failed to find trailing bags: ", nextBag)
                    pass
                # find the leading number
                mS = self.bagS.match(nextBag)
                if mS:
                    # split the number from the node
                    weight = int(nextBag[:mS.end()])
                    node = nextBag[mS.end()+1:]
                    # add that to the graph value
                    tempValue.append([node, weight])
                else:
                    print("failed to find a number: ", nextBag)
                    pass
                
        # add the result to the graph
        if bag in self.graph.keys():
            # append
            for node in tempValue:
                self.graph[bag].append(node)
        else:
            # initialize
            self.graph[bag] = tempValue

    def totalBags(self):
        rootNode = ['shiny gold', 1]
        return self.countBelow(self.graph, rootNode) - 1

    def countBelow(self, graph, node):
        # number of bags
        rv = node[1]

        # number of bags times number of bags below
        brv = 0
        for neighbor in graph[node[0]]:
            brv += self.countBelow(graph, neighbor)

        rv += rv * brv
        
        print("for node: ",node," returning ",rv)
        return rv

def main():
    dataFile = 'sample_data.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]

    # instantiate class
    bags = Bags()

    with open(dataFile,'r') as df:
        for line in df:
            # read in the data
            bags.bagRules(line)

    # return the answer
    print(bags.totalBags())

if __name__ == "__main__":
    # run this file as a script
    main()
