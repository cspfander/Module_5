"""
Program: input_validation_while_loops.py
Author: Colten Pfander
Last date modified: 9/23/2019



The purpose of this program is to prompt the user for a numeric input between 1 and 100, promp the user until the input
is in the correct range, and once the input is correct store the input in a list
"""


if __name__ == '__main__':
    try:
        numbers = []
        sent_value = int(input("Please enter how many numbers you would like to store: "))
        num = int(input("Please enter a number between 1 and 100: "))
        while len(numbers) + 1 < sent_value:
            while num > 100 or num < 1:
                num = int(input("No good! Number is outside of the appropriate range! Please enter another number between 1 and 100: "))
            numbers.append(num)
            num = int(input("Please enter a number between 1 and 100: "))
            numbers.append(num)
        for number in numbers:
            print(number)
    except ValueError:
        print("Error! Please only input numbers!")

    # tested input 1: 5, 1, 2, 3, 4 ,5
    # output 1: 1
    #         2
    #         3
    #         4
    #         5
    # tested input 2: 2, 0, 0, 101, 1, 2
    # output 2: 1
    #           2
