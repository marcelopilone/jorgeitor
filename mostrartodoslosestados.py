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
    print()
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

