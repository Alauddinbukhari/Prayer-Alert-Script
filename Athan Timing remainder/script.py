import datetime  # Module for manipulating dates and times
import requests  # Library for making HTTP requests
import smtplib  # Library for sending emails
import os  # Module for interacting with the operating system
from message import message  # Custom module for generating email message

# List of prayer names
prayer_names = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

# Retrieving email and password from environment variables
my_email = os.environ.get("email")  # Your email address
password = os.environ.get("password")  # Your specific app password

# City for which prayer timings are to be fetched
CITY = "Calgary"

# Get the current date and time
date_time = datetime.datetime.now()

# Print current date and time
print(date_time)

# Format current date in dd-mm-yyyy format
current_date = date_time.strftime("%d-%m-%Y")

# Parameters for the API request
parameters = {
    "date": current_date,  # Current date
    "city": CITY,  # City for prayer timings
    "country": "Canada",  # Country of the city
    "state": "Alberta",  # State of the city
}

# API endpoint for fetching prayer timings
api_url = "http://api.aladhan.com/v1/timingsByCity"

# Send GET request to the API to fetch prayer timings
response = requests.get(api_url, params=parameters)

# Print the JSON response received from the API
print(response.json())

# Extract prayer timings from the API response
timing = response.json()["data"]["timings"]

# Iterate through each prayer
for pray in prayer_names:
    # Get current time in 24-hour format
    current_time = date_time.strftime("%H:%M")

    # Check if the current time matches the time of the prayer
    if timing[pray] == current_time:
        # Establish a connection to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # Start TLS (Transport Layer Security) for secure communication
            connection.starttls()

            # Log in to the SMTP server using email and password
            connection.login(user=my_email, password=password)

            # Generate email message for the prayer alert
            email_message = message(prayer_name=pray, h24_time=current_time)

            # Send the email
            connection.sendmail(
                from_addr=my_email,  # Sender's email address
                to_addrs="syedalauddin.b@gmail.com",  # Recipient's email address
                msg=f"Subject: Prayer Alert, Prayer Name: {pray}\n\n{email_message}"  # Email subject and body
            )

            # Break the loop after sending the email
            break

    # If the current time does not match any prayer time
    if pray == prayer_names[-1]:
        print("The time is not yet for any prayer")
