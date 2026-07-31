def find_grades(grades,students):
    """
    grades: 字典，存储学生的成绩,students: 列表，存储学生的姓名,返回一个列表，存储学生的成绩
    """
    assert grades != {} and students != [],"字典和列表不能为空"
    return [grades[name] for name in students]




d = {"Ana":"B","Matt":"C","Join":"B","KAty":"A"}        #字典格式，{key1：value1，key2：value2}，key相当于自定义索引
print(find_grades(d,["Ana","Matt"]))
#添加元素
d["Grace"] = "A"        #直接写，如果py找不到这个索引就会创建新的
#修改值
d["Grace"] = "B"        #直接改
#删除
del(d["Ana"])           #del函数
#查找
print("Grace" in d)     #返回bool
print("Ana" in d)

def find_in_L(L,k):
    """
    L是一个关于字典的列表，k是一个int，返回Ture如果存在key等于k，else return False
    """
    for i in L:
        if k in i:
            return True
    return False


d1 = {1:2,3:4,5:6}
d2 = {2:4,4:6}
d3 = {1:1,3:9,4:16,5:25}
print(find_in_L([d1,d2,d3],2))

#遍历字典中的keys
print(d.keys())     #return "dict_keys(['Matt', 'Join', 'KAty', 'Grace'])"
print(type(d.keys()))       #dect_keys是一种类型
#遍历字典中的值
print(d.values())
print(type(d.values()))
#遍历字典的每一个元素
print(d.items())
print(type(d.items()))

for i,k in d.items():
    print(i,k)

#别名
a = d
print(a)
#复制
a = d.copy()
a = {1:2}
print(a,d)
#key必须是唯一，不可变对象