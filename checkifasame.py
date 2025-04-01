def check_if_same(num1, num2):
    if (num1 ^ num2) != 0:
        print("They are not the same number.")
    else:
        print("They are the same number.")
        
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the first number: "))
check_if_same(num1, num2)