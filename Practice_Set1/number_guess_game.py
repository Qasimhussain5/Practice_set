import random
guess = random.randint(1,10)
while True:
    n = int(input("Enter Number For guess : "))
    if n == guess:
        print("Well done")
        break
    else:
        print("Try Again")