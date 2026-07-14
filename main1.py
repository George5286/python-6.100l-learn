find = int(input("what number to find the cube of: "))
guess = float(input("start with: "))
print("current estimate cubed:", guess**3)
print("next guess to try:", (find/guess**3+guess)/2)

#牛顿迭代法