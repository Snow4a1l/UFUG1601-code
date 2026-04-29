import random
def count(a):
    N = len(a)
    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if a[i] + a[j] == 0:
                cnt += 1
    return cnt


a=[]
for i in range(1000):
    a.append(random.randint(-10,10))
b=[]
for i in range(1000):
    b.append(count(a))
c=0
for a in range(len(b)):
    c +=b[a]
print(c)
     