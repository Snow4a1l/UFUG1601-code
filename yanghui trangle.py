def triangle(n):
    all_line=[]
    all_line.append([1])
    for i in range(2,n+1):#i指的是行数
        all_line.append([1])#每行的第一个数是1
        for k in range(1,i-1):#k指的是每行的第k个数
            all_line[i-1].append(all_line[i-2][k-1]+all_line[i-2][k])
        all_line[i-1].append(1)#最后一个也是一

    result = []
    for i in range(len(all_line)):
        result.append(all_line[i])
    return result















n114514 = int(input())
print(triangle(n114514))
