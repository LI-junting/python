f=open("name&password.text","r")
stp=f.read()
print(stp)
f.close()
stp=stp.split(':')
print(stp)   #用：为标识分割字符串
stp.pop(0)
stp.pop(1)
newstp=stp
print(newstp)

for i in range(3):
    name=input("请输入账号：")
    pwd=input("请输入密码：")
    if name==newstp[0] and pwd==newstp[1]:
        print("恭喜您输入正确，正在进入系统！")
        break
    else: print("输入错误,请重新输入！")
else:
    print("您输入的次数太多，系统强制退出！")

