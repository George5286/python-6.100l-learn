#复制列表（创建副本）
l = [1,2,3,4]
m = l[:]
def remove_all(l,e):
    """
    l是一个列表，e是要剔除的元素
    """
    m = l[:]
    l.clear()
    for i in range(len(m)):
        if m[i] != e:
            l.append(m[i])
    return None
print(l)
remove_all(l,2)
print(l)

#删除元素
l = [2,1,3,6,3,7,0]
del(l[0])       #删除l列表中索引为0的元素
l.remove(3)     #删除l列表中是3的元素（如果有多个3，只会删除索引最小的那个）
l.pop()         #删除最后一个元素（空值），也可以删除指定索引的元素，作为函数会返回被删元素的值
print(l)
#改进remove_all函数
def remove_all(l,e):
    while e in l:           #注意，这里不要用for来遍历，for在list中的机制是遍历索引，边遍历边修改可能会造成问题
        l.remove(e)
    return None
l = [0,3,3,3,1]
remove_all(l,3)
print(l)

#别名
l = [1,2,3,4,5]
m = l                   #m是l的别名，m和l指向同一个列表
l.append(3)
print(l,m)

#浅复制和深复制
old_list = [[1,2],[3,4]]
new_list = old_list[:]          #浅复制，复制了列表的第一层，第二层仍然是引用
#new_list = copy.copy(old_list)         #等价于上一条
print("new_list:",new_list)
print("old_list:",old_list)
new_list.append([5,6])                #在new_list中添加一个新列表[5,6]
print("new_list:",new_list)
print("old_list:",old_list)
new_list[0][0] = 100                   #修改new_list中第一个列表的第一个元素
print("new_list:",new_list)
print("old_list:",old_list)


import copy
#深复制
old_list = [[1,2],[3,4]]
new_list = copy.deepcopy(old_list)          #深复制，复制了列表的所有层
