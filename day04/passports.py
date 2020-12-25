#! /usr/bin/env python3

import sys
import re

class Passports:
    def __init__(self):
        self.passports = []
        self.workingPassport = {}
        self.workingValid = {}
        self.definitionValid = {
            'byr': False, # (Birth Year)
            'iyr': False, # (Issue Year)
            'eyr': False, # (Expiration Year)
            'hgt': False, # (Height)
            'hcl': False, # (Hair Color)
            'ecl': False, # (Eye Color)
            'pid': False, # (Passport ID)
            'cid': True # (Country ID) optional
            }

    def parsePassport(self, line):
        isData = line.find(':') != -1
        keyVal = (line.strip('\n')).split(' ')

        if isData:
            # append passport data to the current passport
            for kv in keyVal:
                # print(kv)
                [key, value] = kv.split(':')
                self.workingPassport[key] = value
        else:
            # blank line marks the end of a passport
            # check validation, append valid key and save
            self.workingValid = self.definitionValid.copy()
            for k,v in self.workingPassport.items():
                valueValid = True
                if k == 'byr':
                    valueValid = (int(v) >= 1920 and int(v) <= 2002)
                elif k == 'iyr':
                    valueValid = (int(v) >= 2010 and int(v) <= 2020)
                elif k == 'eyr':
                    valueValid = (int(v) >= 2020 and int(v) <= 2030)
                elif k == 'hgt':
                    if v.find('cm') >= 0:
                        h = int(v[0:v.find('cm')])
                        valueValid = (h >= 150 and h <= 193)
                    elif v.find('in') >= 0:
                        h = int(v[0:v.find('in')])
                        valueValid = (h >= 59 and h <= 76)
                    else:
                        valueValid = False
                elif k == 'hcl':
                    p = re.compile('^#[a-z0-9]{6,6}$')
                    valueValid = bool(p.match(v))
                elif k == 'ecl':
                    ecls = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
                    valueValid = (v in ecls)
                elif k == 'pid':
                    p = re.compile('^[0-9]{9,9}$')
                    valueValid = bool(p.match(v))

                if valueValid:
                    self.workingValid[k] = valueValid  
                else:
                    break

            # now evaluate all keys
            isValid = True
            for k, v in self.workingValid.items():
                # print(k, ', ', v)
                if not v:
                    isValid = False
                    break

            self.workingPassport['valid'] = isValid
            self.passports.append(self.workingPassport.copy())
            self.workingPassport.clear()
            self.workingValid.clear()
            # print("Valid: ", isValid)
            # print('----------------------------')

    def countValidPassports(self):
        count = 0
        for passport in self.passports:
            if passport['valid']:
                count += 1
        
        return count

def main():
    fileName = 'sample_data.txt'
    if len(sys.argv) > 1:
        fileName = sys.argv[1]

    passports = Passports()
    
    df = open(fileName, 'r')
    for line in df:
        # parse in the data
        passports.parsePassport(line)
    df.close

    # flush the last passport
    passports.parsePassport(' ')

    # calculate the answer
    print(passports.countValidPassports())

if __name__ == '__main__':
    # run this as a script
    main()
