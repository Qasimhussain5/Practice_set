num = input("Enter a number: ")
sum_digits = sum(int(digit) for digit in num)
print(f"The sum of digits of {num} is {sum_digits}")