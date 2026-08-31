#自定义类型 class(类)

#1.类型：数据类型，eg：int，str，float，list，dictionary
#2.对象：真实存在于内存中，eg：a = 10,10是对象
#3.实例：a = 10，10是int的实例，对象的
#interesting，类型也是对象，如
print(type(int))        #返回type，说明int是type的实例
print(type(type))

#一个对象由数据，方法组成

class coordinate(object):               #定义类型，但没有创建实例
    """
    坐标类
    """
    def __init__(self,xval,yval):       #方法（用self来表示未创建的实例）
        self.x = xval                      #如果没有使用self，在函数执行结束后就消失
        self.y = yval

    def distance(self,other):           #专门用来处理coordinate类型的函数（方法），计算两点间的距离
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def to_origin(self):
        self.x = 0
        self.y = 0
    def __str__(self):
        return f"<{self.x},{self.y}>"

class cercle(object):
    """
    圆类
    """
    def __init__(self,c,r):
        assert type(c) == coordinate and type(r) == int
        self.c = c
        self.r = r
    def in_cercle(self,point):
        return point.distance(self.c) < self.r

class fraction(object):
    """
    分数类
    """
    def __init__(self,a,b):
        self.a = a      #分子
        self.b = b      #分母
    def __str__(self):      #分析print,返回必须是str
        if self.b == 1:
            return str(self.a)
        else:
            return f"{self.a}/{self.b}"
    def __mul__(self, other):       #定义乘法*（星号）
        top = self.a * other.a
        bottom = self.b * other.b
        return fraction(top,bottom)     #返回fraction类型
    def __float__(self):
        return self.a/self.b
        



c = coordinate(3,4)                     #创建实例c
origin = coordinate(0,0)                #创建实例origin
print(c.x,c.y)                          #访问实例c的属性
 
print(c.distance(origin))               #点运算符，c传给self，这个方法设计上是给 coordinate 类型的实例使用的
print(coordinate.distance(c,origin))    #两者的效果一样（我必须传入c来作为self，因为点号前面不是实例而是类名）
coordinate.to_origin(c)
print(c.x,c.y)

c = coordinate(3,4)
my_cercle = cercle(c,3)
print(my_cercle.r)

print(c)        #只是输出地址，我们想要坐标,用__str__特殊函数可以定义print怎么输出
print(isinstance(c,coordinate))     #用isinstance函数检查c是不是coordinate类型

a = fraction(1,3)
b = fraction(2,5)
print(a,b)
print(a*b)
print(a.__mul__(b))     #也可以这样写
print(float(a))