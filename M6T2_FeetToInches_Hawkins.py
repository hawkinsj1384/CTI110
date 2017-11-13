# This program converts feet to inches
# 11/12/2017
# CTI-110 M6T2_FeetToInches 
# Jalessa Hawkins

# main function
def main():
    # Get a number of feet from the user
    feet = int(input('Enter a number of  feet: '))

    # Convert user input to inches.
    print(feet,'feet equals', feet_to_inches(feet), 'inches.')

# The feet_to_inches function converts feet to inches.
def feet_to_inches(feet):
    return feet * 12
main()
