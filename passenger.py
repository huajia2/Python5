while True:
 print("乘客买票请输入1")
 print("乘客没有买票请输入2")
 print("乘客携带危险物品请输入3")
 print("乘客没有携带危险物品请输入4")
 pass_num = int(input("乘客是否买票："))
 if pass_num == 1 :
    print("乘客已经买票，允许近站。")
    if pass_num == 4:
        print("乘客顺利进站！")
 elif pass_num == 3:
    print("乘客携带危险物品，不允许进站！")
    break
 elif pass_num == 2 :
    print("乘客没有买票，不允许进站！")
    break
    continue