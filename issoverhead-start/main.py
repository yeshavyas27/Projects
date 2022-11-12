import requests
import smtplib
from datetime import datetime

MY_LAT = -11.6892
MY_LONG = -43.3822
MY_EMAIL = "yeshacodes@gmail.com"
MY_PASSWORD = "yujjfkqvdfwdtnrr"


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if time_now >= sunset:
        return True


def within_range():
    if iss_latitude <= MY_LAT + 5 and iss_latitude > MY_LAT or iss_latitude >= MY_LAT-5 and iss_latitude < MY_LAT:
        if iss_longitude<=MY_LONG+5 and iss_longitude>MY_LONG or iss_longitude>=MY_LONG-5 and iss_longitude<MY_LONG:
            if is_night():
                send_email()



def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="yeshacodes@yahoo.com",
                            msg="Subject: ISS nearby\n\n Look Up!!")









response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

time_now = datetime.now().hour

within_range()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



