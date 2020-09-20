import mysql.connector
import json
import requests
import time
import threading
from datetime import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Sk1m1r1bang",
    database = "temperatures",
)
mycursor = mydb.cursor()


sqlFormula = "INSERT INTO poznan (day,temperature) VALUE (%s, %s)"

def send_temperature():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?id=3088171&appid=0fd80fcf961605d7ddfac000edca9f77&units=metric")
    data = (datetime.today().now().strftime("%A"), response.json()['main']['temp'])
    mycursor.execute(sqlFormula, data)
    mydb.commit()
    print(datetime.today().now().strftime("%A"),response.json()['main']['temp'])
    threading.Timer(10, send_temperature).start()

# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)

send_temperature()
