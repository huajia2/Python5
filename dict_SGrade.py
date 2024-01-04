dict_Grade = {}
print("1.查看学生成绩")
print("2.增加学生成绩")
print("3.修改学生成绩")
print("4.删除学生成绩")
print("5.退出系统")

while True :
    num  = int(input("请输入您要进行的选项"))
    if num == 1 :
        if len(dict_Grade) == 0 :
            print("学生的成绩表为空！")
        else:
            for Student,Grade in dict_Grade.items() :
                print(f"学生的姓名是{Student}，学生的成绩是{Grade}")
    elif num == 2 :
        Student = input("请输入学生的姓名：")
        Grade = input("请输入学生的成绩：")
        dict_Grade[Student] = Grade
        print(f"{Student}的成绩添加成功！成绩是{Grade}")
    elif num == 3 :
        Student = input("请输入要修改成绩的学生姓名：")
        Grade = input("请输入要修改的成绩")
        if Student in dict_Grade.items() :
            dict_Grade.update({Student:Grade})
            print(f"{Student}成绩修改成功！新的成绩为{Grade}")
        else:
            print("没有该名学生！请重新输入：")
    elif num == 4 :
        Student = input("请输入想要删除成绩的学生：")
        if Student in dict_Grade:
            del dict_Grade[Student]
            print("该学生的成绩删除成功")
    elif num == 5 :
        print("退出系统！")
        break
