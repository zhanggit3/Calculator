#import math

#define addition

#define substraction

#define multiplication

#define division



#rest memory: write CE|C, delete everything in the list

import re
import math
import operator

while True:
    user_input = input("Enter a number or enter CE|C to clear: ")
    if user_input == "CE|C":
        break
    elif not user_input.isdigit():
        print("That's not a number")
        continue
    else:
        number1 = int(user_input)

    op = input("Enter an operator (+, -, *, /, √) or enter CE|C to clear: ")
    if op == "CE|C":
        break
    elif op == "√":
        output = math.sqrt(number1)
        print(output)
        continue
    else:
        op

    user_input1 = input("Enter another numbe or enter CE|C to clear: ")
    if user_input1 == "CE|C":
        break
    elif not user_input1.isdigit():
        print("That's not a number")
        continue
    else:
        number2 = int(user_input1)


    if op == "+":
        ans = number1 + number2
    elif op == "-":
        ans = number1 - number2
    elif op == "*":
        ans = number1 * number2
    elif op == "/":
        ans = number1 / number2
    else:
        print("Not an operator")

    print(number1, op, number2, "=", ans)











