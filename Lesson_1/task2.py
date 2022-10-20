operation = input('choose operation:')
number1 = float (input("Enter number 1:"))
number2 = float (input("Enter number 2:"))
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
elif operation == "^":
    print (number1 ** 2)
    print (number2 ** 2)
elif operation == "√":
    print(number1**0.5)
    print(number2**0.5);