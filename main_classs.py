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


c = coordinate(3,4)                     #创建实例c
origin = coordinate(0,0)                #创建实例origin
print(c.x,c.y)                          #访问实例c的属性

print(c.distance(origin))               #点运算符，c传给self，这个方法设计上是给 coordinate 类型的实例使用的
print(coordinate.distance(c,origin))    #两者的效果一样（我必须传入c来作为self，因为点号前面不是实例而是类名）