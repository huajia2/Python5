num = 3
name_account = 123456
num_password = 654321
while num > 0 :
    account = int(input("请输入用户账号："))
    password = int(input("请输入账号密码："))
    if name_account == account  :
        if num_password == password:
            print("账号登录成功！")
            break
        else:
            num = num - 1
            print(f"用户密码错误，您还有{num}次机会！")
else:
        print("输入错误次数过多，请稍后再试。")