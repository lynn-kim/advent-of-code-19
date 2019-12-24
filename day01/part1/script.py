import math

file = open('input', 'r')

total_fuel = 0

for x in file:
    curr = math.floor( int (x) / 3) - 2 
    total_fuel += curr

print("The total fuel required is", total_fuel)

file.close()
