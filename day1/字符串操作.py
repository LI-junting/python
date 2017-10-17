name=input("name:")
age=int(input("age:"))
job=input("job:")

# print("李军挺的信息：\n名字：",name,"\n年龄是：",age,"\n工作是：",job)  为每个变量新建内存空间
print("%s的信息：\nName:%s\nAge:%s\nJOB:%s"%(name,name,age,job))  #通过%s来引用前面变量的数值
#通过三个单引号 来实现段落的格式化输出
msg='''  
%s的信息：
    Name:%s
    Age:%s
    JOB:%ss
''' %(name,name,age,job)
print(msg)