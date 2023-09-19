# 字典深層式

score = {'Tom':95,'Bill':78,'John':47,'Eward':67,'Eric':52,'Ivy':67,'David':87}

print('及格有\n',{k:v for k,v in score.items() if v >= 60})
print('不及格有\n',{k:v for k,v in score.items() if v <= 60})   # \n 空行

print()

minScores = min(zip(score.values(),score.keys()))
maxScores = max(zip(score.values(),score.keys()))

print(minScores)
print(maxScores)

# zip 合併

d1 = [1,2,3]
d2 = [4,5,6]

maxD = zip(d1,d2)
print(list(maxD))

