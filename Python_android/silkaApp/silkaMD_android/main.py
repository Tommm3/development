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

from datetime import datetime, timedelta

from kivy.storage.jsonstore import JsonStore

from helpers import text_field_helper


# get the current weekday number and name
weekdayNumber = datetime.now()
# indicate the saveFile
jsonSaveFile = 'silka_final3.json'
# indicate exercise days
exerciseDays = (0,1,3,4)


# create a list of tuples of exercises info
def get_init_exercise_tuple(wd, saveFile):
    store = JsonStore(saveFile)
    listOfTuples = []
    counter=1
    if wd==0:
        exRange = store.keys()[:8]
    elif wd==1:
        exRange = store.keys()[8:17]
    elif wd==3:
        exRange = store.keys()[17:25]
    elif wd==4:
        exRange = store.keys()[25:30]
    else:
        return ""
        exit()
    for k in exRange:
        dict_json = store.get(k)
        list_json=[counter]
        counter+=1
        list_json.extend([dict_json['name'], dict_json['sets'], dict_json['repeats'],dict_json['weights'][-1], "NEI"])
        listOfTuples.append(tuple(list_json))
    return listOfTuples


def check_for_nei(listOfTuples):
    isValue = False
    for item in listOfTuples:
        if item[-1] == 'NEI':
            isValue = True
    return isValue


def check_for_values(listOfTuples):
    isValue = False
    for item in listOfTuples:
        if item[-1] != 'NEI':
            isValue = True
    return isValue


