# num = int(input("请输入一个整数："))
# for i in range(2, num):
#     if num > 1 :
#         for j in range(2, int(i ** 0.5) + 1): #不能被2到它自身的平方根之间的任何数字整除
#             if i % j == 0:
#                 break
#         else:
#             print(i,end=" ")
num = int(input("请输入一个整数："))
for i in range(2,num) :
    for j in range(2 , int(i ** 0.5) + 1):
        if i % j == 0 :
            break
        else:
            print(i,end = " ")