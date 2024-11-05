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
kermit = input("Would you like to see a picture of Kermit now? (Y/N)")
if kermit == "y" or kermit == "yes" or kermit == "Y":
    print("Excellent, here ya go:")
    print("""
                      .---.     .---.
                     ( -o- )---( -o- )
                     ;-...-`   `-...-;
                    /                 \\
                   /                   \\
                  | /_               _\ |
                  \`'.`'"--.....--"'`.'`/
                   \  '.   `._.`   .'  /
                _.-''.  `-.,,_,,.-`  .''-._
               `--._  `'-.,_____,.-'`  _.--`
                    /                 \\
                   /.-'`\   .'.   /`'-.\\
                  `      '.'   '.
          """)
else:
    print("That's ok, here's one anyway. No worries")
    print("""
                      __
                   (+)  (+)                     
                  /        \  
                  \  -==-  / 
                   \      / 
                  </\/\/\/\> 
                  /        \\
          """)
#gets the current date and time
current_date_and_time = datetime.now()
#opens the volumes text file and appends stuff to it (hence "AT")
with open("volumes.txt","at") as volume_file:
    #prints the current date and time, but w/out the time
    #so just the date basically
    print(f"{current_date_and_time:%Y-%m-%d}, {width:.0f}, {a:.0f}, {diameter:.0f}, {volume}", file=volume_file)