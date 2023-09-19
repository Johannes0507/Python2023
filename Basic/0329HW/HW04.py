scores = [100,60,70,80,99,100,66]
while True:
    print("目前內容：",scores)
    i = int(input("輸入要移除的數字空格跳出："))
    if i == "":
        break
    if scores.count(i) > 0:
        a = scores.index(i)
        scores.pop(a)
    else:
        print("找不到此數字")
