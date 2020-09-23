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

class MySilka(Widget):
    weekday = ObjectProperty(None)
    exercises = ObjectProperty(None)
    def get_weekday(self):
        self.weekday.text = datetime.now().strftime("%A")
    def get_exercises(self):
        self.exercises.text = str(pd.read_excel('silka.xlsx', index_col=None, usecols=[0], skiprows=10, nrows=7)).replace('\n','\n\n')

class MyApp(App):
    def build(self):
        apka = MySilka()
        apka.get_weekday()
        apka.get_exercises()
        return apka

if __name__ == "__main__":
    MyApp().run()
