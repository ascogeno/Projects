import math
#gets user input for the number of items and boxes
inp_items = input("Enter the number of items: ")
inp_per_b = input("Enter the number of items PER BOX: ")
#takes the inputs and puts them in float variables
items_float = float(inp_items)
per_b_float = float(inp_per_b)
#converts those floats back to ints, just in case the user enters a decimal and breaks the program
items = int(round(items_float,0))
per_b = int(round(per_b_float,0))
#does the math for the boxes
num_boxes = math.ceil(items/per_b)
#output
print(f"For {items} items, packing {per_b} in each box, you will need {num_boxes} boxes.")