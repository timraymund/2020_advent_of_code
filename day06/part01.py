#! /usr/bin/env python3

import sys

class CustomsQuestions:
    def __init__(self):
        self.answers = {}
        self.group = 0
        self.ansSet = set()
        
        self.eanswers = {}
        self.eansSet = set() # the intersection of answer for the group
        self.pansSet = set() # the current persons answers
        self.first = True # first person in the group
    
    def storeAnswers(self, line):
        ans = list(line.strip('\n'))
        if len(ans) > 0:
            for a in ans:
                self.ansSet.add(a)
                self.pansSet.add(a)
            if self.first:
                self.eansSet = self.pansSet.copy()
                self.first = False
            else:
                self.eansSet.intersection_update(self.pansSet)
            self.pansSet.clear()
        else:
            self.answers[self.group] = self.ansSet.copy()
            self.eanswers[self.group] = self.eansSet.copy()
            self.group += 1
            self.ansSet.clear()
            self.eansSet.clear()
            self.first = True

    def countPerGroup(self):
        totalAnswerPerGroup = 0
        for g, a in self.answers.items():
            print(len(a))
            totalAnswerPerGroup += len(a)
        
        totalEAnswerPerGroup = 0
        for g, a in self.eanswers.items():
            totalEAnswerPerGroup += len(a)

        return totalAnswerPerGroup, totalEAnswerPerGroup

    

def main():
    dataFile = 'sample_data.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]

    cq = CustomsQuestions()

    with open(dataFile, 'r') as df:
        for line in df:
            # absorb the input
            cq.storeAnswers(line)

    # find the answer
    print(cq.countPerGroup())

if __name__ == '__main__':
    # run this file as a standalone script
    main()
