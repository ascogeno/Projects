def get_initial(name, capitalize = True):
    """This function returns the first letter of the name"""
    if capitalize:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial
def main():
    my_name = input('What is your first name? ')
    my_initial = get_initial(my_name)
    print(f'Your first initial is {my_initial}')

main()