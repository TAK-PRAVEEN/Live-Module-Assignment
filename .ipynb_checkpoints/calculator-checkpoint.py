def operations(ops):
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    if ops=="*":
        print(f"Multiplication of {num1} & {num2} is {num1*num2}")
    elif ops=="-":
        print(f"Subtraction of {num2} from {num1} is {num1-num2}")
    elif ops=="/":
        print(f"Divison of {num1} by {num2} is {num1/num2}")
    elif ops=="+":
        print(f"Addition of {num1} & {num2} is {num1+num2}")
    else:
        print("Invalid operator")