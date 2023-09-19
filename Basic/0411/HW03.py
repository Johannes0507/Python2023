student = {"David":98,"Peter":60,"Mary":55}

print("Bill" in student)

print("Mary" in student)

print()

while True:
    search = input("請輸入學生名，q離開：")
    
    if search == 'q':
        break
    
    if search in student:
        print(search,"分數",student[search])
    
    else:
        score = int(input("請輸入分數："))
        student[search] = score

print(student)

