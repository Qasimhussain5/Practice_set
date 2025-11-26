num = int(input("Enter a decimal number: "))
n = num
binary = ""

if n == 0:
    binary = "0"
else:
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2

print(f"Binary of {num} is {binary}")
