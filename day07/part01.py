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

    def bagRoot(self):
        # make sure shiny gold is in the graph as a leaf
        if 'shiny gold' not in self.graph.keys():
            self.graph['shiny gold'] = []
        
        # create a root node value without shiny gold
        tempValue = []
        for key in self.graph.keys():
            if key != 'shiny gold':
                tempValue.append([key, 1])

        self.graph['deep root'] = tempValue

    def DFSBags(self):
        count = 0
        rootNode = 'deep root' # start at root
        for node in self.graph[rootNode]:
            self.numberOfBags = 0
            visited = set()
            self.dfs(self.graph, node[0], visited)
            if self.numberOfBags > 0:
                count += 1
            # print(node[0], self.numberOfBags, count)
        return count

    def BFSBags(self):
        count = 0
        rootNode = 'deep root' # start at root
        for node in self.graph[rootNode]:
            visited = set()
            queue = []
            rv = self.bfs(self.graph, node[0], visited, queue)
            count += rv
            # print(node[0], rv, count)
        return count

    def dfs(self, graph, node, visited = set()):
        # print("dfs: ", node)
        if node == 'shiny gold':
            # print("found shiny gold")
            self.numberOfBags += 1
        if node not in visited:
            visited.add(node)
            if node in graph.keys():
                for neighbor in graph[node]:
                    self.dfs(graph, neighbor[0], visited)
            else:
                # missing node
                print("found a lost node: ", node)
    
    def bfs(self, graph, node, visited = set(), queue = []):
        visited.add(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            # print("bfs: ", s)
            if s == 'shiny gold':
                # print("found shiny gold")
                return 1

            for neighbor in graph[s]:
                if neighbor[0] not in visited:
                    visited.add(neighbor[0])
                    queue.append(neighbor[0])

        return 0


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

    # add a root to the graph
    bags.bagRoot()
    
    # return the answer
    print(bags.DFSBags())

    # try something else
    print(bags.BFSBags())

if __name__ == "__main__":
    # run this file as a script
    main()
