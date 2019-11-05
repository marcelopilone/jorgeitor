from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from database import conexionBaseDeDatos

class EstadoItem(Widget):
    idx = NumericProperty(None)
    name = StringProperty('')
    pass



class EstadoList(BoxLayout):

    def build(self):
        ## declaro la conexion y la tabla estados que es la que voy a usar en esta funcion
        base = conexionBaseDeDatos()
        engine = base.conexion
        connection = engine.connect()
        metadata = db.MetaData()
        estados = db.Table('estados', metadata, autoload=True, autoload_with=engine)



class EstadoScreen(Screen):


    def crear_estado(self):
        print("apretome esta")
        pass

    def crear_nuevo_estado(self):
        layout       = BoxLayout( padding = 10, orientation = 'horizontal' )
        inputEdicion = TextInput()
        botonParaActualizar = Button(text = "Crear", on_press = self.crear_estado )

        layout.add_widget(inputEdicion)
        layout.add_widget(botonParaActualizar)

        pop = Popup(title='Modificar estado',
        content= layout,
        size_hint=(None, None), size=(400, 400))
        pop.open()



    def on_enter(self):
        print("start inicio "*5)


        def eliminarEstado(self,idEstado,estadoName,estadoFechaCreacion,botonEditar,botonEliminar):
            base = conexionBaseDeDatos()
            engine = base.conexion
            connection = engine.connect()
            query = db.delete(estados)
            query = query.where(estados.columns.id == idEstado)
            results = connection.execute(query)
            if(results):
                self.ids.listado_de_estados.remove_widget(estadoName)
                self.ids.listado_de_estados.remove_widget(estadoFechaCreacion)
                self.ids.listado_de_estados.remove_widget(estadoName)
                self.ids.listado_de_estados.remove_widget(botonEditar)
                self.ids.listado_de_estados.remove_widget(botonEliminar)

        def edicionEstado(idEstado,estadoAnterior,val):
            queryActualizar = db.update(estados).values(name = val).where(estados.columns.id == idEstado)
            ResultProxy = connection.execute(queryActualizar)
            if(ResultProxy):
                print('jaja')

        def editarEstado(self,idEstado):

            query = db.select([estados]).where(estados.columns.id == idEstado)
            ResultProxy = connection.execute(query)
            ResultSet = ResultProxy.fetchall()
            estadoAnterior = ResultSet[0][1];


            layout       = BoxLayout( padding = 10 )
            inputEdicion = TextInput(id="txt_input_nombre_estado_edicion",text = estadoAnterior)
            botonParaActualizar = Button(text = "Actualizar",on_press=lambda x:edicionEstado(idEstado,estadoAnterior,inputEdicion.text))

            layout.add_widget(inputEdicion)
            layout.add_widget(botonParaActualizar)

            pop = Popup(title='Modificar estado',
            content= layout,
            size_hint=(None, None), size=(400, 400))
            pop.open()

        def listarBotones(self,idEstado,estadoName,estadoFechaCreacion):
            botonEditar = Button(text='Editar',on_press = lambda x:editarEstado(self,idEstado))
            self.ids.listado_de_estados.add_widget(botonEditar)
            botonEliminar = Button(text='Eliminar',on_press = lambda x:eliminarEstado(self,idEstado,estadoName,estadoFechaCreacion,botonEditar))
            botonEliminar = Button(text='Eliminar',on_press = lambda x:eliminarEstado(self,idEstado,estadoName,estadoFechaCreacion,botonEditar,botonEliminar))
            self.ids.listado_de_estados.add_widget(botonEliminar)

        def recorrerArray( arrayVar ):
            for x in arrayVar[:20]:
                estadoName = Label(text='[color=000000]'+x[1]+'[/color]',font_size='20sp',markup = True)
                self.ids.listado_de_estados.add_widget(estadoName)
                fecha = x[2]
                #fecha_final = fecha.strftime("%m/%d/%Y, %H:%M:%S")
                fecha_final = fecha.strftime("%m/%d/%Y")
                estadoFechaCreacion = Label(text='[color=000000]'+fecha_final+'[/color]',font_size='20sp',markup = True)
                self.ids.listado_de_estados.add_widget(estadoFechaCreacion)
                idDelEstado = x[0]
                listarBotones(self,idDelEstado,estadoName,estadoFechaCreacion)

        def mostrarTabla():
            ## Agrego las cabeceras de la tabla
            self.ids.listado_de_estados.clear_widgets()
            estadoName = Label(id='hola',text='[color=000000]Nombre[/color]',font_size='22sp',markup = True,line_height = 150)
            self.ids.listado_de_estados.add_widget(estadoName)
            fechaDeCreacion = Label(text='[color=000000]Fecha creación[/color]',font_size='22sp',markup = True,line_height = 150)
            self.ids.listado_de_estados.add_widget(fechaDeCreacion)
            acciones = Label(text='[color=000000]Acciones[/color]',font_size='22sp',markup = True,line_height = 150)
            self.ids.listado_de_estados.add_widget(acciones)
            campoVacio = Label(text='[color=000000][/color]',font_size='22sp',markup = True,line_height = 150)
            self.ids.listado_de_estados.add_widget(campoVacio)
            # traigo los datos            
            query = db.select([estados])
            ResultProxy = connection.execute(query)
            ResultSet = ResultProxy.fetchall()
            ## Se muestran las filas                        
            print(recorrerArray( ResultSet ))





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
    


class EstadoGrid(GridLayout):
    pass



