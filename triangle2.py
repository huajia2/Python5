# for i in range(1,4) :
#     for j in range(i):
#         print("*",end=" ")
#     print()
# print("--------------------------")
# for i in range(1,4) :
#         print(" "*(4-i),"*"*(2*i-1))
for i in range(1,4) :
    for j in range(i) :
        print("*",end=" ")
    print()
print("________________________________")
for i in range(1,4) :
    print(" "*(4-i),"*"*(2*i-1))
for i in range(1,10) :
    for j in range(1,i+1) :
        print(f"{j}*{i}={j*i}",end=" ")
    print()