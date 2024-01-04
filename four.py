num = int(input("请输入一个四位数："))
if num > 1000 and num < 9999 :
    a = num//1000
    b = (num//100)%10
    c = (num//10)%10
    d = num%10
    if num == a**4 + b**4 + c**4 + d**4:
        print(num,"这是一个玫瑰数")
    else:
        print(num,"这不是一个玫瑰数")
else:
    print("请输入一个四位数：")