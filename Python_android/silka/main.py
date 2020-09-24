import kivy
from kivy.app import App
# from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from datetime import datetime
import pandas as pd

def read_day(wd):
    if wd=='Monday':
        df = pd.read_excel('silka.xlsx', skiprows=1, usecols=[0], nrows=7)
    if wd=='Tuesday':
        df = pd.read_excel('silka.xlsx', skiprows=9, usecols=[0], nrows=8)
    if wd=='Thursday':
        df = pd.read_excel('silka.xlsx', skiprows=18, usecols=[0], nrows=7)
    if wd=='Friday':
        df = pd.read_excel('silka.xlsx', skiprows=26, usecols=[0], nrows=4)
    return df.to_string(index=False).replace('\n','\n\n')

def read_day_weight(wd):
    reader = pd.read_excel(r'silka.xlsx')
    if wd=='Monday':
        df = pd.read_excel('silka.xlsx', skiprows=1, usecols=[len(reader.columns)-1], nrows=7)
    if wd=='Tuesday':
        df = pd.read_excel('silka.xlsx', skiprows=9, usecols=[len(reader.columns)-1], nrows=8)
    if wd=='Thursday':
        df = pd.read_excel('silka.xlsx', skiprows=18, usecols=[len(reader.columns)-1], nrows=7)
    if wd=='Friday':
        df = pd.read_excel('silka.xlsx', skiprows=26, usecols=[len(reader.columns)-1], nrows=4)
    print(len(reader.columns)-1)
    return df.to_string(index=False).replace('\n','\n\n')

class MySilka(Widget):
    weekday = ObjectProperty(None)
    exercises = ObjectProperty(None)
    last_weight = ObjectProperty(None)
    def get_weekday(self):
        self.weekday.text = datetime.now().strftime("%A")
    def get_exercises(self):
        self.exercises.text = read_day(self.weekday.text)
        self.last_weight = read_day_weight(self.weekday.text)
        print(self.exercises.text, 'utf-8')
        print(self.last_weight, 'utf-8')

class MyApp(App):
    def build(self):
        apka = MySilka()
        apka.get_weekday()
        apka.get_exercises()
        return apka

if __name__ == "__main__":
    MyApp().run()
