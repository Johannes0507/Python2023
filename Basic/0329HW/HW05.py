number = []

while len(number) < 6 :
    a = int(input("請輸入六個數字不能重複,輸入exit跳出："))
    if a == exit:
        break    
    if number.count(a) < 1:
        number.append(a)
    else:
        print("xx")
print(number)

for i in range(5):
    for x in range(6 - i - 1):
        if number[x] < number[x+1]:
            number[x],number[x+1] = number[x+1],number[x]
print(number)



    