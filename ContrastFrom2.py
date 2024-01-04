# while True :
#     num_list = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖']
#     result = ''
#     number = input('输入一个数字：')
#     for i in range(len(number)):
#         num = int(number[i])
#         result += num_list[num]
#     print('转换结果为：',result)

while True :
    num_list = ['零','壹','贰','叁','肆','伍','陆','柒','捌','玖','什']
    result = ''
    num = input('请输入一个数字：')
    for i in range(len(num)) :
        new_num = int(num[i])
        result = result + num_list[new_num]
    print(result)