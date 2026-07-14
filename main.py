a = "abc"
print(len(a))
print(a[-1])
print(a[len(a)-1])
b = 1
print(a + str(b))
text = input(b)
#print(type(int(text)))

#if you use input,it always returns type of string
#if you want change decimal to int,just need to through str-float-int
print(int(float(text)))

verb = input("please type a verb: ")
print("I can", verb ,"better than you!")
print((verb+" ")*4 + verb)