import kivymd
from kivymd.app import MDApp
# from kivy.lang import Builder
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# from kivy.uix.textinput import TextInput
# from datetime import datetime
# import pandas as pd
# from openpyxl import load_workbook

# def read_day(wd):
#     if wd=='Monday':
#         df = pd.read_excel('silka.xlsx', skiprows=1, usecols=[0], nrows=7)
#     elif wd=='Tuesday':
#         df = pd.read_excel('silka.xlsx', skiprows=9, usecols=[0], nrows=8)
#     elif wd=='Thursday':
#         df = pd.read_excel('silka.xlsx', skiprows=18, usecols=[0], nrows=7)
#     elif wd=='Friday':
#         df = pd.read_excel('silka.xlsx', skiprows=26, usecols=[0], nrows=4)
#     else:
#         return 'Brak świczeń na dziś'
#         exit()
#     return df.to_string(index=False).replace('\n','\n\n')
#
# def read_day_weight(wd):
#     reader = pd.read_excel(r'silka.xlsx')
#     if wd=='Monday':
#         df = pd.read_excel('silka.xlsx', skiprows=1, usecols=[len(reader.columns)-1], nrows=7)
#     elif wd=='Tuesday':
#         df = pd.read_excel('silka.xlsx', skiprows=9, usecols=[len(reader.columns)-2], nrows=8)
#     elif wd=='Thursday':
#         df = pd.read_excel('silka.xlsx', skiprows=18, usecols=[len(reader.columns)-2], nrows=7)
#     elif wd=='Friday':
#         df = pd.read_excel('silka.xlsx', skiprows=26, usecols=[len(reader.columns)-2], nrows=4)
#     else:
#         return ''
#         exit()
#     return df.to_string(index=False).replace('\n','\n\n')
#
# class MySilka(BoxLayout):
#     weekday = ObjectProperty(None)
#     exercises = ObjectProperty(None)
#     last_weight = ObjectProperty(None)
#
#     def __init__(self, **kwargs):
#         # weekday_in = datetime.now().strftime('%A')
#         weekday_in = datetime.now().strftime('%A')
#         super(MySilka,self).__init__(**kwargs)
#         self.size_hint_x = 1.7
#         self.padding = 100
#         self.new_weights = GridLayout(cols=1, spacing=20)
#         global new_weight1
#         new_weight1=TextInput(multiline=False)
#         global new_weight2
#         new_weight2=TextInput(multiline=False)
#         global new_weight3
#         new_weight3=TextInput(multiline=False)
#         global new_weight4
#         new_weight4=TextInput(multiline=False)
#         global new_weight5
#         new_weight5=TextInput(multiline=False)
#         self.new_weights.add_widget(new_weight1)
#         self.new_weights.add_widget(new_weight2)
#         self.new_weights.add_widget(new_weight3)
#         self.new_weights.add_widget(new_weight4)
#         self.new_weights.add_widget(new_weight5)
#         if weekday_in == "Monday" or weekday_in == "Thursday" or weekday_in == "Tuesday":
#             global new_weight6
#             new_weight6=TextInput(multiline=False)
#             global new_weight7
#             new_weight7=TextInput(multiline=False)
#             global new_weight8
#             new_weight8=TextInput(multiline=False)
#             self.new_weights.add_widget(new_weight6)
#             self.new_weights.add_widget(new_weight7)
#             self.new_weights.add_widget(new_weight8)
#             print(weekday_in)
#             if weekday_in == "Tuesday":
#                 global new_weight9
#                 new_weight9=TextInput(multiline=False)
#                 self.new_weights.add_widget(new_weight9)
#         self.add_widget(self.new_weights)
#
#     def get_weekday(self):
#         # self.weekday.text = datetime.now().strftime('%A')
#         self.weekday.text = datetime.now().strftime('%A')
#     def get_exercises(self):
#         self.exercises.text = read_day(self.weekday.text)
#         self.last_weight = read_day_weight(self.weekday.text)
#         print(self.exercises.text, 'utf-8')
#         print(self.last_weight, 'utf-8')
#     def btn(self):
#         masa = [new_weight1.text,new_weight2.text,new_weight3.text,new_weight4.text,new_weight5.text]
#         if self.weekday.text == 'Monday' or self.weekday.text == 'Thursday':
#             masa.extend([new_weight6.text,new_weight7.text,new_weight8.text])
#         elif self.weekday.text == 'Tuesday':
#             masa.extend([new_weight6.text,new_weight7.text,new_weight8.text,new_weight9.text])
#         elif self.weekday.text == 'Friday':
#             pass
#         else:
#             exit()
#         writer = pd.ExcelWriter('silka.xlsx', engine='openpyxl')
#         writer.book = load_workbook('silka.xlsx')
#         writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
#         reader = pd.read_excel(r'silka.xlsx')
#         masa_dict = {('masa'+str(len(reader.columns)-2)):masa}
#         df = pd.DataFrame(masa_dict)
#         if self.weekday.text == 'Monday':
#             df.to_excel(writer,index=False,startcol=len(reader.columns))
#         elif self.weekday.text == 'Tuesday':
#             df.to_excel(writer,index=False,startcol=len(reader.columns)-1,startrow=9,header=False)
#         elif self.weekday.text == 'Thursday':
#             df.to_excel(writer,index=False,startcol=len(reader.columns)-1,startrow=18,header=False)
#         elif self.weekday.text == 'Friday':
#             df.to_excel(writer,index=False,startcol=len(reader.columns)-1,startrow=26,header=False)
#         writer.close()
#         print(masa)


class MyApp(MDApp):
    def build(self):
        # apka = MySilka()
        # apka.get_weekday()
        # apka.get_exercises()
        return
if __name__ == "__main__":
    MyApp().run()
