import mysql.connector
import json
import requests
import time
import threading
import pytz
from datetime import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Sk1m1r1bang",
    database = "photoresistor",
)
mycursor = mydb.cursor()

sqlFormula = "INSERT INTO light (time,value) VALUE (%s, %s)"

tz = pytz.timezone('UTC')

def send_temperature():
    # Get request for a latest json from Thingspeak
    response = requests.get("https://api.thingspeak.com/channels/557741/feeds.json?results=1")
    # Find a timestamp in written json and convert it to datetime object
    date_object = datetime.strptime(response.json()['feeds'][0]['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    # Localize a timestamp in UTC timezone
    local_tz = tz.localize(date_object)
    # Convert a timestamp timezone to Europe/Warsaw
    wawa_tz = local_tz.astimezone(pytz.timezone('Europe/Warsaw'))
    # Create a tuple with timestamp and a value from sensor
    data = (wawa_tz.strftime('%d-%m-%Y %H:%M:%S'), response.json()['feeds'][0]['field4'])
    # Populate a database
    mycursor.execute(sqlFormula, data)
    # Confirm action
    mydb.commit()
    # Print out a written strings
    print(wawa_tz.strftime('%d-%m-%Y %H:%M:%S'), response.json()['feeds'][0]['field4'])
    # Wait 20 s
    threading.Timer(20, send_temperature).start()

send_temperature()
