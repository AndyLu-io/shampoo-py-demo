# list1=[1,2,3,4]
# print(list1)
# print(list1[0])
# print(list1[3])
#
# list2=["tom", "jerry", 1, 2]
# print(list2)
# print(len(list2))

list3 = [[1, 2], ["test", "fast"]]
print(list3[1])

# def testMatrix(row, col):
#     matrix = [[0 for i in range(col)] for j in range(row)]
#
#     for i in range(row):
#         for j in range(col):
#             matrix[i][j] = i * col + j
#     print(matrix)
#
# testMatrix(2, 3)
# testMatrix(3, 2)

list4 = list(range(1, 20))
print(list4)

tuo1 = (1, 2, 3)
print(tuo1)


dict1 = {"name": "tom", "age": 10}
print(dict1)
print(dict1["name"])
for key in dict1:
    print(key, dict1[key])

for key, value in dict1.items():
    print(key, value)


year=int(input("请输入年份："))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("闰年")
else:
    print("平年")

