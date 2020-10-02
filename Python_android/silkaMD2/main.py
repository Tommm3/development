import kivymd
from kivymd.app import MDApp

from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton, MDRectangleFlatIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem, OneLineAvatarIconListItem
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.metrics import dp
from helpers import username_helper, button_helper, list_helper, text_field_helper
from datetime import datetime
import pandas as pd
from openpyxl import load_workbook
#
# KV = '''
# <Content>
#     text: "Enter"
#
# '''


def get_init_exercise_tuple():
    wd = datetime.now().strftime("%A")
    reader = pd.read_excel(r'silka.xlsx')
    if wd=='Monday':
        df = pd.read_excel('silka.xlsx', skiprows=0, usecols=[0,1,len(reader.columns)-1], nrows=8)
    elif wd=='Tuesday':
        df = pd.read_excel('silka.xlsx', skiprows=8, usecols=[0,1,len(reader.columns)-2], nrows=9)
    elif wd=='Thursday':
        df = pd.read_excel('silka.xlsx', skiprows=17, usecols=[0,1,len(reader.columns)-2], nrows=8)
    elif wd=='Friday':
        df = pd.read_excel('silka.xlsx', skiprows=25, usecols=[0,1,len(reader.columns)-2,len(reader.columns)-1], nrows=5)
    else:
        df = 'Brak świczeń na dziś'
    print(df.to_records(index=False))
    return df.to_records(index=False)

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

class Content(Widget):
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        table = MDDataTable(pos_hint={"center_x":0.5,"center_y":0.5},
                            size_hint=(0.9,0.6),
                            check="True",
                            rows_num=9,
                            column_data=[
                                ("Exercise",dp(80)),
                                ("Repeats",dp(20)),
                                ("Last weight",dp(20)),
                                ("New weight",dp(20))
                            ],
                            row_data=get_init_exercise_tuple()
                            )
        table.bind(on_row_press=self.row_press)
        head = MDLabel(text = datetime.now().strftime('%A'),
                        halign = 'center',
                        font_style = 'H3',
                        pos_hint={"center_x":0.5,"center_y":0.9},
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color
                        )
        screen.add_widget(head)
        screen.add_widget(table)
        return screen

    def row_press(self, instance_table, current_row):
        self.weight = Builder.load_string(text_field_helper)
        self.dialog = MDDialog(text=current_row.text + "\n\n",
                        size_hint=(0.8,1),
                        buttons=[MDRectangleFlatButton(text="OK",
                                                    on_release=self.close_dialog,
                                                    text_color=self.theme_cls.primary_color,
                                                    pos_hint={"center_x":1,"center_y":0.5})]
                                )

        self.dialog.add_widget(self.weight)
        self.dialog.open()

    def close_dialog(self, obj):
        print(self.weight.text)
        self.dialog.dismiss()


if __name__ == "__main__":
    MyApp().run()
