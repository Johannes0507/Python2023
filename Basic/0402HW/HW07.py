students = {"Tom":40,"Judy":100,"Bill":66}
print(students["Tom"])
print()
print(students)

fruit = {}
fruit[0] = "John"
num = dict()
num[1] = "Johannes"
print(num)
print(fruit[0])
print()

students.pop("Tom")
print(students)

print()
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 修改键 'a' 的值为 4
my_dict['a'] = 4

# 修改键 'b' 为 'new_key'，并将其值设置为 5
my_dict['new_key'] = my_dict.pop('b')
my_dict['new_key'] = 5

print(my_dict)