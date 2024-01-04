x = float(input("请输入第一条边"))
y = float(input("请输入第二条边"))
z = float(input("请输入第三条边"))
q = (x+y+z)/2
s = (q*(q-x)*(q-y)*(q-z))**0.5
print("三角形的周长为：",q)
print("三角形的面积为:",s)


