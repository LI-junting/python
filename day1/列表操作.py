job=['gongchengshi','chushi','caifeng']
print(job[0])
print(job[2])

job.append("jiaoshi")  #增加元素到列表里面，默认增加在最后一个
print(job)

num=job.index("jiaoshi") #查找“jiaoshi”在列表的位置即索引值 第一个为 “0”
print(num)

count=job.count("jiaoshi") #统计列表元素为“jiaoshi”的数量
print(count)

job.insert(2,'getihu') #在第三个位置插入一个名为“getihu”的元素
print(job)

job.remove("chushi") #删除列表中为元素名为“chushi”的元素
print(job)

job.reverse() #将元素位置翻转
print(job)

job.sort() #按照ASCII码进行排序
print(job)

job.insert(5,"64brother")
job.insert(1,"64brother")
print(job)

for i in range(job.count('64brother')):
    job.remove('64brother')
print(job)