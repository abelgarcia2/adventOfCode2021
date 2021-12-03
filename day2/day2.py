f = open('day2/input.txt', 'r')

positions = f.readlines()

h_position = 0
depth = 0
aim = 0

for i in positions:
    direction = i.split()[0]
    quantity = int(i.split()[1])

    if (direction == 'forward'):
        h_position += quantity
        depth += quantity * aim
    elif (direction == 'down'):
        # depth += quantity
        aim += quantity
    elif (direction == 'up'):
        # depth -= quantity
        aim -= quantity

print(h_position * depth)