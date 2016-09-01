import kivy
kivy.require('1.9.1')

from kivy.app import App


class Calkvlator(App):

    def print_number(self, number):
        text = "{}{}".format(self.root.display.text, number)
        self.root.display.text = text

    def print_operator(self, operator):
        text = "{} {} ".format(self.root.display.text, operator)
        self.root.display.text = text

    def clear_display(self):
        self.root.display.text = ""

    def del_char(self):
        self.root.display.text = self.root.display.text[:-1]


if __name__ == "__main__":
    Calkvlator().run()
