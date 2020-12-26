#! /usr/bin/env python3

import sys

class Jolt:
    def __init__(self):
        self.adapters = [0]
        self.graph = {}
        self.count = 0

    def loadAdapters(self, line):
        self.adapters.append(int(line.strip('\n')))

    def graphAdapters(self):
        # sort the adapters
        self.adapters.sort()
        # for each adapter in adapters
        for i in range(len(self.adapters)):
            # add to the graph
            self.graph[self.adapters[i]] = []
            # look forward min(3, the end), implicitly assuming unique adapters
            start = min(i+1, len(self.adapters)-1)
            stop = min(i+3, len(self.adapters)-1)
            # for each of the foward looking adapters
            for j in range(start, stop+1):
                # if the adapter differences is 3 or less
                diff = self.adapters[j] - self.adapters[i]
                if diff >= 1 and diff <= 3:
                    # append to the adjacency list
                    self.graph[self.adapters[i]].append(self.adapters[j])

        # dfs the graph with no visited and count on leaf
        # visited = set()

        print(self.graph)

        # the following dfs with visited disabled works, but 
        # when the answer is in the trillions, it will take forever to finish
        # self.dfs(self.graph, self.adapters[0], visited)

        # this after some thought about branching 
        # probably could have figured this out while building the graph,
        # that is, while iterating frontwise through the adapters,
        # but to me, it makes more sense spelled out this way.
        print(self.unwind())
        return self.count
    
    def unwind(self):
        # start at the end and go backwards
        # at a node, the nways = sum(for each adjacency, numways)
        #
        # return the top nways
        nways = {}
        for i in range(len(self.adapters)-1,-1,-1):
            tempSum = 0
            for node in self.graph[self.adapters[i]]:
                if node in nways.keys():
                    tempSum += nways[node]
            nways[self.adapters[i]] = max(1, tempSum)

        print(nways)
        return nways[self.adapters[0]]

    def dfs(self, graph, node, visited = set()):
        # dfs with disabled visited
        # print("dfs: ", node)
        if True: # node not in visited:
            visited.add(node)
            if node in graph.keys():
                if len(graph[node]) == 0:
                    # leaf
                    self.count += 1
                else:
                    for neighbor in graph[node]:
                        self.dfs(graph, neighbor, visited)
            else:
                # a missing node in the graph
                print("found a lost node: ", node)
        else:
            # this is another path to the end
            self.count += 1
        return



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
    print(j.graphAdapters())

if __name__ == '__main__':
    # run this file as a standalone script
    main()
