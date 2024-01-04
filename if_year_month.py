year = int(input("请输入年份："))
month = int(input("请输入月份："))
if month in [1,3,5,7,8,10,12] :
    print(f"{year}年{month}月有31天")
elif month in [4,6,9,11] :
    print(f"{year}年{month}月有30天")
elif month == 2 :
    if(year%400 == 0 ) or (year%4 == 0 and year%100 != 0) :
        print(f"{year}年{month}月有29天")
    else:
        print(f"{year}年{month}月有28天")
