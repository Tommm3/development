import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty

class MyGrid(Widget):
    output = ObjectProperty(None)
    result = ObjectProperty(None)

    def btn1(self):
        self.output.text+="1"
    def btn2(self):
        self.output.text+="2"
    def btn3(self):
        self.output.text+="3"
    def btn4(self):
        self.output.text+="4"
    def btn5(self):
        self.output.text+="5"
    def btn6(self):
        self.output.text+="6"
    def btn7(self):
        self.output.text+="7"
    def btn8(self):
        self.output.text+="8"
    def btn9(self):
        self.output.text+="9"
    def btnPlus(self):
        self.output.text+="+"
    def btnMinus(self):
        self.output.text+="-"
    def btnMultiply(self):
        self.output.text+="*"
    def btnDivide(self):
        self.output.text+="/"
    def btnPower(self):
        self.output.text+="**"
    def btnNegate(self):
        pass
    def btn0(self):
        self.output.text+="0"
    def btnPoint(self):
        self.output.text+="."
    def btnResult(self):
        self.result.text = str(eval(self.output.text))
        self.output.text = ""
    def btnBackspace(self):
        self.output.text = self.output.text[:-1]
    def btnCancel(self):
        self.output.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
