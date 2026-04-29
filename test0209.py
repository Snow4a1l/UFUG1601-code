import time 
import random
text="Hello World"
result=""
list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
for ch in text:#遍历text中的每个字符
    for i in random.sample(list, len(list)):
        print(result+i)
        if ch==i:
            time.sleep(0.3)
            result += ch
            break