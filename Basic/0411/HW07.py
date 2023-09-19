scores = {'David':99,'Tom':88}

scores['Bill'] = 90

scores.setdefault('Peter')

print("分數",scores)

print()

scores['Peter'] = 61

# update   更新(增加)
scores.update({'Mary':91,'Sue':86})

print(scores)

print("依姓名排序")
for key in sorted(scores):
    print("%-10s %d" % (key,scores[key]))

scores.pop("Bill")
print()

for key in sorted(scores,reverse = True):
    print("%-10s %d" % (key,scores[key]))

print("字串清除：",scores.clear())

scores.updpte()


