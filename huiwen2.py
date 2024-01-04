num = int(input("请输入一个整数："))
num_str = str(num)
huiwen_num_str = num_str[ : :-1]
if huiwen_num_str == num_str:
    print("这是一个回文数。")
else:
    print("这不是一个回文数。")