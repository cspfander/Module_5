"""
Program: basic_for_loops.py
Author: Colten Pfander
Last date modified: 9/23/2019



The purpose of this program is to declare a list of floating point numbers, write a for loop to print each, and write a second for
loop to print the odd number descending from 99 to 33
"""


if __name__ == '__main__':
    numbers = [3.14, 24.0, 11.22, 1.01]

    # for loop to print all numbers in list numbers
    for num in numbers:
        print(num)

    # prints all odd numbers from 99 to 33
    for odd_num in range(99, 32, -2):
        print(odd_num)
