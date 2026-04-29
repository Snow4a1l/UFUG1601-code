import sys

lines = sys.stdin.readlines()

list1 = []
for line in lines:
    list1.append(line.strip())
print("[" + "'" + list1[0] + "'", end="")
for i in range(1, len(list1)):
    print(", " + "'"+list1[i]+"'", end="")
print("]")
