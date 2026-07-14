for n in range(5):
    print(n)
print(" ")

#for i in range(start,stop,step)
#range 遍历
for i in range(1,4,2):
    print(i)


print(" ")
n = [1,2,3,4,5]

for i in n:
    print(i)

start = int(input("start: "))
end = int(input("end: "))
summ = 0
for i in range(start,end+1):
    summ += i
print(summ)

#factorial
x = int(input("x: "))
out = 1
for i in range(1,x+1):
    out *= i
print(out)

#conclusion:for loop is useful for exact loop time,and  while loop is fit for unexact time