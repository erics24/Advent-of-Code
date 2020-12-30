'''
with open("input.txt") as f:
    numTrees = 0
    x, y = 0, 0
    for line in f.readlines()[1:]:
        print(line.strip())
        length = len(line.strip())   
        print(length)
        x = (x + 3) % length
        print(line[x])
        if line[x] == '#':
            numTrees += 1
            
        if x > 30:
            break
print(numTrees)
'''
### Part 2 ###
with open("input.txt") as f:
    grid = f.read().strip().split('\n')

def down_slope(x_interval, y_interval, grid_map):
    pos_x, pos_y = 0, 0
    numTrees = 0
    length = len(grid_map[0])
    for line in grid_map[y_interval:len(grid_map):y_interval]:
        pos_x = (pos_x + x_interval) % length
        if line[pos_x] == "#":
            numTrees += 1
    return numTrees

Trial_1_1 = down_slope(1, 1, grid)
print(Trial_1_1)
Trial_3_1 = down_slope(3, 1, grid)
print(Trial_3_1)
Trial_5_1 = down_slope(5, 1, grid)
print(Trial_5_1)
Trial_7_1 = down_slope(7, 1, grid)
print(Trial_7_1)
Trial_1_2 = down_slope(1, 2, grid)
print(Trial_1_2)

Answer = down_slope(1, 1, grid) * down_slope(3, 1, grid) * down_slope(5, 1, grid) \
    * down_slope(7, 1, grid) * down_slope(1, 2, grid)
print(Answer)
