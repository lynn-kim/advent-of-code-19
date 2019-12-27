with open('input') as f:
    content = f.read().splitlines()

first = content[0].split(',')
second = content[1].split(',')

def get_coordinates(input):

    coordinates = []

    x = y = 0 

    for step in input: 

        diff_x = diff_y = 0
        
        num_places = int(step[1:])

        dir = step[0]

        if dir == 'R': 
            diff_x = 1
        elif dir == 'L':
            diff_x = -1
        elif dir == 'U': 
            diff_y = 1
        elif dir == 'D':
            diff_y = -1

        for a in range (0, num_places):
            x += diff_x
            y += diff_y

            new = (x,y)

            coordinates.append(new)

    return coordinates

path1 = get_coordinates(first)
path2 = get_coordinates(second)

poi = list(set(path1) & set(path2))

all_dist = []

for point in poi:
    distance = abs(point[0]) + abs(point[1])
    all_dist.append(distance)

print (min(all_dist))