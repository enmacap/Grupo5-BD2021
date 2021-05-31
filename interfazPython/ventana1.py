#para la interfaz
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#para la base de datos
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'grupo5'
DB_PASS = '12345'
DB_NAME = 'bdfuncionario'

datos = [DB_HOST, DB_USER,  DB_PASS, DB_NAME]
miConexion =MySQLdb.connect(*datos)

root = Tk()
root.title(" Grupo 5")
root.geometry("900x500")

#declacion de las variables para los campos
miId= IntVar()
miCi= StringVar()
miNombre= StringVar()
miApellido= StringVar()
miCorreo= StringVar()
miDepartamento= StringVar()
miInfectado=StringVar()
miTarjeta =StringVar()
micodigo_rfid= StringVar()

def conexionBBDD():
    DB_HOST = 'localhost'
    DB_USER = 'grupo5'
    DB_PASS = '12345'
    DB_NAME = 'bdfuncionarios'

    datos = [DB_HOST, DB_USER,  DB_PASS, DB_NAME]
    miConexion =MySQLdb.connect(*datos)
    #miCursor = miConexion.cursor()

def eliminarBBDD():
    miCursor = miConexion.cursor()
    if messagebox.askyesno(message="Los datos se perderan definitivamente, Desea continuar?", title= "ADVERTENCIA"):
        miCursor.execute("DROP TABLE Funcionario")
    else:
        pass
    limpiarCampos()
    mostar()
    miCursor.close()
    
def salirAplicacion():
    valor = messagebox.askquestion("Salir","Esta seguro que desea salir de la Aplicacion?")
    if valor == "yes":
        root.destroy()#sirve para cerrar las ventanas
        pass
    
def limpiarCampos():
    miId.set("")
    miCi.set("")
    miNombre.set("")
    miApellido.set("")
    miCorreo.set("")
    miDepartamento.set("")
    miInfectado.set("")
    miTarjeta.set("")
    micodigo_rfid.set("")
    
    
def mensaje():
    acerca = '''Aplicacion Trabajo Base de Datos \n
                Integrantes:\n
                -\n
                -\n
                -\n
                -\n
                Tutores:
                -\n
                -\n
                -\n
                '''
    messagebox.showinfo(title="INFORMACION", message= acerca)

def crearFuncionario():
    miConexion =MySQLdb.connect(*datos)
    miCursor = miConexion.cursor()
    
    try:
        sql = '''INSERT INTO funcionario( ci, nombre, apellido, correo, departamento_id, rfid_codigo)
            VALUES ( %s, %s, %s, %s, %s, %s);'''
        miCursor.execute(sql, (miCi.get(), miNombre.get(), miApellido.get(), miCorreo.get(),int(miDepartamento.get()),int(miTarjeta.get())))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error")
        pass
    limpiarCampos()
    mostrar()
    miCursor.close()
    
def crearDepartamento():
    miConexion =MySQLdb.connect(*datos)
    miCursor = miConexion.cursor()
    try:
        sql = '''INSERT INTO departamento(nombre, infectado)
            VALUES ( %s, %s);'''
        miCursor.execute(sql,(miDepartamento.get(), miInfectado.get()))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error")
        pass
    limpiarCampos()
    mostrar()
    miCursor.close()

def crearTarjeta():
    miConexion =MySQLdb.connect(*datos)
    miCursor = miConexion.cursor()
    try:
        sql = '''INSERT INTO departamento(nombre, infectado)
            VALUES ( %s, %s);'''
        miCursor.execute(sql, (micodigo_rfid.set(),miTarjeta.get()))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error")
        pass
    limpiarCampos()
    mostrar()
    miCursor.close()
    

def mostrar():
    miConexion =MySQLdb.connect(*datos)
    miCursor = miConexion.cursor()
    #para evitar que se registre los registros a la hora de mostras
    
    registro= tree.get_children()# almacenamos todos los elemntos que se encuentre en nuestra tabla si es que lo hay
    for elemento in registro:
        tree.delete(elemento)
    #extraemos los valores de la base de datos
    try:
        miCursor.execute("SELECT * FROM funcionario")
        for row in miCursor:
            tree.insert("",0,text=row[0], values= (row[1],row[2],row[3], row[4], row[5], row[6]))
    except:
        pass
    miCursor.close()

########### Tabla#########
tree= ttk.Treeview(height=10,columns=('#0','#1','#2','#3', '#4','#5','#6'))
tree.place(x=0,y=350)
tree.column('#0', width=50)
tree.heading('#0', text= "Id", anchor = CENTER)

tree.column('#1', width=100)
tree.heading('#1', text= "CI", anchor = CENTER)

tree.column('#2', width=150)
tree.heading('#2', text= "Nombre", anchor = CENTER)

tree.column('#3', width=150)
tree.heading('#3', text= "Apellido", anchor = CENTER)

tree.column('#4', width=150)
tree.heading('#4', text= "Correo", anchor = CENTER)

