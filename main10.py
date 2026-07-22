#列表推导式
squares = [x**2 for x in range(10)]         #列表推导式的基本语法是：[表达式 for 变量 in 可迭代对象 if 条件]，其中if条件是可选的。
print(squares)                              #快速创建列表的方式，效率高于for循环
a = [x*2 for x in range(10) if x%2==0]          #列表推导式中可以加条件
print(a)
