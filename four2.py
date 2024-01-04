
while True:
    # num1=8765
    # # c=a//b
    # a = num1 // 1000
    # b = (num1 // 100) % 10
    # c = (num1 // 10) % 10
    # d = num1 % 10
    # print(a,b,c,d)

    num = int(input("请输入一个四位数"))
    if 1000 < num < 9999 :
     a = num // 1000
     b = (num//100)%10
     c = (num//10)%10
     d = num % 10
     if num == a**4 + b*b*b*b + c*c*c*c + d*d*d*d :
        print("这是一个玫瑰数")
        continue
     else:
        print("它不是一个玫瑰数")
        continue

