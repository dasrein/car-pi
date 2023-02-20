import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

import brightness

# import audacious

Config.set("graphics", "resizable", True)


class MyLayout(FloatLayout):
    pass


class MyApp(App):  # <- Main Class
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
