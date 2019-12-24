file = open('input', 'r')
arr = file.read().split(',')
file.close()

nums = []

for x in arr:
    nums.append(int(x))

while (nums[i] != 99):
    if nums[i] == 1: 
        nums[nums[i+3]] = nums[nums[i+1]] + nums[ nums[i+2]]
    elif nums[i] == 2:
        nums[nums[i+3]] = nums[nums[i+1]] * nums[ nums[i+2]]
    i += 4
    
print (nums)