import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.properties import BooleanProperty


class Calkvlator(App):
    clear_bool = BooleanProperty(False)

    def print_number(self, number):
        if self.clear_bool:
            self.clear_display()

        text = "{}{}".format(self.root.display.text, number)
        self.root.display.text = text

    def print_operator(self, operator):
        if self.clear_bool:
            self.clear_bool = False

        text = "{} {} ".format(self.root.display.text, operator)
        self.root.display.text = text

    def clear_display(self):
        self.root.display.text = ""
        self.clear_bool = False

    def del_char(self):
        self.root.display.text = self.root.display.text[:-1]

    def calculate(self):
        self.root.display.text = str(eval(self.root.display.text))
        self.clear_bool = True


if __name__ == "__main__":
    Calkvlator().run()
