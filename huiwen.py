num = int(input("请输入一个整数"))
num_str = str(num)
reverse_str=num_str[::-1]
if reverse_str == num_str:
    print(num,"是一个回文数")
else:
    print(num,"不是一个回文数")

