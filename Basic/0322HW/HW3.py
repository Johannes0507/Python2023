x = int(input("第一邊："))
y = int(input("第二邊："))
z = int(input("第三邊："))

if x + y >= z and x + z >= y and y + z >= x:
    if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
        print("構成等腰三角形")
    elif x == y == z:
        print("構成正三角形")
else:
    print("無法構成三角形")
