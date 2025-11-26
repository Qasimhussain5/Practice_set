print("Simple Calculator")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

choice = int(input("Enter your choice (1-4): "))
a = int(input("Enter Your Number : "))
b = int(input("Enter Your Number : "))
if choice == 1:
    print("Result: " , a+b)
elif choice ==2:
    print("Result: " , a-b)
elif choice == 3:
    print("Result: " , a*b)
elif choice == 4:
    if a == 0:
        print("Invalid")
    else:
        print("Result: ", a/b)