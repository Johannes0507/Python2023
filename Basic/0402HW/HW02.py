a = 100
b = a
number = [1,2,3,4]
newnumber = number

print(id(a))
print(id(b))
print(id(number))
print(id(newnumber))
print()

a = 200
print(id(a))
print(id(b))
print()

number[0] = 20
print(id(number))
print(id(newnumber))