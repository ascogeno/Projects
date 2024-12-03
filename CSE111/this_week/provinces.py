def main():

    provinces = []
    with open("provinces.txt", "rt") as province_file:
        for line in province_file:
            clean_line = line.strip()
            provinces.append(clean_line)

    
    provinces.pop(0)
    provinces.pop()

    for index in range(len(provinces)):
        if provinces[index] == 'AB':
            provinces[index] = 'Alberta'
    print(provinces)
#commented out, but it should do the same thing as the above code
    """while 'AB' in provinces:
        index = provinces.index('AB')
        provinces[index] = 'Alberta'"""

    albertas = provinces.count("Alberta")
    print(f'There are {albertas} Albertas in the list.')


if __name__== '__main__':
    main()