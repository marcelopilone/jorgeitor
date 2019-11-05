#kivy
import kivy
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.config import Config
## material design
from kivymd.theming import ThemeManager

## archivos python hechos por nosotros

from database import conexionBaseDeDatos
from estados import EstadoScreen

Config.set('graphics', 'width', 1600)
Config.set('graphics', 'height', 800)


class JorgeitorApp(App,BoxLayout,GridLayout):
    theme_cls = ThemeManager()



if __name__ == '__main__':
    JorgeitorApp().run()