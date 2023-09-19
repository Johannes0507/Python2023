n = int(input("幾層？"))

data = [1]

for i in range(n):
    print(data)     # 印出data
   
    plist = []  # 創建一個空串列
    
    plist.append(data[0])   # 加入位子第0 data[1]
    
    for i in range(len(data)-1):
        plist.append(data[i]+data[i+1])
    
    plist.append(data[-1])
    
    data = plist    # 繼承上一個迴圈的長度
    
    