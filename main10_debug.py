#debug
#IndexError: 表示索引超出范围，通常是因为访问了一个不存在的索引位置。
#TypeError：表示类型错误，通常是因为对不支持该操作的数据类型执行了操作。
#NameError：表示名称错误，通常是因为使用了未定义的变量或函数名。
#ValueError：表示值错误，通常是因为传递了不合适的值给函数。


try:                    #尝试执行可能出错的代码,如果出现异常，则会跳转到except块中执行相应的处理代码
    print(1/0)
except ZeroDivisionError:    #捕获除以零的异常
    print("除以零错误")
except:
    print("其他错误")
else:                 #如果try块中没有异常发生，则会执行else块中的代码
    print("没有错误")
finally:             #无论是否发生异常，都会执行finally块中的代码
    print("执行结束")

def pairwise_div(Lnum,Ldenom):
    """
    计算两个列表中对应元素的商，并返回一个新的列表。
    """
    assert len(Lnum) == len(Ldenom), "两个列表长度不一致"
    assert len(Lnum) and len(Ldenom) > 0, "列表不能为空"
    try:
        l = [Lnum[i]/Ldenom[i] for i in range(len(Lnum))]
    except:
        raise ValueError("不能除以0")
    return l
print(pairwise_div([4,5,6],[1,0,3]))

#断言（强制判断条件是否为真，不符合直接报错，通常用在函数中判断输入值是否符合要求）
def divide(a, b):
    assert b != 1, "除数不能为1"  #断言b不等于1，如果b等于1，则抛出AssertionError异常，并显示指定的错误信息
    return a / b
print(divide(10, 1))