tree.column('#5', width=150)
tree.heading('#5', text= "Departamento", anchor = CENTER)

#tree.column('#6', width=50)
tree.heading('#6', text= "Tarjeta", anchor = CENTER)

def seleccionarUsandoClick(event):
    item= tree.identify('item', event.x,event.y)
    miId.set((tree.item(item, "text")))
    miCi.set(tree.item(item, "values")[0])
    miNombre.set(tree.item(item, "values")[1])
    miApellido.set(tree.item(item, "values")[2])
    miCorreo.set(tree.item(item, "values")[3])
    miDepartamento.set(tree.item(item, "values")[4])
    miTarjeta.set(tree.item(item, "values")[5])  
tree.bind("<Double-1>", seleccionarUsandoClick)    

def actualizarFuncionario():
    miConexion =MySQLdb.connect(*datos)
    miCursor = miConexion.cursor()
    try:
        datos = miCi.get(),miNombre.get(),miApellido.get(), miCorreo.get(),miDepartamento.get(),miTarjeta.get()
        miCursor.execute("UPDATE funcionario SET CI=?, NOMBRE=?, APELLIDO=?, CORREO=?, DEPARTAMENTO=?, TARJETA=? WHERE Id" + miId.get(), (datos))
        miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al actualizar un registro")
        pass
    limpiarCampos()
    mostrar()
    miCursor.close()

def borrarFuncionario():
    miConexion =MySQLdb.connect(*datos)
    miCursor = miConexion.cursor()
    try:
        if messagebox.askyesno(message= "Realmente desea eliminar el registro?", title= "ADVERTENCIA"):
            miCursor.execute("DELETE FROM funcionario WHERE Id=" + miId.get())
            miConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al tratar de eliminar el registro")
        pass
    limpiarCampos()
    mostrar()
    miCursor.close()
    
########## Colocar widgets en la vista##########

####Crear los menus####
menubar= Menu(root)
menubasedat= Menu(menubar, tearoff=0)
menubasedat.add_command(label= "Conectar Base de datos", command= conexionBBDD)
menubasedat.add_command(label= "Salir", command= salirAplicacion)
menubar.add_cascade(label="Inicio", menu= menubasedat)

ayudamenu= Menu(menubar, tearoff= 0)
ayudamenu.add_command(label= "Resetear Campos", command= limpiarCampos)
ayudamenu.add_command(label= "Acerca", command= mensaje)
menubar.add_cascade(label="Ayuda", menu=ayudamenu)

#####Creando etiquetas y cajas de texto####
e1= Entry(root, textvariable= miId) #sirve para guardar el valor del id para luego reutilizarlo 

l2= Label(root, text= "CI:")
l2.place(x=30,y=10)
e2= Entry(root, textvariable= miCi, width=20)
e2.place(x=140, y=10)

l3= Label(root, text= "Nombre: ")
l3.place(x=30,y=40)
e3= Entry(root, textvariable= miNombre, width=50 )
e3.place(x=140, y=40)

l4= Label(root, text= "Apellido:")
l4.place(x=30,y=70)
e4= Entry(root, textvariable= miApellido, width=50)
e4.place(x=140, y=70)

l5= Label(root, text= "Correo:")
l5.place(x=30,y=100)
e5= Entry(root, textvariable= miCorreo, width=50)
e5.place(x=140, y=100)

l5= Label(root, text= "Departamento:")
l5.place(x=30,y=130)
e5= Entry(root, textvariable= miDepartamento, width=50)
e5.place(x=140, y=130)

l5= Label(root, text= "Tarjeta:")
l5.place(x=30,y=160)
e5= Entry(root, textvariable= miTarjeta, width=50)
e5.place(x=140, y=160)

######creando botones######
b1= Button(root, text="Crear Registro", command=crearFuncionario)
b1.place(x=700, y=40)
b2= Button(root, text="Modificar Registro", command= actualizarFuncionario)
b2.place(x=700, y=80)
b3= Button(root, text="Mostrar Lista", command= mostrar)
b3.place(x=700, y=120)
b4= Button(root, text="Eliminar Registro", command= borrarFuncionario)
b4.place(x=700, y=160)

#### Boton para editar cambios
def editarFuncionario():
#     message = ''
#     try:
#         tree.item(tree.selection())['values'][0]
#     except IndexError as e:
#         message = 'Por favor selecciona un dato'
#         return
#     miNombre= tree.item(tree.selection())['text']
#     #old_price = self.tree.item(self.tree.selection())['values'][0]
    edit_wind = Toplevel()
    edit_wind.title("Ventana nueva")
    edit_wind.geometry("500x500")
b5= Button(root, text="Editar", command= editarFuncionario)
b5.place(x=700, y=200)

#ttk.Button(text = 'EDIT', command = self.edit_product).grid(row = 5, column = 1, sticky = W + E)


root.config(menu=menubar)
root.mainloop()


