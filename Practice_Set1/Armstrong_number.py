print("Armstrong numbers between 1 and 1000:")

for num in range(1, 1001):
    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d) ** power

    if total == num:
        print(num)
