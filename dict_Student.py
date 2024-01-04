dict_Student = {}
print("1:查看学生成绩")
print("2:增加学生成绩")
print("3:修改学生成绩")
print("4:删除学生成绩")
print("5:退出系统")

while True:
    num = int(input("请输入您的选项:"))
    if num == 1:
        if len(dict_Student) == 0:
            print("未录入学生成绩！")
        else:
            for Student, Grade in dict_Student.items():
                print(f'学生 {Student} 的成绩是 {Grade}')
    elif num == 2:
        Student = input("请输入学生")
        grade = input("请输入成绩")
        dict_Student[Student] = grade
        print(f'学生 {Student} 的成绩添加成功！')
    elif num == 3:
        Student = input("请输入修改学生")
        grade = input("请输入修改成绩")
        if Student in dict_Student:
            dict_Student[Student] = grade
            print(f'学生 {Student} 的成绩修改成功！')
        else:
            print("该学生没有成绩记录！")
    elif num == 4:
        Student_Grade = input("请输入需要删除成绩的学生:")
        if Student_Grade in dict_Student:
            del dict_Student[Student_Grade]
            print(f'学生 {Student_Grade} 的成绩删除成功！')
        else:
            print("该学生没有成绩记录！")
    elif num == 5:
        print("成功退出系统")
        break