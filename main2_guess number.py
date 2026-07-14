secret = 5
answer = int(input("please type a number: "))
if answer == secret:
    print("you guessed right")
elif answer >= secret:
    print("you guessed big")
else:
    print("you guessed small")

a = (secret == answer)
print(a)
#绝对值
print(abs(-3))