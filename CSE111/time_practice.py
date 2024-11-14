from datetime import datetime

def print_time_and_message(message):
    print(message)
    print(datetime.now())

print_time_and_message("Hello world! Here is the current time.")