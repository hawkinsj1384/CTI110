# This program calculates average and grade letter
# November 17, 2017
# CTI-110 M6HW1 - Test Average and Grade
# Jalessa Hawkins

def main():
# Here the user will input five test grades.
    scores = input("Enter five test scores separated by commas: ")
    return [int(num) for num in scores.split(",")]

# The each grade inputted by the user will be given a grade letter 
def determine_grade(num):
    if 90 <= num <= 100:
        letter_grade = "A"
    elif 80 <= num <= 89:
        letter_grade = "B"
    elif 70 <= num <= 79:
        letter_grade = "C"
    elif 60 <= num <= 69:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade

# This function determines the average of the grades.
def calc_average(grades):
    average = sum(grades) / len(grades)
    grade = determine_grade(average)
    print("The average is: {:.1f} which is {}".format(average, grade))

# This formats the output of the letter grades.
def show_letters(num, letter_grade):
    print("{:.1f} is {}\n".format(num, letter_grade))

# This allows the program to run and formats it to list
lst = main()
for n in lst:
    show_letters(n, determine_grade(n))
calc_average(lst)

