# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     count = 0
#     while left <= right:
#         mid = (left + right) // 2
#         count += 1
#         if arr[mid] == target:
#             return mid, count
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1, count

# # example usage
# my_list = [2, 4, 6, 8, 10]
# target = 8
# index, count = binary_search(my_list, target)
# print("Target found at index", index, "after", count, "comparisons.")

def mid(a,b):
    if a > b:
        return("相乘：",a*b) 
    elif a < b:
        return("相加：",a+b)
     

x = mid(50,100)
print(x)

y = mid(100,50)
print(y)
    