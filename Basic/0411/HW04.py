member = {"Mery":10000,"Bill":5000000,"Johannes":0}

keys = member.keys()

values = member.values()

items = member.items()

print(keys)
print()
print(values)
print()
print(items)
print()

listk = list(keys)
listv = list(values)
listi = list(items)

print(listk)
print()
print(listv)
print()
print(listi)
print()

print(min(listv))
print(max(listv))

print()

for it in listi:
    print(it)
    print(it[0],it[1])

print()

for k,v in listi:
    print(k,v)