def login(account,password,num):
    while num>0:
        name_account = input('请输入账号：')
        num_password = input('请输入密码：')
        if name_account == account :

            if num_password == password :
                print("登录成功")
            else:
                print("用户名或密码错误！")
                break
        else:
            print("用户密码错误！你还有"+str(num)+"次机会。")
            num = num-1
    print("输入次数过多，请稍后再试")
login('123456','654321',3)

