#! /usr/bin/env python3

import sys

class Assembly:
    def __init__(self):
        self.instructions = []
        self.visited = []
        self.instructionPointer = 0 # intel convention instead of program counter
        self.acc = 0 # accumulator

    def loadMemory(self, line):
        # read in an instruction and load it into memory
        # strip
        [instruction, vStr] = (line.strip('\n')).split(' ')
        self.instructions.append([instruction, vStr])
        self.visited.append(0)

    def run(self):
        # run the loaded program
        self.instructionPointer = 0
        self.acc = 0
        hcf = False
        while not hcf:
            hcf = self.execute()

        return self.acc

    def execute(self):
        hcf = False # return value
        # diagnostic
        print(self.instructions[self.instructionPointer], self.visited[self.instructionPointer]," | ",self.instructionPointer, self.acc)
        # if not here before, execute
        if self.visited[self.instructionPointer] == 0:
            hcf = False
            self.visited[self.instructionPointer] += 1
            # execute an instruction at the IP
            [instruction, vStr] = self.instructions[self.instructionPointer]
            if instruction == 'nop':
                self.instructionPointer += 1
            elif instruction == 'acc':
                self.acc += int(vStr)
                self.instructionPointer += 1
            elif instruction == 'jmp':
                self.instructionPointer += int(vStr)
            else:
                print("unknown instruction: ",instruction,vStr)
                hcf = True

        else: # halt and catch fire
            hcf = True

        return hcf

def main():
    dataFile = 'sample01.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]

    # instantiate
    mp = Assembly()

    with open(dataFile, 'r') as df:
        for line in df:
            mp.loadMemory(line)

    print(mp.run())

if __name__ == '__main__':
    # execute this file as a standalone script
    main()
