#二分法查找平方根
# x = float(input('Enter a number: '))
# epsilon = 0.01
# num_guesses = 0
# if x >= 1:
#     low = 0
#     high = x
# else:
#     low = x
#     high = 1
# guess = (low + high)/2
# while abs(guess**2 - x) >= epsilon:
#     if guess**2 > x:
#         high = guess
#     else:
#         low = guess
#     guess = (low + high)/2
#     num_guesses += 1
#
# print(num_guesses+1)
# print(guess)


#二分法查找立方根
cube = 27
epsilon = 0.01
if abs(cube) >= 1:
    low = 0
    high = cube
else:
    low = cube
    high = 1
guess = (low + high)/2
while abs(guess**3 - cube) >= epsilon:
    if guess ** 3 > cube:
        high = guess
    else:
        low = guess
    guess = (low + high) / 2

print(guess)