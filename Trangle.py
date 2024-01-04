x = int(input("请输入三角形的第一条边："))
y = int(input("请输入三角形的第二条边："))
z = int(input("请输入三角形的第三条边："))
q = (x+y+z)/2
s = (q*(q-x)*(q-y)*(q-z))**0.5
print(f"三角形的半周长是{q}")
print(f"三角形的面积是{s}")