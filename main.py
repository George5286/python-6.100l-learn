a = "abc"
print(len(a))       #len函数，返回字符串长度
print(a[-1])        #负数指引，输出c
print(a[len(a)-1])      #输出c
b = 1
print(a + str(b))       #+号可用于字符串连接
text = input(b)
#print(type(int(text)))

#if you use input,it always returns type of string
#if you want change decimal to int,just need to through str-float-int
print(int(float(text)))

verb = input("please type a verb: ")
print("I can", verb ,"better than you!")    #逗号会自动添加空格，可以连接不同类型
print((verb+" ")*4 + verb)