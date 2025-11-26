ch = input("Enter number : ")

ch = ch.lower()
if ch.isalpha():
    if ch in ('a','e','i','o','u'):
        print("Vowel")
    else:
        print("constent")
else:
    print("Enetr correct alphabet")