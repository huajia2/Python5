# list_one = ['1','w','e','5','d','8','5','5']
# a = 0
# max_str = 0
# for i in list_one:
#     if list_one.count(i)>a:
#         a = list_one.count(i)
#         max_str= i
# print("出现次数最多的是"+str(max_str)+",次数为："+str(a))
list_two = ['a','d','d','d','r','q','q','m']

a = 1
for i in list_two :
    if list_two.count(i)>a:
        c = list_two.count(i)
        for j in range (c-1) :
            list_two.remove(i)
        # b = i
        # list_two.remove(b)
print(tuple(list_two))
# list_two = list(set(list_two))
# print(list_two)
