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

tz = pytz.timezone('America/Godthab')

def send_temperature():
    response = requests.get("https://api.thingspeak.com/channels/557741/feeds.json?results=1")
    date_object = datetime.strptime(response.json()['feeds'][0]['created_at'], '%Y-%m-%dT%H:%M:%SZ')
    local_tz = tz.localize(date_object)
    utc_tz = local_tz.astimezone(pytz.UTC)
    data = (local_tz.strftime('%d-%m-%Y %H:%M:%S'), response.json()['feeds'][0]['field4'])
    mycursor.execute(sqlFormula, data)
    mydb.commit()
    print(local_tz.strftime('%d-%m-%Y %H:%M:%S'), response.json()['feeds'][0]['field4'])
    # info = response.json()
    # print(info['feeds'][1]['field4'])
    threading.Timer(20, send_temperature).start()

# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

send_temperature()
