#kivy
import kivy
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
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
import os

Window.size = (1600, 1200)

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

    def guardarTransferencia(self,fecha,numTransferencia):
        if not fecha or not numTransferencia:
            pop = Popup(title='Transferencias',
            content=Label(text='Por favor no cargue una transferencia vacia.'),
            size_hint=(None, None), size=(400, 400))
            pop.open()
        else:
            base = conexionBaseDeDatos()
            engine = base.conexion
            connection = engine.connect()
            metadata = db.MetaData()
            transferencias = db.Table('transferencias', metadata, autoload=True, autoload_with=engine)
            fechaCreacion = datetime.now()
            query = db.insert(transferencias).values(fecha=fecha,num_transferencia=numTransferencia,created=fechaCreacion) 
            ResultProxy = connection.execute(query)
            if( ResultProxy ):
                pop = Popup(title='Transferencias',
                content=Label(text='Se ha creado la transferencia con exito.'),
                size_hint=(None, None), size=(400, 400))
                pop.open()

    def guardarLibros(self,nombreLibro,razonSocialLibro,cbuLibro,cuilLibro):
        if not nombreLibro or not razonSocialLibro or not cbuLibro or not cuilLibro:
            pop = Popup(title='Libros',
            content=Label(text='Por favor no cargue libro vacio.'),
            size_hint=(None, None), size=(400, 400))
            pop.open()
        else:
            base = conexionBaseDeDatos()
            engine = base.conexion
            connection = engine.connect()
            metadata = db.MetaData()
            libros = db.Table('libros', metadata, autoload=True, autoload_with=engine)
            fechaCreacion = datetime.now()
            query = db.insert(libros).values(name=nombreLibro,razon_social=razonSocialLibro,cbu=cbuLibro,cuil=cuilLibro,created=fechaCreacion) 
            ResultProxy = connection.execute(query)
            if( ResultProxy ):
                pop = Popup(title='Libros',
                content=Label(text='Se ha creado el libro con exito.'),
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

        def eliminarEstado(self,idEstado,estadoName,estadoFechaCreacion,botonEditar,botonEliminar):
            base = conexionBaseDeDatos()
            engine = base.conexion
            connection = engine.connect()
            query = db.delete(estados)
            query = query.where(estados.columns.id == idEstado)
            results = connection.execute(query)
            if(results):
                self.root.ids.listado_de_estados.remove_widget(estadoName)
                self.root.ids.listado_de_estados.remove_widget(estadoFechaCreacion)
                self.root.ids.listado_de_estados.remove_widget(estadoName)
                self.root.ids.listado_de_estados.remove_widget(botonEditar)
                self.root.ids.listado_de_estados.remove_widget(botonEliminar)

        def edicionEstado(idEstado,estadoAnterior,val,estadoName,pop):
            queryActualizar = db.update(estados).values(name = val).where(estados.columns.id == idEstado)
            ResultProxy = connection.execute(queryActualizar)
            if(ResultProxy):
                estadoName.text = str('[color=000000]'+val+'[/color]')
                print('jaja')
                pop.dismiss()

        def editarEstado(self,idEstado,estadoName):

            query = db.select([estados]).where(estados.columns.id == idEstado)
            ResultProxy = connection.execute(query)
            ResultSet = ResultProxy.fetchall()
            estadoAnterior = ResultSet[0][1];

            pop = Popup(title='Modificar estado',
            size_hint=(None, None), size=(400, 400))

            layout       = BoxLayout( padding = 10 )
            inputEdicion = TextInput(id="txt_input_nombre_estado_edicion",text = estadoAnterior)
            botonParaActualizar = Button(text = "Actualizar",on_press=lambda x:edicionEstado(idEstado,estadoAnterior,inputEdicion.text,estadoName,pop))

            layout.add_widget(inputEdicion)
            layout.add_widget(botonParaActualizar)

            pop = Popup(title='Modificar estado',
            content= layout,
            size_hint=(None, None), size=(400, 400))
            pop.open()

        def listarBotones(self,idEstado,estadoName,estadoFechaCreacion):
            botonEditar = Button(text='Editar',on_press = lambda x:editarEstado(self,idEstado,estadoName))
            self.root.ids.listado_de_estados.add_widget(botonEditar)
            botonEliminar = Button(text='Eliminar',on_press = lambda x:eliminarEstado(self,idEstado,estadoName,estadoFechaCreacion,botonEditar))
            botonEliminar = Button(text='Eliminar',on_press = lambda x:eliminarEstado(self,idEstado,estadoName,estadoFechaCreacion,botonEditar,botonEliminar))
            self.root.ids.listado_de_estados.add_widget(botonEliminar)

        def recorrerArray( arrayVar ):
            for x in arrayVar[:20]:
                estadoName = Label(text='[color=000000]'+x[1]+'[/color]',font_size='20sp',markup = True)
                self.root.ids.listado_de_estados.add_widget(estadoName)
                fecha = x[2]
                #fecha_final = fecha.strftime("%m/%d/%Y, %H:%M:%S")
                fecha_final = fecha.strftime("%m/%d/%Y")
                estadoFechaCreacion = Label(text='[color=000000]'+fecha_final+'[/color]',font_size='20sp',markup = True)
                self.root.ids.listado_de_estados.add_widget(estadoFechaCreacion)
                idDelEstado = x[0]
                listarBotones(self,idDelEstado,estadoName,estadoFechaCreacion)

        def mostrarTabla():
            ## Agrego las cabeceras de la tabla
            self.root.ids.listado_de_estados.clear_widgets()
            estadoName = Label(id='hola',text='[color=000000]Nombre[/color]',font_size='22sp',markup = True,line_height = 150)
            self.root.ids.listado_de_estados.add_widget(estadoName)
            fechaDeCreacion = Label(text='[color=000000]Fecha creación[/color]',font_size='22sp',markup = True,line_height = 150)
            self.root.ids.listado_de_estados.add_widget(fechaDeCreacion)
            acciones = Label(text='[color=000000]Acciones[/color]',font_size='22sp',markup = True,line_height = 150)
            self.root.ids.listado_de_estados.add_widget(acciones)
            campoVacio = Label(text='[color=000000][/color]',font_size='22sp',markup = True,line_height = 150)
            self.root.ids.listado_de_estados.add_widget(campoVacio)
            # traigo los datos            
            query = db.select([estados])
            ResultProxy = connection.execute(query)
            ResultSet = ResultProxy.fetchall()
            ## Se muestran las filas                        
            print(recorrerArray( ResultSet ))

        mostrarTabla()

    '''
        Muestra transferencias
    '''            
    def mostrarTransferencias(self, **kwargs):

        ## declaro la conexion y la tabla estados que es la que voy a usar en esta funcion
        base = conexionBaseDeDatos()
        engine = base.conexion
        connection = engine.connect()
        metadata = db.MetaData()
        transferencias = db.Table('transferencias', metadata, autoload=True, autoload_with=engine)

        def eliminarTransferencia(self,idTransferencia,fechaTrans,numeroTransferencia,botonEditar,botonEliminar,fechaTransCreacion):
            base = conexionBaseDeDatos()
            engine = base.conexion
            connection = engine.connect()
            query = db.delete(transferencias)
            query = query.where(transferencias.columns.id == idTransferencia)
            results = connection.execute(query)
            if(results):
                self.root.ids.listado_de_transferencias.remove_widget(fechaTrans)
                self.root.ids.listado_de_transferencias.remove_widget(numeroTransferencia)
                self.root.ids.listado_de_transferencias.remove_widget(fechaTrans)
                self.root.ids.listado_de_transferencias.remove_widget(botonEditar)
                self.root.ids.listado_de_transferencias.remove_widget(botonEliminar)
                self.root.ids.listado_de_transferencias.remove_widget(fechaTransCreacion)

        def edicionTransferencia(idTransferencia,transferenciaAnterior,val,val2,fechaTrans,numeroTransferencia,pop):
            queryActualizar = db.update(transferencias).values(fecha = val,num_transferencia = val2).where(transferencias.columns.id == idTransferencia)
            ResultProxy = connection.execute(queryActualizar)
            if(ResultProxy):
                fechaTrans.text = str('[color=000000]'+val+'[/color]')
                numeroTransferencia.text = str('[color=000000]'+val2+'[/color]')
                print('jaja')
                pop.dismiss()

        def editarTransferencia(self,idTransferencia,fechaTrans,numeroTransferencia):


            query = db.select([transferencias]).where(transferencias.columns.id == idTransferencia)
            ResultProxy = connection.execute(query)
            ResultSet = ResultProxy.fetchall()
            transferenciaAnteriorFecha = ResultSet[0][1];
            transferenciaAnteriorFecha = transferenciaAnteriorFecha.strftime("%Y-%m-%d")
            numTransAnterior = ResultSet[0][2];

            pop = Popup(title='Modificar transferencia',
            size_hint=(None, None), size=(400, 400))

            layout       = BoxLayout( orientation='vertical' )
            labelFecha = Label(text = "Fecha transferencia")
            inputEdicion = TextInput(id="txt_input_fecha_transferencia_edicion",text = transferenciaAnteriorFecha)
            labelNumeroDeTransferencia = Label(text = "Número de transferencia")
            inputEdicionNumTrans = TextInput(id="txt_input_num_transferencia_edicion",text = str(numTransAnterior))
            botonParaActualizar = Button(text = "Actualizar",on_press=lambda x:edicionTransferencia(idTransferencia,transferenciaAnteriorFecha,inputEdicion.text,inputEdicionNumTrans.text,fechaTrans,numeroTransferencia,pop))

            layout.add_widget(labelFecha)
            layout.add_widget(inputEdicion)
            layout.add_widget(labelNumeroDeTransferencia)
            layout.add_widget(inputEdicionNumTrans)
            layout.add_widget(botonParaActualizar)

            pop = Popup(title='Modificar transferencia',
            content= layout,
            size_hint=(None, None), size=(400, 400))
            pop.open()

        def listarBotonesTransferencia(self,idTransferencia,fechaTrans,numeroTransferencia,fechaTransCreacion):
            botonEditar = Button(text='Editar',on_press = lambda x:editarTransferencia(self,idTransferencia,fechaTrans,numeroTransferencia))
            self.root.ids.listado_de_transferencias.add_widget(botonEditar)
            botonEliminar = Button(text='Eliminar',on_press = lambda x:eliminarTransferencia(self,idTransferencia,fechaTrans,numeroTransferencia,botonEditar))
            botonEliminar = Button(text='Eliminar',on_press = lambda x:eliminarTransferencia(self,idTransferencia,fechaTrans,numeroTransferencia,botonEditar,botonEliminar,fechaTransCreacion))
            self.root.ids.listado_de_transferencias.add_widget(botonEliminar)

        def recorrerArrayTransferencias( arrayVar ):
            for x in arrayVar[:20]:
                fecha = x[1]
                #fecha_final = fecha.strftime("%m/%d/%Y, %H:%M:%S")
                fecha_final = fecha.strftime("%m/%d/%Y")
                fechaTrans = Label(text='[color=000000]'+fecha_final+'[/color]',font_size='20sp',markup = True)
                self.root.ids.listado_de_transferencias.add_widget(fechaTrans)
                numeroTransferencia = Label(text='[color=000000]'+str(x[2])+'[/color]',font_size='20sp',markup = True)
                self.root.ids.listado_de_transferencias.add_widget(numeroTransferencia)
                fecha = x[3]
                fecha_final = fecha.strftime("%m/%d/%Y")
                fechaTransCreacion = Label(text='[color=000000]'+fecha_final+'[/color]',font_size='20sp',markup = True)
                self.root.ids.listado_de_transferencias.add_widget(fechaTransCreacion)
                
                idDelEstado = x[0]
                listarBotonesTransferencia(self,idDelEstado,fechaTrans,numeroTransferencia,fechaTransCreacion)

        def mostrarTablaTransferencias():
            ## Agrego las cabeceras de la tabla
            self.root.ids.listado_de_transferencias.clear_widgets()
            fechaTrans = Label(id='hola',text='[color=000000]Fecha transferencia[/color]',font_size='22sp',markup = True,line_height = 150)
            self.root.ids.listado_de_transferencias.add_widget(fechaTrans)
            numeroTrans = Label(text='[color=000000]Número transferencia[/color]',font_size='22sp',markup = True,line_height = 150)
            self.root.ids.listado_de_transferencias.add_widget(numeroTrans)
            fechaDeCreacion = Label(text='[color=000000]Fecha creación[/color]',font_size='22sp',markup = True,line_height = 150)
            self.root.ids.listado_de_transferencias.add_widget(fechaDeCreacion)            
            acciones = Label(text='[color=000000]Acciones[/color]',font_size='22sp',markup = True,line_height = 150)
            self.root.ids.listado_de_transferencias.add_widget(acciones)
            campoVacio = Label(text='[color=000000][/color]',font_size='22sp',markup = True,line_height = 150)
            self.root.ids.listado_de_transferencias.add_widget(campoVacio)
            # traigo los datos            
            query = db.select([transferencias])
            ResultProxy = connection.execute(query)
            ResultSet = ResultProxy.fetchall()
            ## Se muestran las filas                        
            print(recorrerArrayTransferencias( ResultSet ))

        mostrarTablaTransferencias()


class ver_estados(Screen):
    pass

#sm = ScreenManager()
#sm.add_widget(ver_los_estados(name='ver_estados'))


class screen1(Screen):  
    def build(self):
           print("jaja 1")

if __name__ == '__main__':
    MainApp().run()