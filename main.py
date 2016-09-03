import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class CalkvlatorRoot(BoxLayout):
    display = ObjectProperty()


class Calkvlator(App):

    def print_number(self, number):
        text = "{}{}".format(self.root.display.text, number)
        self.root.display.text = text


if __name__ == "__main__":
    Calkvlator().run()
