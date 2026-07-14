# a = 0
# for i in range(1,11):
#     if i%2 == 0:
#         a += 1
# print(a)
#
# s = "abcdefg"
# #s is a string sequence
# for char in s:
#     if char == "a" or char == "e":
#         print("there is an a or e")
# #intention: there is a key word "in"
# for char in s:
#     if char in "ae":
#         print("there is an a or e")

# an_letter = "aefhilmnorsxAEFHILMNORSX"
# word = input("Enter a word you are really like: ")
# time = int(input("enthusiasm level: "))
# for w in word:
#     if w in an_letter:
#         print(f"Give me an {w}: {w}")
#     else:
#         print(f"Give me a {w}: {w}")
# print("what does that spell?")
# for i in range(time):
#     print(f"{word} !!!")

#these code is to count a string that the number of the different letters
# a = "abeda"
# b = ""
# count = 0
# for i in a:
#     if i not in b:
#         b = b + i
#         count = count + 1
# print(count)
#
#
# #these code is to test number whether is a prefect square
# num = 4
# for i in range(num+1):
#     if i*i == num:
#         print("this is prefect square and its square root is",i)
#         break
#     elif i*i > num:
#         print("it isn't prefect square")
#         break
#
# found = False
# for i in range(1,11):
#     if i == num:
#         print("found")
#         found = True
# if not found:
#     print("not found")
#
# #these code is to test the number whether is a cube
# cube = int(input("enter an integer: "))
# for i in range(abs(cube)+1):
#     if cube < 0:
#         i = -i
#         if i**3 == cube:
#             print(f"{i} is a cube root")
#     elif i**3 == cube:
#         print(f"{i} is a cube root")


#10进制转化为2进制
num = 1507
ans = ""
while num > 0:
    ans = str(num%2) + ans
    num = num//2        #整除，直接舍掉小数部分
print(ans)


#finger experience
a = "abcdefg"
b = 0
c = ""
while b < len(a):
    c = c + a[b]
    b = b + 2
print(c)

