"""
Program: average_input_scores.py
Author: Colten Pfander
Last date modified: 9/23/2019



The purpose of this program is to read in one person's names, first and last, their age, and multiple scores
out of 100, storing them in a list
"""


def average(score_list):  # function to average a list of stored inputs
    total_score = 0
    num_of_scores = len(score_list)
    for score in score_list:
        total_score += score
    average_test_score = total_score / num_of_scores
    return average_test_score


if __name__ == '__main__':
    try:
        scores = []
        input_score_message = "Please enter a test score, or enter -1 to end the program: "  # sentinel value / flag + getting score
        last_name = input("Please enter your last name: ")
        first_name = input("Please enter your first name: ")
        test_score = float(input(input_score_message))

        while test_score >= 0:
            scores.append(test_score)
            test_score = float(input(input_score_message))
        avg_scores = average(scores)
        print(last_name + ", " + first_name + " average grade: %.2f" % avg_scores)
    except ValueError:
        print("Error! Please use only numbers for test scores!")  # try / except block to catch letters being put into scores

    # tested inputs 1: Pfander, Colten, 100, 50, -1
    # outputs 1: Pfander, Colten average grade: 75.00
    # tested inputs 2: Sandler, Adam, 25, 25, 100, 100, 90, -1
    # outputs 2: Sandler, Adam average grade: 68.00
