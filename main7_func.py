#def定义函数
#even偶数，odd奇数
def is_even(i):
    return i % 2 == 0
#整除
def div_by(n,d):
    return n % d == 0

print(div_by(10,2))

#在a到b中的奇数相加
def sum_odd(a,b):
    temp = 0
    for i in range(a,b+1):
        if i%2 != 0:
            temp += i
    return temp
print(sum_odd(1,5))

#如果函数没有return任何值，python会返回None（nonetype类型） return None
#interesting:pirnt作为一个函数本身不会return任何值
print(print(5))

def count_unms_with_sqrt_close_to(n,epsilon=0.01):   #写成(n,epsilon=0.01)时，用户不输入epsilon时默认epsilon=0.01
                                                    #默认参数必须放在非默认参数的后面
    """                                                 
    在n的范围内,有多少整数的平方根落在这个范围

    """
    temp = 0
    temp1 = 0
    flag1 = False
    flag2 = False
    for i in range(n**3):
        if (n - epsilon)**2 < i < (n + epsilon)**2:
            temp += 1    
        if temp1 != temp:
            flag1 = True
        if flag1 == True and temp1 == temp:
            break
        temp1 = temp
    return temp
#calling the function
print(count_unms_with_sqrt_close_to(10,0.1))
print(count_unms_with_sqrt_close_to(10))  # 使用默认的epsilon值
print(count_unms_with_sqrt_close_to(10,epsilon=0.001))
print(count_unms_with_sqrt_close_to(n=10,epsilon=0.001))

#如果函数中没有相关变量，他会到外层作用域寻找相关变量直到找到为止
#函数可以访问超出自身的变量，但是不能修改
x = 1
def app(b):
    print(x)
print(app(1))
#函数的类型是function
print(type(app),type(x))
#可以对function进行运算
abcd = app      #引用名称，没有调用函数
print(abcd(1))

#一个经典的例子
def clac(op,x,y):       #op作为变量传递了add函数进去
    return op(x,y)
def add(x,y):
    return x+y
print(clac(add,5,3))

#函数返回函数（链式）
def make_prod(a):       #看不懂内存关系的回到12集40：00
    def g(b):
        return a*b
    return g
val = make_prod(2)(3)
print(val)