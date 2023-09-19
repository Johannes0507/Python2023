scores = [100,60,70,80,99,100,66,100,100,60,80]
start = 0
while True:
    print(scores)
    a = int(input("輸入要移除的數字,exit離開："))
    if a == exit:
        break
    for i in range(scores.count(a)):
        index = scores.index(a,start)
        scores.pop(index)

    