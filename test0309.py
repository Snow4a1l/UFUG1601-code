'''
#list1=[1,2,3,4,5]
#print(list1[4])
#if 5 in list1:
#    print("5 is in the list")
#print(list1.index(3))
#print(list1.count(2))
#list1.append(6)
#list1.extend([7,8])
#list1.insert(-1,-3.5)
#print(list1)

###

list1=[1,5,3,4,2]
#list1[2:3] = [10,11,12]
#print(list1)

list1.remove(3)
print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)
'''

'''
lst = [10, 12, 23, 54, 15]#设置lst为一个列表，包含5个元素
lst.append(7)#在lst的末尾添加一个元素7
lst.extend([8, 9, 3])#在lst的末尾添加一个列表[8, 9, 3]中的元素
lst.insert(2, 2.75)#在索引为2的位置插入元素2.75
lst.remove(3)#移除第一个值为3的元素
print(lst.pop())#弹出并返回最后一个元素
print(lst.pop(4))#弹出并返回索引为4的元素
lst[1:5] = [20, 21, 22]#将索引为1到4的元素替换为[20, 21, 22]
lst2 = [4, 6, 8, 2, 0]
lst2.sort()#对lst2进行排序
lst2.reverse()#将lst2反转
lst3 = lst2#lst3指向lst2的同一个列表对象
lst4 = lst2[:]#lst4是lst2的一个副本
lst2[-1]= 17#将lst2的最后一个元素修改为17
print(lst2)
print(lst3)
print(lst4)
'''
def cent_to_fahr(cent):
    return cent / 5.0 * 9 + 32
ctemps = [-40, 0, 20, 37, 100]
# Goal: set ftemps to [-40, 32, 68, 98.6, 212]
ftemps = [cent_to_fahr(c) for c in ctemps]
print(ftemps)


list2= [1, 2, 3, 4, 5]
list2.insert(-1, 10)
print(list2)
