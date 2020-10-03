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


def get_init_exercise_tuple():
    wd = datetime.now().strftime("%A")
    reader = pd.read_excel(r'silka.xlsx')
    if wd=='Monday':
        df = pd.read_excel('silka.xlsx', skiprows=0, usecols=[0,1,len(reader.columns)-1,len(reader.columns)], nrows=8)
        df.index+=1
    elif wd=='Tuesday':
        df = pd.read_excel('silka.xlsx', skiprows=8, usecols=[0,1,len(reader.columns)-2,len(reader.columns)-1], nrows=9)
        df.index+=1
    elif wd=='Thursday':
        df = pd.read_excel('silka.xlsx', skiprows=17, usecols=[0,1,len(reader.columns)-2,len(reader.columns)-1], nrows=8)
        df.index+=1
    elif wd=='Friday':
        df = pd.read_excel('silka.xlsx', skiprows=25, usecols=[0,1,len(reader.columns)-2,len(reader.columns)-1], nrows=5)
        df.index+=1
    else:
        df = 'Brak świczeń na dziś'
    print(df.to_records(index=True))
    return df.to_records(index=True)


class Content(Widget):
    pass


class MyApp(MDApp):
    def build(self):
        self.current_table = get_init_exercise_tuple()
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        self.screen = Screen()
        self.table = MDDataTable(pos_hint={"center_x":0.5,"center_y":0.5},
                            size_hint=(0.9,0.6),
                            rows_num=9,
                            column_data=[
                                ("No.",dp(8)),
                                ("Exercise",dp(80)),
                                ("Repeats",dp(20)),
                                ("Last weight",dp(20)),
                                ("New weight",dp(20))
                            ],
                            row_data=self.current_table,
                            )
        self.table.bind(on_row_press=self.row_press)
        head = MDLabel(text = datetime.now().strftime('%A'),
                        halign = 'center',
                        font_style = 'H3',
                        pos_hint={"center_x":0.5,"center_y":0.9},
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color
                        )
        self.confirm = MDRectangleFlatButton(text="CONFIRM",
                                    on_release=self.confirm_action,
                                    text_color=self.theme_cls.primary_color,
                                    pos_hint={"center_x":0.8,"center_y":0.1}
                                    )
        self.screen.add_widget(head)
        self.screen.add_widget(self.table)
        self.screen.add_widget(self.confirm)
        return self.screen

    def row_press(self, instance_table, instance_row):
        self.row_no = int(instance_row.index/5)
        self.weight = Builder.load_string(text_field_helper)
        self.dialog = MDDialog(text=instance_row.text + "\n\n",
                        size_hint=(0.8,1),
                        buttons=[MDRectangleFlatButton(text="OK",
                                                    on_release=self.close_dialog,
                                                    text_color=self.theme_cls.primary_color,
                                                    pos_hint={"center_x":1,"center_y":0.5})]
                                )
        self.dialog.add_widget(self.weight)
        self.dialog.open()

    def close_dialog(self, obj):
        if self.weight.text != "":
            list_current_table_row = list(self.current_table[self.row_no])
            list_current_table_row[4] = self.weight.text
            self.current_table[self.row_no] = tuple(list_current_table_row)
            self.table = MDDataTable(pos_hint={"center_x":0.5,"center_y":0.5},
                                size_hint=(0.9,0.6),
                                rows_num=9,
                                column_data=[
                                    ("No.",dp(8)),
                                    ("Exercise",dp(80)),
                                    ("Repeats",dp(20)),
                                    ("Last weight",dp(20)),
                                    ("New weight",dp(20))
                                ],
                                row_data=self.current_table
                                )
            self.table.bind(on_row_press=self.row_press)
            self.screen.add_widget(self.table)
        self.dialog.dismiss()

    def confirm_action(self):
        pass

if __name__ == "__main__":
    MyApp().run()
