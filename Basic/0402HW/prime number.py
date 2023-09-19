for i in range(2,1000):
    if (i > 2) and (i % 2 == 0):
        continue
    elif (i > 3) and (i % 3 == 0):
        continue
    else:
        print(i)
    print()