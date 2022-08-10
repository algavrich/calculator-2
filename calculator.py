"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# loop forever
while True:
    # ask user for math problem
    user_choice = input('Type your math problem using operator num1 num2 format > ')
    # tokenize input
    tokens = user_choice.split(' ')
    # quit if first token is q
    if tokens[0] == "q":
        break
    # if first token isn't q, check operator validity
    elif tokens[0] in ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']:
        # if operator is +, print sum of nums
        if tokens[0] == "+":
            print(add(float(tokens[1]), float(tokens[2])))
        # if operator is -, print num1 - num2
        elif tokens[0] == "-":
            print(subtract(float(tokens[1]), float(tokens[2])))
        # if operator is *, print num1 * num2
        elif tokens[0] == "*":
            print(multiply(float(tokens[1]), float(tokens[2])))
        # if operator is /, print num1 / num2
        elif tokens[0] == "/":
            print(divide(float(tokens[1]), float(tokens[2])))
        # if operator is square, print num1 ** 2
        elif tokens[0] == "square":
            print(square(float(tokens[1])))
        # if operator is cube, print num1 ** 3
        elif tokens[0] == "cube":
            print(cube(float(tokens[1])))
        # if operator is pow, print num1 ** num2
        elif tokens[0] == "pow":
            print(power(float(tokens[1]), float(tokens[2])))
        # if operator is mod, print num1 % num2
        elif tokens[0] == "mod":
            print(mod(float(tokens[1]), float(tokens[2])))

    # if operator not valid, print error
    else:
        print("ERROR: That's not a valid operator")
        
            
    