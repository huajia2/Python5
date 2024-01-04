# s = "hello lily"
# count_dict = {}
# for char in s :
#     if char in count_dict :
#         count_dict[char] +=1
#     else:
#         count_dict[char] = 1
# max_count = max(count_dict.values())
# max_char = []
# for char ,count in count_dict.items() :
#     if count == max_count:
#         max_char.append(char)
# print("出现的最多字符是：",max_char)
# print("出现次数：",max_count)
s = "hello World"
dict_S = {}
Max_num = 0
Max_char = 0
for char in s :
    if char in dict_S :
        dict_S[char] += 1
    else:
        dict_S[char] = 1
print(dict_S)
for char in s :
    if s.count(char) > Max_num :
        Max_char = char
        Max_num = s.count(char)
print("出现最多的字符是：",Max_char)
print("出现的次数是：",Max_num)

