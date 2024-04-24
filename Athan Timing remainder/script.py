import datetime
import requests
import smtplib
import os
from message import message


prayer_names =["Fajr","Dhuhr","Asr","Maghrib","Isha"]
my_email = os.environ.get("email")#your email
password = os.environ.get("password")#your specific app password

CITY = "Calgary"

date_time = datetime.datetime.now()

current_date = date_time.strftime("%d-%m-%Y")

parameters = {
    "date":current_date,
    "city":"Calgary",
    "country":"Canada",
    "state":"Alberta",
}
api_url = f"http://api.aladhan.com/v1/timingsByCity/{date_time}"

response = requests.get(api_url,params=parameters)

timing= response.json()["data"]["timings"]


for pray in prayer_names:
    current_time= date_time.strftime("%H:%M")
    if timing[pray] == current_time:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            email_message= message(prayer_name=pray,h24_time=current_time)
            connection.sendmail(from_addr=my_email, to_addrs="syedalauddin.b@gmail.com",
                                msg=f"Subject: Prayer Alert, Prayer Name: {pray}\n\n{email_message}")
            break

    if pray == prayer_names[-1]:
        print("The time is not yet for any prayer")
        
