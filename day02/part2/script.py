file = open('input', 'r')
arr = file.read().split(',')
file.close()

nums = []

for x in arr:
    nums.append(int(x))

temp = nums[:]

for noun in range(0,100):
    for verb in range(0,100):

        temp[1] = noun
        temp[2] = verb
        curr = 0

        length = len(temp)
        exists = True        
        while (temp[curr] != 99 and exists): 
            if temp[curr] == 1: 
                temp[temp[curr+3]] = temp[temp[curr+1]] + temp[ temp[curr+2]]
            elif temp[curr] == 2:
                temp[temp[curr+3]] = temp[temp[curr+1]] * temp[ temp[curr+2]]
           
            curr += 4
            exists = temp[curr+3] < length and temp[curr+1] < length and temp[curr+2] < length

        if (temp[0] == 19690720):
            answer = 100 * noun + verb 
            print ( "noun: %s, verb: %d, answer: %f" % (noun, verb, answer))
            break
        else:
            temp = nums[:]
        
        
    
# print (nums)