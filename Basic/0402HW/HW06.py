data = (1,2,3,4,5)
print(type(data))
print(data[0])
print(data)
print()


listdata = list(data)
listdata[0] = 100
data = tuple(listdata)
print(data)