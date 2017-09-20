for j in range(5):
    for i in range(10):
        if i <5:
            continue    #跳出本次循环，继续执行下一次循环  break是结束该层的整个循环
        if j > 3:
            break
        print(i)