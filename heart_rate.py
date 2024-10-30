"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# gets user to input their age
text = input("Please enter your age: ")
#converts their input into an integer in the variable "age"
age = int(text)
#finds maximum heart-rate
maximum_rate = 220-age
#arithmatic to find the upper and lower bounds to keep the heart-rate at
low_percent_float = maximum_rate*0.65
high_percent_float = maximum_rate*0.85
#converts the float variables made above into ints, so we don't display decimals later
low_percent=int(low_percent_float)
high_percent=int(high_percent_float)
#output for the user
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart-rate between {low_percent} and {high_percent}")
print("beats per minute.")
