import random
a=random.randint(1,100)
guess=1
x=int(input())
while  x!=a:
    if x>a:
        print("大了")
    else:
        print("小了")
    x=int(input())
    guess+=1
print(guess)


