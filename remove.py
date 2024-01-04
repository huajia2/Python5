list_two = ['1','w','e','5','d','8','5','5']
# set可以自动去除重复的元素，只保留一个
list_three = list(set(list_two))
# 使用tuple()函数创建数组时，不传入任何数据，就回创建一个空元组；如果要创建包含元素的数组即必须传入可以迭代类型
print(tuple(list_three))


