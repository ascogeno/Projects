import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    product_dict = {}
    
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        
        for row in csv_reader: #for each line in the csv file
            p_number = row[key_column_index] #represents the key for use in the dict, expects a 0 to be passed in
            product_dict[p_number] = row #assigns the array to the current product number

    return product_dict


def main():
    """Executes other functions"""
    try:
        products_dict = read_dictionary("products.csv",0) #creates a dictionary based on the contents of products.csv
        quest = input("Where would you like to shop today? Enter the name of the store you'd like to shop with today: ")
        print(f"{quest}\n") #for reciept formatting, I guess?
        num_items = 0
        subtotal = 0
        current_date_and_time = datetime.now()
        with open("request.csv", 'r') as file: #opens request.csv
            csv_reader = csv.reader(file)
            next(csv_reader)# Skips header row
            for row in csv_reader:
                p_number = row[0]
                quantity = row[1] #defines variables for use later, names are 
                quant = int(quantity)
                current_product=products_dict[p_number] #grabs the array assigned to the product number
                price = float(current_product[2])
                num_items += quant
                subtotal += (price*quant)
                print(f"{current_product[1]}: {quantity} @ {current_product[2]}")

        #prints literally everything
        print(f"Number of items: {num_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {subtotal*0.06:.2f}")
        print(f"Total: {(subtotal + (subtotal*0.06)):.2f}\n")
        print(f"Thank you for taking a chance at {quest}")
        print(f"{current_date_and_time:%a %b %I:%M:%S %Y}")

    except FileNotFoundError as nofile:
        print(f"Error: missing file\n{nofile}")
    except KeyError as nokey:
        print(f"Error: unknown product ID in the request.csv file \n{nokey}")
    


if __name__ == "__main__":
    main()


    