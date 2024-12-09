import csv

def read_dictionary(filename, key_column_index):
    """Reads a CSV file and creates a dictionary with I-Number as key and student name as value."""
    students_dict = {}
    
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        
        for row in csv_reader:
            i_number = row[key_column_index]
            name = row[1]  # Assuming name is in the second column
            students_dict[i_number] = name
    
    return students_dict

def main():
    filename = 'students.csv'
    key_column_index = 0  # Assuming the I-Number is in the first column
    
    # Step 1: Read the students CSV into a dictionary
    students_dict = read_dictionary(filename, key_column_index)
    
    # Step 2: Get I-Number from the user
    i_number = input("Enter I-Number: ")
    
    # Step 3: Check if the I-Number exists and display the name or print an error message
    if i_number in students_dict:
        print(f"Student name: {students_dict[i_number]}")
    else:
        print("No such student")

# Run the main function
if __name__ == '__main__':
    main()