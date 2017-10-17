#
# f=open("test.log","w") #写入模式
# f.write("this is the first line\n")
# f.write("this is the second line\n")
# f.write("this is the third line\n")
# f.write("this is the four line\n")
# f.write("this is the five line\n")

# f=open("test.log","r")#只读模式
# print (f.read())

# f=open("test.log","a") #追加模式
# f.write("6\n")
# f.write("7\n")

f=open("test.log","w+")
f.write("new line\n")
print(f.readline())
f.close()
