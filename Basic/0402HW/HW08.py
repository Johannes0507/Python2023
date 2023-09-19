content = {"A":"樂觀","B":"悲觀","O":"自信","AB":"聒噪"}

blood = input("請輸入血型：")

blood = blood.upper()

if content.get(blood) == None:
    print("找不到血型：",blood)
else:
    print(blood,content[blood])
