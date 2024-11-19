from datetime import datetime
import math

date = datetime.now()
day = date.weekday()
disc = False
discount = 0.00
sub = float(input("What is your subtotal? (Be honest): "))
if sub >= 50.00 and day == 3:
    discount = sub * 0.1
    sub = sub-discount
    disc = True
tax = sub*0.06
sub = sub+tax

if disc == True:
    print(f"Discount amount: {discount:.2f}")
print(f"Sales tax amount: {tax:.2f}")
print(f"Total: {sub:.2f}")