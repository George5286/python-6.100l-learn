where = input("go right or left: ")
n = 1
while where == "right":
    where = input("go right or left: ")
    n += 1
    if n >= 2:
        print("it has something wrong")
print("that's right,you get out the loop")


x = int(input("type number to calculate x!: "))
z = x
y = 1
while x >= 1:
    y = y*x
    x -= 1
print(f"{z} factorial is {y}")

a = 0
while a < z:
    print("hello world")
    a += 1
