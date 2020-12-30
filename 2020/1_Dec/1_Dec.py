import time, os

### 1_Dec part 1 ###
with open("input.txt") as f:
    text = f.read()
nums = text.strip().split('\n')

for index, num in enumerate(nums):
    for second_num in nums[index + 1:]:
        if int(num) + int(second_num) == 2020:
            result = int(num)*int(second_num)
print(result)



### 1_Dec part 2 ###
for index, num in enumerate(nums):
    for second_num in nums[index + 1:]:
        for third_num in nums[index + 2:]:
            if int(num) + int(second_num) + int(third_num) == 2020:
                result = int(num)*int(second_num)*int(third_num)
                print(num, second_num, third_num)
print(result)


