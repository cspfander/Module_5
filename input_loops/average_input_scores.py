"""
Program: average_input_scores.py
Author: Colten Pfander
Last date modified: 9/23/2019



The purpose of this program is to read in one person's names, first and last, their age, and multiple scores
out of 100, storing them in a list
"""


def average(score_list):
    total_score = 0
    num_of_scores = len(score_list)
    for score in score_list:
        total_score += score
    average_test_score = total_score / num_of_scores
    return average_test_score


if __name__ == '__main__':
    average()
