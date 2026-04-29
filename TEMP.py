name = input()
sid = input()

result = sum(int(ch) for ch in sid)
while result > 9:
    result = sum(int(d) for d in str(result))

list2 = [result * (ord(ch.upper()) - ord('A') + 1) for ch in name if ch.isalpha()]

while len(list2) > 1:
    for i in range(len(list2)//2):
        list2[i] += list2[-1-i]
    list2 = list2[:(len(list2)+1)//2]

print(list2[0])