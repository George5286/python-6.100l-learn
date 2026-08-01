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