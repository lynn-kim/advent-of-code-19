import math

file = open('input', 'r')

total_fuel = 0
rows = 0 

for x in file:
    val = math.floor(int(x) / 3) - 2 
    while (val > 0): 
        total_fuel += val
        val = math.floor( val / 3) - 2         

print("The total fuel required is", total_fuel)

file.close()