"""
Program: validation_with_try.py.
Author: Mohammad Noori
Date: 09/21/2019
This program let the user enter three scores and print the average with try and exception validation.
"""


def average_score():  # declaring function
    first_grade = float(input("please, enter your next grade"))  # first user input
    if first_grade < 0:  # accept negative
        raise ValueError("This wrong")  # try and exception validation.
    second_grade = float(input("please, enter your next grade"))  # second input
    if second_grade < 0:  # accept negative
        raise ValueError("This wrong")  # try and exception validation.
    third_grade = float(input("please, enter your next grade"))  # third input
    if third_grade < 0:  # accept negative
        raise ValueError("This wrong")  # try and exception validation.
    average_ = first_grade + second_grade + third_grade  # calculation addition
    grade_average = float(3)  # variable
    total_grade = average_ / grade_average  # calculation average
    print("grade:", total_grade)  # output
    return total_grade  # return


if __name__ == '__main__':
    average_score()  # call the function.
