#!/usr/bin/env python3

import sys # for command line args

class Passwords:
    def __init__ (self):
        self.passwords = []
    
    def parsePassword(self, line):
        # split a liine of input on spaces first
        [freq, letter, pwd] = (line.strip('\n')).split(' ')

        # parse out min and max freq
        minFreq = int(freq.split('-')[0])
        maxFreq = int(freq.split('-')[1])
        
        # parse out the validation character
        validChar = letter[0]

        # store the results
        self.passwords.append([minFreq, maxFreq, validChar, pwd])

    def countValid(self):
        count = 0
        for [minFreq, maxFreq, validChar, pwd] in self.passwords:
            # assume invalid
            isValid = False

            # parse password for character frequencies
            charFreq = {}
            for char in pwd:
                if char in charFreq.keys():
                    charFreq[char] += 1
                else:
                    charFreq[char] = 1

            # test password against the rule
            if validChar in charFreq.keys():
                if charFreq[validChar] >= minFreq and charFreq[validChar] <= maxFreq:
                    isValid = True

            if isValid:
                count += 1

            # diagnostic
            print(minFreq, maxFreq, validChar, pwd, isValid)
        return count


def main():
    dataFile = 'sample_data.txt'

    if len(sys.argv) > 1:
        dataFile = sys.argv[1]
    print("using data file: ", dataFile)
    
    passwords = Passwords()
    df = open(dataFile, 'r')
    for line in df:
        passwords.parsePassword(line)
    df.close()

    print(passwords.countValid())


if __name__ == "__main__":
    # run
    main()


