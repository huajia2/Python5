import random
number = random.randint(0,100)
print("您一共有5次猜数的机会")
num = 5
while num > 0 :
    num2 = int(input("请输入您要猜的数字："))
    if num2 > number :
        print("大了")
    elif num2 < number :
        print("小了")
    else:
        print("恭喜您蒙对了！")
        break
    num = num - 1
    print(f"您还有{num}次机会！")


