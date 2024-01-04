# def weather () :
#     print("*" * 13)
#     print("日期：4月8日")
#     print("温度：14~28°C")
#     print("空气状况：良")
#     print("*" * 13)
# weather()

# def modif_weather(today, temp, air_quality) :
#     print("*" * 13)
#     print(f"日期：{today}")
#     print(f"温度：{temp}")
#     print(f"空气状况：{air_quality}")
#     print("*" * 13)
# modif_weather('4月28日','14~28°C','良')

# def division (num_one,num_two) :
#     print(num_one / num_two)
# division(10,16)

# def info(name,age,address) :
#     print(f'姓名：{name}')
#     print(f'年龄：{age}')
#     print(f'地址：{address}')
# info(name='wo',age=18,address='河南')

# def connect (ip,port = 3306) :
#     print(f"连接地址为：{ip}")
#     print(f"连接端口为：{port}")
#     print(f"连接成功")
# connect('22.1.4.98.13.08')
# connect(ip='22.1.14.9.8.1.30.',port=5555)

# def test(*args) :
#     print(*args)                                   #不定长参数
# test("a",'a','b','3','你会发大财')

# def test(**kwargs) :
#     print(kwargs)                   #**kwargs调用函数时传入的所有参数被**kwargs接收后以字典的形式保存
# test(a = 1,b = "nihao",c = 7)

# def use_var() :
#     name = 'python'                               #局部变量只在函数内部有效
#     print(name)
# use_var()

# count = 10
# def use_var() :
#     print(count)                                #程序中的任何位置都可以访问全局变量
# use_var()
# print(count)

# count = 10
# def use_var() :
#     global count                          #使用关键字global进行声明全局变量，然后在修改
#     count += 10
#     print(count)
# use_var()


# def factorial (num) :
#     if num == 1 :
#         return  1                        #递归函数
#     else :
#         return num*factorial(num-1)
# print(factorial(5))

print(abs(-8))
list = (1,2,3,4,5,6,"zhangsan")
print(len(list))
print(ord('a'))
print(chr(97))




