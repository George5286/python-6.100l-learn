#lambda函数，临时函数，当函数比较简短，使用次数不多时可以使用

def do_twice(n,f):      #f是一个函数
    return f(f(n))
print(do_twice(3,lambda x:x**2))

#tuple元组  无法修改
te = ()    #空元组
a = (5)     #错误写法，此时py认为括号只是决定运算优先级
print(type(a),a)
b = (5,)            #正确写法
print(type(b),b)
t = (2,"mit",3)
t = t + (4,5,"edu")     #加法运算
print(t)
print(t[3:4])           #切片，从3号位开始，4号位结束（不包括）

# t = 324                 #t可以重新赋值，解除对元组的绑定，与新类型绑定在一起
# print(t)
# print(max(b))


m = "abcedfg"           #字符串也可以进行类似的操作
print(m[1:3])

seq = (2,"a",3,(1,2))   #嵌套
print(len(seq))
print(len(seq[3]))
print(seq[3][0])
print(seq[0:3:2])           #从0位开始，3位结束，步长位2

for i in seq:
    print(i)

x = 1
y = 2
(x,y) = (y,x)       #x和y交换

def a(x,y):
    m = x*y
    d = x/y
    return (m,d)
print(a(3,4))

def char_counts(s):
    """
    s是string，小写字母，返回 1.元音字母的数量 2.辅音字母的数量
    """
    an_letter = "aefhilmnorsx"
    num_an = 0
    for i in s:
        if i in an_letter:
            num_an += 1
    return(num_an,len(s)-num_an)

print(char_counts("aaaaaaaaa"))

#均值函数
def mean(*args):            #python中*args表示可变参数，传入的参数会被打包成一个tuple
    """
    args是多个参数，返回均值
    """
    print(type(args))      #args是一个tuple
    return sum(args)/len(args)
print(mean(1,2,3,4,5))

#lists列表，列表是可变的
a_list = [1,2,3,[4,5],"a"]
a = [1,2] + [3,4] + [5]
print(a)

def list_sum(l):
    """
    l是一个list，返回list中所有元素的和
    """
    total = 0
    for i in l:
        total += i
    return total
print(list_sum([1,2,3,4,5]))

a_list[3] = 10
a_list.append(11)        #在列表末尾添加元素11,但作为函数，它不会返回任何值，即None
print(a_list)

a_list.extend([3,4])        #直接在a_list后面追加新的列表

def make_ordered_list(n):
    """
    n是一个正数，返回从0到n的列表
    """
    a = []
    for i in range(n+1):
        a.append(i)
    return a
print(make_ordered_list(6))

def remove_elem(l,e):
    """
    l是一个列表，输出l列表剔除e的新列表
    """
    a = []
    for i in l:
        if i != e:
            a.append(i)
    return a
print(remove_elem([1,2,3,4,5],5))

#string 转化成list
s = "i like apples"
l = list(s)             #直接转化为列表，每个字符为一个元素
print(l)
l = s.split(" ")        #将s字符串以“ ”作为分割转化成列表
print(l)
#list 转化成string
print(" ".join(l))      #使用.join函数可以将list中每个元素以“ ”为间隔分开
print("_".join(l))      #.join只适合包含字符串元素的列表
print("".join(l))

def count_words(sen):
    """
    sen是一个句子，返回这个句子有多少个单词
    """
    newlist = sen.split(" ")
    return len(newlist)
print(count_words("i like apples , apples are good for our health"))

#sort函数，给list里面的元素排序
l = [2,4,9,1,3]                     #升序排序
string = ["apple","egg","b"]        #首字母排序
l.sort()
string.sort()
print(l,string)
#sorted函数，排序时会创建副本，不影响原来的list
l = [2,4,9,1,3]
l1 = sorted(l)
print(l1)
#reverse()函数，倒转list里面的元素
l.reverse()
print(l)

def square_list(l):
    """
    将列表中的数字全部平方
    """
    for i in range(len(l)):
        l[i] = l[i]**2
l = [1,2,3,4,5]
square_list(l)
print(l)

#清空列表
l.clear()       #使用这个函数时，l在内存中的位置没有发生改变（可以用id来查看位置）
print(l)