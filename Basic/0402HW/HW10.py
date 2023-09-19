data = [80,60,70,90,49,33,89]

start = 0 # 第一個位置

end = len(data) -1  # 串列最後一個位置

data.sort(reverse = False)  # 把串列從小排到大

while True: # 如果最終位置大於等於初始位置就啟用迴圈

    find = int(input("輸入要尋找的值："))

    mid = (end + start) // 2  # 找出串列的中間位置

    if data[mid] == find:
        print("找到了")
        break

    elif find > data[mid]:
        start = mid + 1

    else:
        end = mid - 1
        
        

            
        

    




    
            
        

