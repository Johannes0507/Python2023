import copy
number = [1,2,3,4,5]
num = copy.copy(number)
print(num)
number[0] = 100
print(num)
print(number)