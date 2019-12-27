# at least two adjacent digits are the same 
# numbers never decrease from left to right
# always 6 digits 
# find number of valid solutions in range 
def checkDouble(num):
    if num < 11:
        return False 
    elif num % 10 == ((num / 10) % 10):
        return True
    else: 
        return checkDouble(num/10)

def checkIncrease(num):
    if num < 10:
        return True 
    elif num % 10 < ((num / 10) % 10):
        return False 
    else:
        return checkIncrease (num/10)

solutions = []

for i in range (246515, 739105):
    isValid = checkDouble(i) and checkIncrease(i)
    if (isValid):
        solutions.append(i)

print (len(solutions))
