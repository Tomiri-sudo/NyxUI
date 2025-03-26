import random
i = 0
while 1 == 1:
    if i < 10:
        print(random.randint(1, 4))
        i = i + 1
    elif i == 10:
        print("stop")
        break