import kivymd
from kivymd.app import MDApp

from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton,  MDRectangleFlatIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.metrics import dp

from datetime import datetime

import pandas as pd

from openpyxl import load_workbook

from helpers import text_field_helper


# get the current weekday number
weekday = datetime.now().weekday()

# create a list of tuples of exercises info
def get_init_exercise_tuple(wd):
    # get info about the columns/rows in current xlsx file
    reader = pd.read_excel(r'silka.xlsx')
    # read the exercises for a specific weekday
    if wd==0:
        df = pd.read_excel('silka.xlsx', skiprows=0, usecols=[0,1,len(reader.columns)-1], nrows=8)
    elif wd==1:
        df = pd.read_excel('silka.xlsx', skiprows=8, usecols=[0,1,len(reader.columns)-2], nrows=9)
    elif wd==3:
        df = pd.read_excel('silka.xlsx', skiprows=17, usecols=[0,1,len(reader.columns)-2], nrows=8)
    elif wd==4:
        df = pd.read_excel('silka.xlsx', skiprows=25, usecols=[0,1,len(reader.columns)-2], nrows=5)
    else:
        return ""
        exit()
    # add a dummy column for new weight for user to put and increment indexes to start from 1
    df['new'] = pd.Series(["NEI"]*len(df), index=df.index)
    df.index+=1
    return df.to_records()


class MyApp(MDApp):
    # call a built-in method to build App
    def build(self):
        # set initial conditions
        self.current_table = get_init_exercise_tuple(weekday)
        self.set_style()
        self.screen = Screen()
        # show exerecises table if there are any for today
        if weekday in (0,1,3,4):
            self.update_screen()
        else:
            self.no_exercises_screen()
        return self.screen


    # act on clicking on exercise
    def row_press(self, instance_table, instance_row):
        # calculate row number
        self.row_no = int(instance_row.index/5)
        # show dialog window with title, tekst input and OK button
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

    # act on confirming user's input
    def close_dialog(self, obj):
        # update current_table string by user's text input if it is not empty
        if self.weight.text != "":
            list_current_table_row = list(self.current_table[self.row_no])
            list_current_table_row[4] = self.weight.text
            self.current_table[self.row_no] = tuple(list_current_table_row)
            self.update_screen()
        # close dialog window
        self.dialog.dismiss()

    # act on confirming new weight data
    def confirm_action(self,obj):
        # create a dictionary with new data
        temp = []
        for last in self.current_table:
            temp.append(last[-1])
        writer = pd.ExcelWriter('silka.xlsx', engine='openpyxl')
        # read and copy existin xlsx file
        writer.book = load_workbook('silka.xlsx')
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        reader = pd.read_excel(r'silka.xlsx')
        masa_dict = {('masa'+str(len(reader.columns)-2)):temp}
        df = pd.DataFrame(masa_dict)
        # write to excel, use a correct place in sheet depending on a weekday
        if weekday == 0:
            df.to_excel(writer,index=False,startcol=len(reader.columns))
            print(reader.nrows)
        elif weekday == 1:
            df.to_excel(writer,index=False,startcol=len(reader.columns)-1,startrow=9,header=False)
        elif weekday == 3:
            df.to_excel(writer,index=False,startcol=len(reader.columns)-1,startrow=18,header=False)
        elif weekday == 4:
            df.to_excel(writer,index=False,startcol=len(reader.columns)-1,startrow=26,header=False)
        writer.close()

    # update data on screen
    def update_screen(self):
        # erase existing objects
        self.screen.canvas.clear()
        # add a valid datateble, confirm button and title
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
        self.confirm = MDRectangleFlatButton(text="CONFIRM",
                                    on_release=self.confirm_action,
                                    text_color=self.theme_cls.primary_color,
                                    pos_hint={"center_x":0.8,"center_y":0.1}
                                    )
        head = MDLabel(text = "Monday",
                        halign = 'center',
                        font_style = 'H3',
                        pos_hint={"center_x":0.5,"center_y":0.9},
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color
                        )
        self.screen.add_widget(self.table)
        self.screen.add_widget(self.confirm)
        self.screen.add_widget(head)

    # show a screen with no exercises
    def no_exercises_screen(self):
        # erase existing objects
        self.screen.canvas.clear()
        # add title and info to screen
        info = MDLabel(text = "No exercises for today",
                        halign = 'center',
                        font_style = 'H4',
                        pos_hint={"center_x":0.5,"center_y":0.5},
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color
                        )
        head = MDLabel(text = datetime.now().strftime('%A'),
                        halign = 'center',
                        font_style = 'H3',
                        pos_hint={"center_x":0.5,"center_y":0.9},
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color
                        )
        self.screen.add_widget(head)
        self.screen.add_widget(info)

    # set style properties
    def set_style(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

# run App
if __name__ == "__main__":
    MyApp().run()
