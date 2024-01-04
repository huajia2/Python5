import random
num2 = 5
random_num = random.randint(1, 21)
print("请输入一个整数（你有5次机会）：")
while num2 > 0:
    num = int(input("请输入一个整数："))
    if num > random_num:
        print("很遗憾，你猜大了。")
    elif num < random_num:
        print("很遗憾，你猜小了。")
    else:
        print("恭喜，猜数成功！")
        break
    num2 -= 1
    print("你还有" + str(num2) + "次机会。")

