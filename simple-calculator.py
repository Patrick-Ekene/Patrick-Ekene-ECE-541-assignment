# A simple Calculator
operator = input("What operation do you want to perform. add, subtract, multiply, divide? ")

num1 = float(input("input  the first number "))

num2 = float(input("input the second number "))



if operator == "add":
    sum = num1 + num2
    print("Result is " + str(sum))

elif operator == "subtract":
    diff = num1 - num2
    print("Result is " + str(diff))

elif operator == "multiply":
    product = num1 * num2
    print("Result is " + str(product))

elif operator == "divide":
    quotient = num1 / num2
    print("Result is " + str(quotient))