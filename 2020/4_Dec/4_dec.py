### Part 1 ###
'''
with open("input.txt") as f:
    passports = f.read().split('\n\n')

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] ## 'cid' optional

def find_keys(passport_element):
    return passport_element.split(":")[0]

num_valid = 0
for passport in passports:
    valid = True
    passport = passport.split()
    key_list = list(map(find_keys, passport))
    field_index = 0
    while valid and field_index < len(fields):
        if fields[field_index] not in key_list:
            valid = False
            break
        field_index += 1
    if not valid: continue
    num_valid += 1

print(num_valid)
'''
### Part 2 ###
import re
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] ## 'cid' optional

with open("input.txt") as f:
    passports = f.read().split('\n\n')

def validate_values(passport_dict):
    for field in fields:
        if field not in pass_dict.keys():
            print("0")
            return False
    byr = passport_dict['byr']
    iyr = passport_dict['iyr']
    eyr = passport_dict['eyr']
    hgt = passport_dict['hgt']
    hcl = passport_dict['hcl']
    ecl = passport_dict['ecl']
    pid = passport_dict['pid']
    
    if len(byr) != 4 or not (1920 <= int(byr) <= 2002):
        print("1")
        return False
    if len(iyr) != 4 or not (2010 <= int(iyr) <= 2020):
        print("2")
        return False
    if len(eyr) != 4 or not (2020 <= int(eyr) <= 2030):
        print("3")
        return False
    if re.match(r"^\d{1,}(cm|in)$", hgt) is None:
        return False
    else:        
        if 'in' in hgt:
            if not (59 <= int(hgt.split("in")[0]) <= 76):
                print("4")
                return False
        if 'cm' in hgt:
            if not (150 <= int(hgt.split("cm")[0]) <= 193):
                print("5")
                return False
    if re.match(r"^#[0-9a-f]{6}$", hcl) is None:
        print("6")
        return False
    eye_col = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl not in eye_col:
        print("7")
        return False
    if re.match(r"^\d{9}$", pid) is None:
        print("8")
        return False
    return True
    

valids = 0
for passport in passports:
    passport = passport.split()
    pass_dict = {}
    for element in passport:
        key, val = element.split(":")
        pass_dict[key] = val
    print(pass_dict)
    if validate_values(pass_dict):
        valids += 1
        print(True)

print(valids)