class MyApp(MDApp):
    # call a built-in method to build App
    def build(self):
        # set initial conditions
        self.current_table = get_init_exercise_tuple(weekdayNumber.weekday(), jsonSaveFile)
        self.set_style()
        self.screen = Screen()
        # show exerecises table if there are any for today
        self.update_day_screen()
        return self.screen


    # act on clicking on exercise
    def row_press(self, instance_table, instance_row):
        # calculate row number
        self.row_no = int(instance_row.index/6)
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
            list_current_table_row[5] = self.weight.text
            self.current_table[self.row_no] = tuple(list_current_table_row)
            self.update_screen()
        # close dialog window
        self.dialog.dismiss()


    # act on confirming new weight data
    def confirm_action(self,obj):
        # create a dictionary with new data
        store = JsonStore('silka_final3.json')
        if not check_for_nei(self.current_table):
            if weekdayNumber.weekday()==0:
                exRange = store.keys()[:8]
            elif weekdayNumber.weekday()==1:
                exRange = store.keys()[8:17]
            elif weekdayNumber.weekday()==3:
                exRange = store.keys()[17:25]
            elif weekdayNumber.weekday()==4:
                exRange = store.keys()[25:30]
            counter = 0
            for k in exRange:
                dict_json = store.get(k)
                tabs = dict_json['weights']
                if len(tabs) < (int(datetime.now().strftime("%V"))-38):
                    tabs.append(self.current_table[counter][-1])
                else:
                    tabs[-1]=self.current_table[counter][-1]
                counter+=1
                store.put(k, name=dict_json['name'], sets=dict_json['sets'], repeats=dict_json['repeats'], weights=tabs)
            self.show_confirm_dialog("Weights updated")
            self.current_table = get_init_exercise_tuple(weekdayNumber.weekday(), jsonSaveFile)
            self.update_day_screen()
        else:
            self.show_confirm_dialog("Add new weight to each exercise")

    def show_confirm_dialog(self, textInfo):
        self.dialog_confirm = MDDialog(text=textInfo,
                                size_hint=(0.8,1)
                                )
        self.dialog_confirm.open()


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
                                ("Sets",dp(20)),
                                ("Repeats",dp(20)),
                                ("Last weight",dp(20)),
                                ("New weight",dp(20))
                            ],
                            row_data=self.current_table,
                            )
        self.table.bind(on_row_press=self.row_press)
        self.confirm = MDRectangleFlatButton(text="CONFIRM",
                                    size_hint=(0.25,0.1),
                                    on_release=self.confirm_action,
                                    text_color=self.theme_cls.primary_color,
                                    pos_hint={"center_x":0.8,"center_y":0.1}
                                    )
        head = MDLabel(text = weekdayNumber.strftime("%A"),
                        halign = 'center',
                        font_style = 'H3',
                        pos_hint={"center_x":0.5,"center_y":0.9},
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color
                        )
        self.button_left = MDRectangleFlatButton(text="<",
                                    size_hint=(0.14,0.1),
                                    on_release=self.day_before,
                                    text_color=self.theme_cls.primary_color,
                                    pos_hint={"center_x":0.08,"center_y":0.9}
                                    )
        self.button_right = MDRectangleFlatButton(text=">",
                                    size_hint=(0.14,0.1),
                                    on_release=self.day_after,
                                    text_color=self.theme_cls.primary_color,
                                    pos_hint={"center_x":0.92,"center_y":0.9}
                                    )
        self.screen.add_widget(self.table)
        self.screen.add_widget(self.confirm)
        self.screen.add_widget(self.button_left)
        self.screen.add_widget(self.button_right)
        self.screen.add_widget(head)


    def day_before(self,obj):
        global weekdayNumber
        if not check_for_values(self.current_table) or (weekdayNumber.weekday() not in exerciseDays):
            if weekdayNumber.weekday() > 0:
                weekdayNumber-=timedelta(days=1)
            self.current_table = get_init_exercise_tuple(weekdayNumber.weekday(), jsonSaveFile)
            self.update_day_screen()
        else:
            self.show_day_before_dialog("You are in the middle of your workout. Do you want to switch day?")


    def show_day_before_dialog(self, info):
        self.dialog_day_before = MDDialog(text=info,
                                size_hint=(0.8,1),
                                buttons=[MDRectangleFlatButton(text="YES",
                                                            on_release=self.day_before_confirmed,
                                                            text_color=self.theme_cls.primary_color,
                                                            pos_hint={"center_x":1,"center_y":0.5}),
                                        MDRectangleFlatButton(text="NO",
                                                            on_release=self.close_dialog_day_before,
                                                            text_color=self.theme_cls.primary_color,
                                                            pos_hint={"center_x":1,"center_y":0.5})]
                                )
        self.dialog_day_before.open()

    def close_dialog_day_before(self,obj):
        self.dialog_day_before.dismiss()


    def day_before_confirmed(self,obj):
        global weekdayNumber
        if weekdayNumber.weekday() > 0:
            weekdayNumber-=timedelta(days=1)
        self.current_table = get_init_exercise_tuple(weekdayNumber.weekday(), jsonSaveFile)
        self.update_day_screen()
        self.dialog_day_before.dismiss()


    def day_after(self,obj):
        global weekdayNumber
        if not check_for_values(self.current_table) or (weekdayNumber.weekday() not in exerciseDays):
            if weekdayNumber.weekday() < 6:
                weekdayNumber+=timedelta(days=1)
            self.current_table = get_init_exercise_tuple(weekdayNumber.weekday(), jsonSaveFile)
            self.update_day_screen()
        else:
            self.show_day_after_dialog("You are in the middle of your workout. Do you want to switch day?")


    def show_day_after_dialog(self, info):
        self.dialog_day_after = MDDialog(text=info,
                                size_hint=(0.8,1),
                                buttons=[MDRectangleFlatButton(text="YES",
                                                            on_release=self.day_after_confirmed,
                                                            text_color=self.theme_cls.primary_color,
                                                            pos_hint={"center_x":1,"center_y":0.5}),
                                        MDRectangleFlatButton(text="NO",
                                                            on_release=self.close_dialog_day_after,
                                                            text_color=self.theme_cls.primary_color,
                                                            pos_hint={"center_x":1,"center_y":0.5})]
                                )
        self.dialog_day_after.open()


    def close_dialog_day_after(self,obj):
        self.dialog_day_after.dismiss()


    def day_after_confirmed(self,obj):
        global weekdayNumber
        if weekdayNumber.weekday() < 6:
            weekdayNumber+=timedelta(days=1)
        self.current_table = get_init_exercise_tuple(weekdayNumber.weekday(), jsonSaveFile)
        self.update_day_screen()
        self.dialog_day_after.dismiss()


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
        head = MDLabel(text = weekdayNumber.strftime('%A'),
                        halign = 'center',
                        font_style = 'H3',
                        pos_hint={"center_x":0.5,"center_y":0.9},
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color
                        )
        self.button_left = MDRectangleFlatButton(text="<",
                                    size_hint=(0.14,0.1),
                                    on_release=self.day_before,
                                    text_color=self.theme_cls.primary_color,
                                    pos_hint={"center_x":0.08,"center_y":0.9}
                                    )
        self.button_right = MDRectangleFlatButton(text=">",
                                    size_hint=(0.14,0.1),
                                    on_release=self.day_after,
                                    text_color=self.theme_cls.primary_color,
                                    pos_hint={"center_x":0.92,"center_y":0.9}
                                    )
        self.screen.add_widget(head)
        self.screen.add_widget(self.button_left)
        self.screen.add_widget(self.button_right)
        self.screen.add_widget(info)


    # set style properties
    def set_style(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"


    def update_day_screen(self):
        if weekdayNumber.weekday() in exerciseDays:
            self.update_screen()
        else:
            self.no_exercises_screen()


# run App
if __name__ == "__main__":
    MyApp().run()
