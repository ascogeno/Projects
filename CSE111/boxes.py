import math
#gets user input for the number of items and boxes
items = int(input("Enter the number of items: "))
per_b = int(input("Enter the number of items PER BOX: "))
#does the math for the boxes
num_boxes = math.ceil(items/per_b)
#output
print(f"For {items} items, packing {per_b} in each box, you will need {num_boxes} boxes.")