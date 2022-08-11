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
    # check for length of 2
    if len(tokens) == 2:
        # convert num1 to int
        try:
            float(tokens[1])
        except:
            print("ERROR: That's not a valid number")
        else:
            num1 = float(tokens[1])
            # if operator is square, print num1 ** 2
            if tokens[0] == "square":
                print(square(num1))
            # if operator is cube, print num1 ** 3
            elif tokens[0] == "cube": 
                print(cube(num1))
            else:
                print("ERROR: That's not a valid operator")
    # check for length of 3
    elif len(tokens) == 3:
        # convert num1 to int
        try:
            float(tokens[1])
        except:
            print("ERROR: That's not a valid number")
        else:
            try:
                float(tokens[2])
            except:
                print("ERROR: That's not a valid number")
            else:
                num1 = float(tokens[1])
                num2 = float(tokens[2])
                # if operator is +, print sum of nums
                if tokens[0] == "+":
                    print(add(num1, num2))
                # if operator is -, print num1 - num2
                elif tokens[0] == "-":
                    print(subtract(num1, num2))
                # if operator is *, print num1 * num2
                elif tokens[0] == "*":
                    print(multiply(num1, num2))
                # if operator is /, print num1 / num2
                elif tokens[0] == "/":
                    print(divide(num1, num2))
                # if operator is pow, print num1 ** num2
                elif tokens[0] == "pow":
                    print(power(num1, num2))
                # if operator is mod, print num1 % num2
                elif tokens[0] == "mod":
                    print(mod(num1, num2))
                # if operator not valid, print error
                else:
                    print("ERROR: That's not a valid operator")

    else:
        print("ERROR: That's an invalid input")
            
            
    