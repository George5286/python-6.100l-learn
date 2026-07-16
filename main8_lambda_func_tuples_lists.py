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
