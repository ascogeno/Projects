import math
from datetime import datetime

#Get tire info from the user
width = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
#does the math, and rounds to 2 decimal points
volume = round((math.pi*(width*width)*a*(width * a + (2540*diameter)))/10000000000,2)
#output for the user
print(f"The approximate volume is {volume} liters")
#gets the current date and time
current_date_and_time = datetime.now()
#opens the volumes text file and appends stuff to it (hence "AT")
with open("volumes.txt","at") as volume_file:
    #prints the current date and time, but w/out the time
    #so just the date basically
    #makes you wonder a bit, doesn't it
    print(f"{current_date_and_time:%Y-%m-%d}, {width}, {a}, {diameter}, {volume}", file=volume_file)