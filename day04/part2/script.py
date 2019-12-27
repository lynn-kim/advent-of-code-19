# two adjacent digits 
# numbers never decrease from left to right
# always 6 digits 
# find number of valid solutions in range 


# 666625
# 123444
def checkDouble(num):
    for i in range(0, len(num)-1): # length = 6 - 1 = 5 since exclusive, goes to 4 
        if num[i] == num [i+1] and ( i > len(num) - 3 or num[i] != num [i+2]) and (i < 1 or num[i] != num[i-1]):
            return True
    return False 

def checkIncrease(num):
    if num < 10:
        return True 
    elif num % 10 < ((num / 10) % 10):
        return False 
    else:
        return checkIncrease (num/10)

solutions = []

for i in range (246515, 739105):
    isValid = checkDouble(str(i)) and checkIncrease(i)
    if (isValid):
        solutions.append(i)
print (len(solutions))
