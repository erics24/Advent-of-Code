
### 2_Dec part 1 ###
with open("input.txt") as f:
    lines = f.readlines()

count = 0
'''
for line in lines:
    policy, password = line.strip().split(": ")
    nums, letter = policy.split()
    low, high = nums.split("-")
    if int(low) <= password.count(letter) <= int(high):
        count += 1
print(count)
'''
### Part 2 ###
for line in lines:
    policy, password = line.strip().split(": ")
    nums, letter = policy.split()
    low, high = nums.split("-")
    if bool(password[int(low)-1] == letter) != bool(password[int(high)-1] == letter):
        count += 1
print(count)