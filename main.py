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
from kivy.uix.button import Button
## material design
from kivymd.theming import ThemeManager
from kivymd.uix.button import MDIconButton
## python
import sys #esto sirve para poner un die con sys.exit()
import json
import math
import configparser
import sqlalchemy as db
import json
import pandas as pd
from datetime import datetime
from pprint import pprint # esto es como el debug que usamos en cakephp se usa pprint( var )
## archivos python hechos por nosotros
from database import *

Config.set('graphics', 'width', 1600)
Config.set('graphics', 'height', 800)

class MainApp(App,BoxLayout,GridLayout):
    theme_cls = ThemeManager()

    def probando():
        print('asdasd')

    jaja = probando()

    

    def guardarEstado(self,val):
        if not val:
            pop = Popup(title='Estados',
            content=Label(text='Por favor no cargue un estado vacio.'),
            size_hint=(None, None), size=(400, 400))
            pop.open()
        else:
            base = conexionBaseDeDatos()
            engine = base.conexion
            connection = engine.connect()
            metadata = db.MetaData()
            estados = db.Table('estados', metadata, autoload=True, autoload_with=engine)
            fechaCreacion = datetime.now()
            query = db.insert(estados).values(name=val,created=fechaCreacion) 
            ResultProxy = connection.execute(query)
            if( ResultProxy ):
                pop = Popup(title='Estados',
                content=Label(text='Se ha creado el estado con exito.'),
                size_hint=(None, None), size=(400, 400))
                pop.open()


    '''
        Muestra los estados
    '''            
    def mostrarEstados(self, **kwargs):

        ## declaro la conexion y la tabla estados que es la que voy a usar en esta funcion
        base = conexionBaseDeDatos()
        engine = base.conexion
        connection = engine.connect()
        metadata = db.MetaData()
        estados = db.Table('estados', metadata, autoload=True, autoload_with=engine)

        def eliminarEstado(self,idEstado):
            base = conexionBaseDeDatos()
            engine = base.conexion
            connection = engine.connect()
            query = db.delete(estados)
            query = query.where(estados.columns.id == idEstado)
            results = connection.execute(query)
            if(results):
                self.root.ids.listado_de_estados.clear_widgets()
                Clock.schedule_once(App.get_running_app().mostrarEstados)

        def editarEstado(self,idEstado):
            print(idEstado)

        def listarBotonesParaEditar(self,idEstado):
            botonEliminar = Button(text='Editar',on_press = lambda x:editarEstado(self,idEstado))
            self.root.ids.listado_de_estados.add_widget(botonEliminar)

        def listarBotonesParaEliminar(self,idEstado):
            botonEliminar = Button(text='Eliminar',on_press = lambda x:eliminarEstado(self,idEstado))
            self.root.ids.listado_de_estados.add_widget(botonEliminar)

        def recorrerArray( arrayVar ):
            for x in arrayVar[:20]:
                estadoName = Label(text='[color=000000]'+x[1]+'[/color]',font_size='20sp',markup = True)
                self.root.ids.listado_de_estados.add_widget(estadoName)
                fecha = x[2]
                fecha_final = fecha.strftime("%m/%d/%Y, %H:%M:%S")
                estadoFechaCreacion = Label(text='[color=000000]'+fecha_final+'[/color]',font_size='20sp',markup = True)
                self.root.ids.listado_de_estados.add_widget(estadoFechaCreacion)
                idDelEstado = x[0]
                listarBotonesParaEditar(self,idDelEstado)
                listarBotonesParaEliminar(self,idDelEstado)

        def mostrarTabla():
            ## Agrego las cabeceras de la tabla
            self.root.ids.listado_de_estados.clear_widgets()
            estadoName = Label(text='[color=000000]Nombre[/color]',font_size='20sp',markup = True,line_height = 150)
            self.root.ids.listado_de_estados.add_widget(estadoName)
            fechaDeCreacion = Label(text='[color=000000]Fecha creación[/color]',font_size='20sp',markup = True,line_height = 150)
            self.root.ids.listado_de_estados.add_widget(fechaDeCreacion)
            acciones = Label(text='[color=000000]Acciones[/color]',font_size='20sp',markup = True,line_height = 150)
            self.root.ids.listado_de_estados.add_widget(acciones)
            campoVacio = Label(text='[color=000000][/color]',font_size='20sp',markup = True,line_height = 150)
            self.root.ids.listado_de_estados.add_widget(campoVacio)
            # traigo los datos            
            query = db.select([estados])
            ResultProxy = connection.execute(query)
            ResultSet = ResultProxy.fetchall()
            ## Se muestran las filas                        
            print(recorrerArray( ResultSet ))

        mostrarTabla()

        '''layoutGrid = GridLayout(size_hint=(.8,.8),pos_hint={"center_x":.5,"center_y":.5},orientation='vertical',cols=4 )

        self.root.ids.listado_de_estados.add_widget(layoutGrid)
        

        print('asdasd')'''

class ver_estados(Screen):
    pass

#sm = ScreenManager()
#sm.add_widget(ver_los_estados(name='ver_estados'))


class screen1(Screen):	
    def build(self):
	       print("jaja 1")

if __name__ == '__main__':
    MainApp().run()