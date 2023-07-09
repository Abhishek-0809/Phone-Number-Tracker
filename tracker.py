import tkinter as Tk
from tkinter import *

import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime
import pytz

root = Tk()
root.title("Phone Number Tracker")
root.geometry("365x584")
root.resizable(False, False)
root.configure(bg="#d896ff")
# background color code is #d896ff
# individual background color code is #d8b9ff
# san francisco number +14155553890


def track():
    enter_number = entry.get()
    number = phonenumbers.parse(enter_number)

    # country
    locate = geocoder.description_for_number(number, 'en')
    country.config(text=locate)

    # sim operators like jio,airtel
    operator = carrier.name_for_number(number, 'en')
    sim.config(text=operator)

    # timezone
    time = timezone.time_zones_for_number(number)
    zone.config(text=time)

    # longitude and latitude
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(locate)

    lng = location.longitude
    lat = location.latitude
    longitude.config(text=lng)
    latitude.config(text=lat)

    # time showing in phone
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I : %M %p")
    clock.config(text=current_time)

Heading = Label(root, text="TRACK NUMBER", bg="#d8b9ff",
                font=("arial", 25, "bold"), justify="center")
Heading.place(x=43, y=110)

entry = StringVar()
enter_number = Entry(root, textvariable=entry, width=19, bd=0,
                     background="#d8b9ff", font=("arial", 15), justify="center")
enter_number.place(x=75, y=200)

search = Button(text="SEARCH", width=18, bd=1, bg="#d8b9ff",
                font=("arial", 15), justify="center", command=track)
search.place(x=75, y=300)

country = Label(root, text="COUNTRY:", bg="#d8b9ff",
                fg="black", font=("arial", 10, "bold"))
country.place(x=50, y=400)

sim = Label(root, text="SIM:", bg="#d8b9ff",
            fg="black", font=("arial", 10, "bold"))
sim.place(x=200, y=400)

zone = Label(root, text="TIME ZONE:", bg="#d8b9ff",
             fg="black", font=("arial", 10, "bold"))
zone.place(x=50, y=450)

clock = Label(root, text="PHONE TIME:", bg="#d8b9ff",
              fg="black", font=("arial", 10, "bold"))
clock.place(x=200, y=450)

longitude = Label(root, text="LONGITUDE:", bg="#d8b9ff",
                  fg="black", font=("arial", 10, "bold"))
longitude.place(x=50, y=500)

latitude = Label(root, text="LATITUDE:", bg="#d8b9ff",
                 fg="black", font=("arial", 10, "bold"))
latitude.place(x=200, y=500)

root.mainloop()
