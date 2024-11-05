import math
"""
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""
#gets user input for the length of pendulum
text = input("Length of pendulum (meters): ")
#converts that input into an integer variable
length = float(text)
#does the pendulum math
time = (math.pi*2)*(math.sqrt(length/9.81))
output = round(time,2)
print(f"Time (seconds): {output}")