"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
# gets user to input their age, and converts it to an int
age = int(input("Please enter your age: "))
#finds maximum heart-rate
maximum_rate = 220-age
#arithmatic to find the percents, and rounds them so the output is a bit cleaner
low_percent=round(maximum_rate*0.65)
high_percent=round(maximum_rate*0.85)
#output for the user
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart-rate between {low_percent} and {high_percent}")
print("beats per minute.")
