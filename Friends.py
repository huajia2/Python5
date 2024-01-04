print("欢迎使用好友管理系统")
print("1:添加好友")
print("2:删除好友")
print("3:备注好友")
print("4:展示好友")
print("5:退出")
list_friends = []

while True:
    num = int(input("请输入您要进行操作的选项："))
    if num == 1 :
        friend = input("请输入要添加的好友：")
        list_friends.append(friend)
        print(list_friends)
        print("好友添加成功")
    elif num == 2 :
        friend = input("请输入要删除还有的姓名：")
        list_friends.remove(friend)
        print(list_friends)
        print("删除成功")
    elif num == 3 :
        if friend in list_friends:
            friend = input("请输入要修改的好友姓名：")
            new_friend = input("请输入修改后的好友姓名：")
            list_friends.remove(friend)
            list_friends.append(new_friend)
            print(list_friends)
            print("备注成功")
        else:
            print("没有该好友")
    elif num == 4 :
        if list_friends == [] :
            print("好友列表为空")
        else:
            print(list_friends[:])
    elif num == 5 :
        print("已关闭好友系统")
        break

