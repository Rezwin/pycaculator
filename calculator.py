num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter the operation you would like to perform (+,-,x) : ")

if operation == "+":
    print(f"The sum of the numbers are: \n {num1} + {num2} = {num1+num2}")
elif operation == "-":
    print(f"Subtracting the numbers are: \n {num1} - {num2} = {num1-num2}")
elif operation == "x":
    print(f"Multiplying the numbers are: \n {num1} x {num2} = {num1*num2}")

