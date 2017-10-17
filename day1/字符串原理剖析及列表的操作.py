import  sys
print(sys.argv)

#创建列表
lb_1=[1,2,3,4,5,6]   #直接赋值
lb_2=list((1,2,3,4,5,6))  #通过list创建列表，list里面只能包含一个数据，用（）进行数据分个成诺干元素
lb_3=list(((1,2,3),(4,5,6)))

print(lb_1)
print(lb_2)
print(lb_3)


#列表的操作有一下几种：
'''
    索引    index
    切片    :
    追加    append
    删除    del , remove ,pop
    长度    len 
    循环    for , while ,   break,continue,pass,return,exit
    包含    in , _contains_
'''
#元组的操作跟列表基本上相同，但是元组的元素不能修改
t1=(1,2,{'k1':'v1','k2':'v2'},{'k2':'v2'})
# t1[2]=123 他表示字典元素
t1[2]['k1']=2  #元组的元素的元素是可以修改的
t1[2]['k2']=3
t1[3]['k1']=1
print(t1)

#字典 是靠 键值对 来进行索引
'''
    新增  d[key] XXX
    删除  del  d[key]
    键、值、键值对
          keys values  items
          for k,v in dic.keys
    循环  for ...
    长度  len 


'''