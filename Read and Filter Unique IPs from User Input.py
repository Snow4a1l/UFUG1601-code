import sys
IPlist=[]
lines = sys.stdin.readlines()
while lines is not None:
    lines = sys.stdin.readlines()
    if lines is not None:
        for line in lines:
            line = line.strip()
            if line != "":
                if line not in IPlist:
                    IPlist.append(line)

print("Total IPs found (with duplicates): " + str(len(lines)))
