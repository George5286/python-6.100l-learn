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