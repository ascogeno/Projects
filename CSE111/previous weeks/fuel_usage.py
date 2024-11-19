def main():
    # Get an odometer value in U.S. miles from the user.
    start = float(input("What did the odometer say when you started driving? (Miles): "))
    # Get another odometer value in U.S. miles from the user.
    end = float(input("What did the odometer say when you FINISHED driving? (Miles): "))
    # Get a fuel amount in U.S. gallons from the user.
    gas = float(input("How much gas did you use? (Gallons): "))
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start,end,gas)
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    # Display the results for the user to see.
    print(f"Miles per gallon: {mpg:.1f}")
    print(f"Liters per gallon: {lp100k:.2f}")
    pass

def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    
    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    return_value = (end_miles-start_miles)/amount_gallons
    return return_value


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    return_value = 235.215/mpg
    return return_value
# Call the main function so that
# this program will start executing.
main()