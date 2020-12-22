#!/usr/bin/env python3

import sys # for command line args

class Passwords:
    def __init__ (self):
        self.passwords = []
    
    def parsePassword(self, line):
        # split a liine of input on spaces first
        [freq, letter, pwd] = (line.strip('\n')).split(' ')

        # parse out min and max freq
        first = int(freq.split('-')[0])-1
        second = int(freq.split('-')[1])-1
        
        # parse out the validation character
        validChar = letter[0]

        # store the results
        self.passwords.append([first, second, validChar, pwd])

    def countValid(self):
        count = 0
        for [first, second, validChar, pwd] in self.passwords:
            # assume invalid
            isValid = False

            # parse password for character occurences
            isFirst = pwd[first] == validChar
            isSecond = pwd[second] == validChar

            # test password against the rule (one or the other but not both)
            isValid = bool(isFirst) ^ bool(isSecond)

            if isValid:
                count += 1

            # diagnostic
            print(first, second, validChar, pwd, isValid)
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


