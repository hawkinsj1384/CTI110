#CTI-110
#M3HW1-Age Classifier
#Jalessa Hawkins
#September 22, 2017

def main():
# Define age groups

    Infant = 1
    Child = 12
    Teenager = 19
    Adult = 20

    age = int(input('Enter age: '))

    if age <= Infant:
        print('This person is an infant.')
    else:
        if age <= Child:
            print('This person is a child.')
        else:
            if age <= Teenager:
                print('This person is a teenager.')
            else:
                if age >= Adult:
                    print('This person is an adult.')

main()


