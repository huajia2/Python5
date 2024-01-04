score = int(input("请输入您的会员积分："))
if score == 0:
    print("您不是会员！")
elif 0 < score < 2000:
    print("铜牌会员")
elif 2000 < score < 10000:
    print("银牌会员")
elif 10000 < score < 30000:
    print("金牌会员")
else:
    print('钻石会员')