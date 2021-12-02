def user_num_input():
    global user_input_symbol
    global user_input_space

    user_input_symbol = int(input("Please insert the number of #: "))
    user_input_space = int(input("Please insert the number of space: "))
    
    if user_input_space >= user_input_symbol:
        print("the spaces can't be greater than or equal to symbols!")


def print_my_symbol(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    # scale number
    scl_num = 0
    # hash
    hh = "#"
    # space
    se = " "
    range_1 = int((num1-num2)/2)
    range_2 = int((num1+num2)/2)
    # build columns
    while scl_num < num1:
        # rows with if statements
        if scl_num < range_1:
            for i in range(num1):
                print(hh, end = "")
        elif scl_num in range(range_1, range_2):
            for i in range(range_1):
                print(hh, end = "")
            for i in range(num2):
                print(se, end = "")
            for i in range(range_1):
                print(hh, end = "")
        else:
            for i in range(num1):
                print(hh, end = "")
        # go to the next line
        print("", end = "\n")
        # step of while loop
        scl_num += 1


# apply the funcs
user_num_input()
print_my_symbol(user_input_symbol, user_input_space)

