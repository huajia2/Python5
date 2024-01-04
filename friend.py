list_friend = []
print("1:添加好友")
print("2:删除好友")
print("3:备注好友")
print("4:展示好友")
print("5:退出")

while True:
    num = int(input("请输入您的选项："))
    if num == 1:
        friend = input("请输入需要添加的好友：")
        list_friend.append(friend)
        print(friend)
        print("好友添加成功！")
    elif num == 2:
        friend = input("请输入需要删除的好友：")
        list_friend.remove(friend)
        print(friend)
        print("删除成功！")
    elif num == 3:
        friend = input("请输入需要备注的好友：")
        list_friend.extend(friend)
        print(friend)
        print("备注成功！")
    elif num == 4:
        if len(list_friend) == 0:
            print("好友列表为空!")
        else:
            for friend in list_friend:
                print(friend)
    elif num == 5:
        print("退出")
        break
   


