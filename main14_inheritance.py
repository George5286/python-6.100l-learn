class animal(object):
    def __init__(self,age):
        self.age = age      #实例变量
        self.name = None
    def get_name(self):     #获取器
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age):      #设置器
        self.age = age
    def set_name(self,name = ""):
        self.name = name
    def __str__(self):
        return f"animal:{self.name},{self.age}"

class cat(animal):      #继承了animal类(父类)的所有方法
    def speak(self):
        print("miao")
    def __str__(self):      #子类可以重写父类的方法
        return f"cat:{self.name},{self.age}"

class person(animal):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.friend = []
    def __str__(self):
        return f"person:{self.name},{self.age}"
    def add_friend(self,other):
        self.friend.append(other)
    def del_friend(self,n):
        self.friend.remove(n)
    def speak(self):
        print("hello")
    def __str__(self):
        return f"person:{self.name},{self.age}"

class student(person):
    def __init__(self, name, age,major = ""):
        person.__init__(self,name,age)      #直接调用person的方法来初始化name和age
        self.major = major
    def __str__(self):
        return f"student:{self.name},{self.age}"

class rabit(animal):
    tag = 1     #类变量
    def __init__(self, age,p1 = "",p2 = ""):
        animal.__init__(self,age)

        self.id = rabit.tag     #给每只兔子打上id
        self.p1 = p1
        self.p2 = p2
        rabit.tag += 1
    def __add__(self,other):        #定义加法，交配
        return rabit(0,self,other)
    def __str__(self):
        return f"rabit:{self.name},{self.age}"
    def __eq__(self,other):     #验证是否是同一个爸妈，此处定义的是双引号
        return (self.p1.id == other.p1.id and self.p2.id == other.p2.id) or (self.p1.id == other.p2.id and self.p2.id == other.p1.id)


a = animal(2)
print(a)

def make_animals(l1,l2):
    """
    传入两个列表，一个年龄，一个名字，转换为animal类型存入新列表
    """
    l3 = []
    for i in range(len(l1)):
        l3.append(animal(l1[i]))
        l3[i].set_name(l2[i])
    return l3

l1 = [1,2,5]
l2 = ["a","b","c"]
l3 = make_animals(l1,l2)
for i in range(3):
    print(l3[i])

c = cat(3)
c.set_name("ha_ji_mi")
print(c)
c.speak()

r1 = rabit(3)
r2 = rabit(1)
print(r1.id,r2.id)
r3 = r1 + r2
print(r3.p1.id)