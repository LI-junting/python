lucky_num=19
while True:   #当永远为真时
    input_num=int(input("请输入数字："))
    if input_num==lucky_num:
        print("输入正确")
        break     #退出循环
    elif input_num>lucky_num:
        print("太大了")
    else :
        print("太小了")
