fruits = ['香蕉','蘋果','香瓜','西瓜']
while True:
    print("目前水果種類：",fruits)
    i = input("移除水果空格返回：")
    if i == " ":
        break
    if fruits.count(i) > 0:
        fruits.remove(i)
    else:
        print("沒有此水果")
        