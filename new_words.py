# 创建一个空字典来存储单词和它们的翻译
vocabulary = {}


# 查看生词列表功能
def view_vocabulary():
    if not vocabulary:
        print("生词本内容为空")
    else:
        for word, translation in vocabulary.items():
            print(f"单词: {word}, 翻译: {translation}")

def recall_word():
    if not vocabulary:
        print("生词本内容为空")
        return
    word, translation = list(vocabulary.items())[0]
    user_input = input("请输入该单词的翻译: ")
    if user_input == translation:
        print("太棒了！")
    else:
        print("再想想。")
3
def add_word():
    new_word = input("请输入新单词: ")
    new_translation = input("请输入新单词的翻译: ")
    if new_word in vocabulary:
        print("此单词已存在。")
    else:
        vocabulary[new_word] = new_translation
        print("单词添加成功。")

def delete_word():
    if not vocabulary:
        print("生词本内容为空")
        return
    word_to_delete = input("请输入要删除的单词: ")
    if word_to_delete in vocabulary:
        del vocabulary[word_to_delete]
        print("删除成功。")
    else:
        print("删除的单词不存在。")

def clear_vocabulary():
    if not vocabulary:
        print("生词本内容为空")
    else:
        vocabulary.clear()
        print("生词本已清空。")
def exit_program():
    print("退出生词本。")
    exit()
while True:
    print("\n生词本功能选择:")
    print("1. 查看生词列表")
    print("2. 背单词")
    print("3. 添加新单词")
    print("4. 删除单词")
    print("5. 清空生词本")
    print("6. 退出生词本")
    option = input("请输入选项编号: ")
    if option == "1":
        view_vocabulary()
    elif option == "2":
        recall_word()
    elif option == "3":
        add_word()
    elif option == "4":
        delete_word()
    elif option == "5":
        clear_vocabulary()
    elif option == "6":
        exit_program()
    else:
        print("无效的选项。请重新输入。")