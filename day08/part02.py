#! /usr/bin/env python3

import sys

class Assembly:
    def __init__(self):
        self.instructions = []
        self.visited = set()
        self.instructionPointer = 0 # intel convention instead of program counter
        self.pJMP = [] # instruction pointers for jmp
        self.pNOP = [] # instruction pointers for nops
        self.acc = 0 # accumulator

    def loadMemory(self, line):
        # read in an instruction and load it into memory
        # strip
        [instruction, vStr] = (line.strip('\n')).split(' ')
        self.instructions.append([instruction, vStr])

    def run(self, instructions, tracking):
        # run the loaded program
        self.instructionPointer = 0
        self.visited = set()
        self.acc = 0
        hcf = False
        terminatePointer = len(instructions)
        while not hcf and self.instructionPointer < terminatePointer:
            hcf = self.execute(instructions, tracking)
        return [hcf, self.acc]

    def execute(self, instructions, tracking):
        hcf = False # return value
        # diagnostic
        # print(instructions[self.instructionPointer], self.instructionPointer in self.visited," | ",self.instructionPointer, self.acc)
        # if not here before, execute
        if self.instructionPointer not in self.visited:
            hcf = False
            self.visited.add(self.instructionPointer)
            # execute an instruction at the IP
            [instruction, vStr] = instructions[self.instructionPointer]
            if instruction == 'nop':
                if tracking:
                    self.pNOP.append(self.instructionPointer)
                self.instructionPointer += 1
            elif instruction == 'acc':
                self.acc += int(vStr)
                self.instructionPointer += 1
            elif instruction == 'jmp':
                if tracking:
                    self.pJMP.append(self.instructionPointer)
                self.instructionPointer += int(vStr)
            else:
                print("unknown instruction: ",instruction,vStr)
                hcf = True
        else: # halt and catch fire
            hcf = True
        return hcf

    def modifyMemory(self, ip):
        instructions = []
        for instruction in self.instructions:
            instructions.append(instruction.copy())
        [instruction, vStr] = instructions[ip]
        if instruction == 'jmp':
            print("modifying jmp at: ", ip, "with value ", instructions[ip][1])
            instructions[ip][0] = 'nop'
        elif instruction == 'nop':
            print("modifying nop at: ", ip, "with value ", instructions[ip][1])
            instructions[ip][0] = 'jmp'
        else:
            print("something is not right: ",[instruction, vStr])
        return instructions

def main():
    dataFile = 'sample01.txt'
    if len(sys.argv) > 1:
        dataFile = sys.argv[1]

    # instantiate
    mp = Assembly()

    with open(dataFile, 'r') as df:
        for line in df:
            mp.loadMemory(line)

    # execute the original run
    instructions = []
    for instruction in mp.instructions:
        instructions.append(instruction.copy())
    tracking = True # keep track of jmp and nop instructions
    [hcf, acc] = mp.run(instructions, tracking)
    print("HCF: ", hcf)
    print("accumulator: ",acc)
    print(" ")

    hcf = True
    tracking = False

    # test for jmp to nop and nop to jump
    # this seems brute force
    # is there more efficient answer?  
    print("Starting jmp to nop")
    for pointer in mp.pJMP:
        modified = []
        modified = mp.modifyMemory(pointer)
        [hcf, acc] = mp.run(modified, tracking)
        if not hcf:
            print("done with acc: ", acc)
            break
    
    if hcf:
        print("Starting nop to jmp")
        for pointer in mp.pNOP:
            modified = []
            modified = mp.modifyMemory(pointer)
            [hcf, acc] = mp.run(modified, tracking)
            if not hcf:
                print("done with acc: ", acc)
                break
    
    if hcf:
        print("Failed to find")

if __name__ == '__main__':
    # execute this file as a standalone script
    main()
