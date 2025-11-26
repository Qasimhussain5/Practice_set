# a = input("Enter Number : ")
# rev_a = a[::-1]
# if a == rev_a:
#     print("palindrome")
# else:
#     print("Not palindrome")

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")
