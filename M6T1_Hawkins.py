#CTI-110
#M6T1
#Jalessa Hawkins
#November 11, 2017

def main():
        # Get the distance in kilometers
        kilometers = float(input('Enter a distance in kilometers: '))
        # Display the distance converted to miles.
        show_miles(kilometers)
        
def show_miles(km):
        # Calculate miles
        miles = km * 0.6214
        # Display the miles
        print(km, 'kilometers equals', miles, 'miles.')

main()

        
