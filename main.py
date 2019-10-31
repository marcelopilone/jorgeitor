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
from kivy.uix.widget import Widget
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
import datetime
## archivos python hechos por nosotros
from database import *

Config.set('graphics', 'width', 1600)
Config.set('graphics', 'height', 800)

class MainApp(App,BoxLayout):
    theme_cls = ThemeManager()


    def guardarEstado(self,val):
        base = conexionBaseDeDatos()
        engine = base.conexion
        connection = engine.connect()
        metadata = db.MetaData()
        estados = db.Table('estados', metadata, autoload=True, autoload_with=engine)
        fechaCreacion = datetime.datetime.now()
        query = db.insert(estados).values(name=val,created=fechaCreacion) 
        ResultProxy = connection.execute(query)
        if( ResultProxy ):
            pop = Popup(title='Estados',
            content=Label(text='Se ha creado el estado con exito.'),
            size_hint=(None, None), size=(400, 400))
            pop.open()

class ver_estados(Screen):
    pass

#sm = ScreenManager()
#sm.add_widget(ver_los_estados(name='ver_estados'))


class screen1(Screen):	
    def build(self):
	       print("jaja 1")

if __name__ == '__main__':
    MainApp().run()