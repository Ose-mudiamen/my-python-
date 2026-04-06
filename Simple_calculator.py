print("1 Add numbers")
print("2 Subtract numbers")
print("3 Divide numbers")
print()
num = int(input("Enter from 1,2 or 3: "))
if num == 1:
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))
    total = num1+num2
    print(num1,"+",num2,"is =",total)
elif num == 2:
    num1 = int(input("Enter a large number: "))
    num2 = int(input("Enter a small number: "))
    total = num1-num2
    print(num1,"-",num2,"is = to",total)
elif num == 3:
    num1 = int(input("Enter a large number: "))
    num2 = int(input("Enter a small number: "))
    total = num1//num2
    remain = num1%num2
    print(num1,"divided by",num2,"is",total,"with",remain,"remainder")
else:
    print("This Program Has Ended")