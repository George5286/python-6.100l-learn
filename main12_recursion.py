#递归算法
#计算3*5可以转化成3+（3*4）再转化成3+3+（3*3）...3+3+3+3+(3*1)
def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a,b-1)
print(mult(3,5))

#递归就是不断将问题分解成形式相同但规模更小的子问题，直到达到基准情况

#计算指数
def power_recur(n,p):
    """
    n是底数，p是指数
    """
    assert n != 0 or p != 0,"输入错误"
    if p == 0:
        return 1
    else:
        return n*power_recur(n,p-1)
print(power_recur(2,13))

#计算阶乘
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))

#迭代法 for和while循环

#斐波那契数列（效率低）
def fib(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(fib(34))

#高效率(用字典来存储计算过的结果)
n = {1:1,2:1}
def fibe(x,n):
    if x in n:
        return n[x]
    else:
        temp = fibe(x-1,n) + fibe(x-2,n)
        n[x] = temp
        return temp

print(fibe(34,n))

def sum_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + sum_list(l[1:])

a = [0,1,2,3]
print(sum_list(a))

#扁平化列表
l = [[1,2],[3,4],[5,6,7]]
def flatten(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + flatten(l[1:])

print(flatten(l))

#x是否在l列表中
def in_lists(l,x):
    if len(l) == 1:
        return x in l[0]
    elif x in l[0]:
        return True
    else:
        return in_lists(l[1:],x)

print(in_lists(l,8))

#反转列表内的元素
def my_rev(m):
    if len(m) == 1:
        return m
    else:
        return my_rev(m[1:]) + [m[0]]       #将第一个元素放到最后面
print(my_rev([1,2,3,4,5]))

#使用递归时，确保每一个return返回的类型都是一样的