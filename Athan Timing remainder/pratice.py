import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the datetime object to represent time in 24-hour format (hours and minutes)
formatted_time = current_datetime.strftime("%H:%M")

print("Current Time (24-hour format - hours and minutes):", formatted_time)
