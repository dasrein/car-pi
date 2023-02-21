import kivy
from kivy.config import Config

Config.set("graphics", "fullscreen", "1")
Config.set("graphics", "width", "800")
Config.set("graphics", "height", "600")
Config.write()
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


import brightness

# import audacious


class MyLayout(FloatLayout):
    pass


class MyApp(App):  # <- Main Class
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
