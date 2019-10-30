#kivy
import kivy
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
## material design
from kivymd.theming import ThemeManager
## python
import sys #esto sirve para poner un die con sys.exit()
import json
import math
import configparser
import sqlalchemy as db
import json
import pandas as pd

Config.set('graphics', 'width', 1600)
Config.set('graphics', 'height', 800)


class MainApp(App,BoxLayout):
    theme_cls = ThemeManager()

    def guardarEstado(self,val):
        print(val)
        pop = Popup(title='Invalid Form',
            content=Label(text='Please fill in all inputs with valid information.'),
            size_hint=(None, None), size=(400, 400))

        pop.open()

class screen1(Screen):	
    def build(self):
	       print("jaja 1")

if __name__ == '__main__':
    MainApp().run()