#Proyecto 3 Futoshiki
#David Morales 
                               ######################
                               # Modulos importados #
                               ######################
import tkinter as tk
from functools import partial
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import webbrowser as wb
import pickle
from datetime import datetime
import time
import tkinter.font as tkfont
def mensaje(mensaje):
  messagebox.showinfo("Mensaje",mensaje)
                                      #######################
                                      #  Ventana principal  #
                                      #######################
ventana_principal = tk.Tk()
ancho_ventana = 400
alto_ventana = 60
x_ventana = ventana_principal.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana_principal.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana_principal.geometry(posicion)
ventana_principal.resizable(0,0)
ventana_principal.title("FUTOSHIKI")
mensa=tk.Label(ventana_principal,text="\t""Escoga una opcion del menú superior").grid(row=0,column=0)
menubar = tk.Menu(ventana_principal)
jugarmenu = tk.Menu(menubar,tearoff=0)
jugarmenu.add_command(label="Jugar",command = lambda:jugar())
menubar.add_cascade(label = "Jugar",menu=jugarmenu)
configurarmenu = tk.Menu(menubar,tearoff=0)
configurarmenu.add_command(label="Configurar",command = lambda:configurar())
menubar.add_cascade(label = "Configurar",menu=configurarmenu)
ayudamenu = tk.Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Ayuda",command = lambda:ayuda())
menubar.add_cascade(label = "Ayuda",menu=ayudamenu)
ventana_principal.config(menu=menubar)
fuente = tkfont.Font(family="Arial",size=30)
                                     #######################
                                     #     Opcion Jugar    #
                                     #######################
def jugar():
    ventana_jugar = crear_ventana("jugar",700,700,ventana_principal)
    partidas_facil = [((">",0,0), (">",0,2), (">",0,3),("4",1,0), ("2",1,4),("4",2,2),("<",3,3), ("4",3,4),("<",4,0), ("<",4,1))]
    partidas = escribir_datos_binary("futoshiki2021partidas.dat",partidas_facil)
    lista_partidas = leer_datos_binary("futoshiki2021partidas.dat")
    #input(lista_partidas[0][0][0])
    datos=leer_datos_binary("futoshiki2021configuración.dat")
    nivel = datos["nivel"]
    titulo_label = tk.Label(ventana_jugar,text="FUTOSHIKI",font=fuente)
    titulo_label.config(bg="red",fg="white", width=10, height=1)
    titulo_label.place(relx = 0.500,rely = 0.035,anchor = 'center')
    nivel_label = tk.Label(ventana_jugar,text="NIVEL").place(relx=0.450,rely=0.090,anchor="center")
    nivel_seleccionado = tk.Label(ventana_jugar,text=nivel).place(relx=0.520,rely=0.090,anchor="center")
    nom_jugador =tk.StringVar
    nom_jugador_label= tk.Label(ventana_jugar,text="Nombre del jugador: ").place(relx=0.100,rely=0.110,anchor="center")
    
    nom_jugador_entry= tk.Entry(ventana_jugar,textvariable=nom_jugador).place(relx=0.300,rely=0.110,anchor="center")
    """circulo1=crear_circulos(ventana_jugar,5,5,70,70,"light gray",0.980,0.250)
    
    circulo1.bind("<Button-1>",click)
    circulo2=crear_circulos(ventana_jugar,5,5,70,70,"white",0.980,0.350)
    circulo3=crear_circulos(ventana_jugar,5,5,70,70,"white",0.980,0.450)
    circulo4=crear_circulos(ventana_jugar,5,5,70,70,"white",0.980,0.550)
    circulo5=crear_circulos(ventana_jugar,5,5,70,70,"white",0.980,0.650)"""
    num1_label = tk.Button(ventana_jugar,text="1",command= lambda:colocar_numero(ventana_jugar,1,0.850,0.170)).place(relx=0.850,rely=0.170,anchor="center")
    
    num2_label = tk.Label(ventana_jugar,text="2").place(relx=0.850,rely=0.270,anchor="center")
    
    num3_label = tk.Label(ventana_jugar,text="3").place(relx=0.850,rely=0.370,anchor="center")
    
    num4_label = tk.Label(ventana_jugar,text="4").place(relx=0.850,rely=0.470,anchor="center")
    
    num5_label = tk.Label(ventana_jugar,text="5").place(relx=0.850,rely=0.570,anchor="center")
    #colocar la cuadricula##
    
    #ccc = tk.Label(ventana_jugar,text=num_seleccionado,font="arial 30 bold").place(relx=0.100,rely=0.200,anchor="center")
    cuadro_ejemplo= tk.Button(ventana_jugar,text="\n\n            ",relief=GROOVE).place(relx=0.100,rely=0.200,anchor="center")
    res1=tk.Label(ventana_jugar,text=lista_partidas[0][0][0],font="arial 30 bold").place(relx=0.150,rely=0.200,anchor="center")
    cuadro_ejemplo2= tk.Label(ventana_jugar,text="\n\n            ",relief=GROOVE).place(relx=0.200,rely=0.200,anchor="center")
    cuadro_ejemplo3= tk.Label(ventana_jugar,text="\n\n            ",relief=GROOVE).place(relx=0.300,rely=0.200,anchor="center")
    res2=tk.Label(ventana_jugar,text=lista_partidas[0][1][0],font="arial 30 bold").place(relx=0.350,rely=0.200,anchor="center")
    cuadro_ejemplo4= tk.Label(ventana_jugar,text="\n\n            ",relief=GROOVE).place(relx=0.400,rely=0.200,anchor="center")
    res3=tk.Label(ventana_jugar,text=lista_partidas[0][2][0],font="arial 30 bold").place(relx=0.450,rely=0.200,anchor="center")
    cuadro_ejemplo5= tk.Label(ventana_jugar,text="\n\n            ",relief=GROOVE).place(relx=0.500,rely=0.200,anchor="center")

    cuadro_ejemplo6= tk.Label(ventana_jugar,text="\n4\n           ",font="arial 15 bold",relief=GROOVE).place(relx=0.100,rely=0.300,anchor="center")
    cuadro_ejemplo7= tk.Label(ventana_jugar,text="\n\n            ",relief=GROOVE).place(relx=0.200,rely=0.300,anchor="center")
    cuadro_ejemplo8= tk.Label(ventana_jugar,text="\n\n            ",relief=GROOVE).place(relx=0.300,rely=0.300,anchor="center")
    cuadro_ejemplo9= tk.Label(ventana_jugar,text="\n\n            ",relief=GROOVE).place(relx=0.400,rely=0.300,anchor="center")
    cuadro_ejemplo10= tk.Label(ventana_jugar,text="\n2\n          ",font="arial 15 bold",relief=GROOVE).place(relx=0.500,rely=0.300,anchor="center")





    """c1_1=crear_cuadrados(ventana_jugar,5,5,60,60,"white",0.200,0.300)
    c1_2=crear_cuadrados(ventana_jugar,5,5,60,60,"white",0.300,0.300)
    c1_3=crear_cuadrados(ventana_jugar,5,5,60,60,"white",0.400,0.300)
    c1_4=crear_cuadrados(ventana_jugar,5,5,60,60,"white",0.500,0.300)
    c1_5=crear_cuadrados(ventana_jugar,5,5,60,60,"white",0.600,0.300)

    c2_1=crear_cuadrados(ventana_jugar,5,5,60,60,"white",0.200,0.400)
    c2_2=crear_cuadrados(ventana_jugar,5,5,60,60,"white",0.300,0.400)
    c2_3=crear_cuadrados(ventana_jugar,5,5,60,60,"white",0.400,0.400)
    c2_4=crear_cuadrados(ventana_jugar,5,5,60,60,"white",0.500,0.400)
    c2_5=crear_cuadrados(ventana_jugar,5,5,60,60,"white",0.600,0.400)"""
    
    


    #botones inferiores#
    #cuadrado1=crear_cuadrados(ventana_jugar,3,3,80,70,"red",0.200,0.750)   
    btn_iniciar_juego=tk.Button(ventana_jugar,text="INICIAR""\n""JUEGO",bg="red",activebackground="red",activeforeground="white",relief=GROOVE,cursor="hand2").place(relx=0.080,rely=0.675,anchor="center")

    #cuadrado2=crear_cuadrados(ventana_jugar,3,3,80,70,"cyan",0.400,0.750)   
    btn_borrar_jugada=tk.Button(ventana_jugar,text="BORRAR" "\n""JUGADA",bg="cyan",activebackground="cyan",relief=GROOVE,cursor="hand2").place(relx=0.280,rely=0.675,anchor="center")
    #cuadrado3=crear_cuadrados(ventana_jugar,3,3,90,70,"green",0.600,0.750)   
    btn_terminar_juego=tk.Button(ventana_jugar,text="TERMINAR""\n""JUEGO",bg="green",activebackground="green",activeforeground="white",relief=GROOVE,cursor="hand2").place(relx=0.485,rely=0.675,anchor="center")
    #cuadrado4=crear_cuadrados(ventana_jugar,3,3,80,70,"light blue",0.800,0.750)   
    btn_borrar_juego=tk.Button(ventana_jugar,text="BORRAR""\n""JUEGO",bg="light blue",activebackground="light blue",activeforeground="white",relief=GROOVE,cursor="hand2").place(relx=0.680,rely=0.675,anchor="center")
    #cuadrado5=crear_cuadrados(ventana_jugar,3,3,80,70,"yellow",0.999,0.750)   
    btn_top=tk.Button(ventana_jugar,text="TOP""\n""10",bg="yellow",activebackground="yellow",relief=GROOVE,cursor="hand2").place(relx=0.880,rely=0.675,anchor="center")
    btn_guardar_juego = tk.Button(ventana_jugar,text="GUARDAR JUEGO").place(relx=0.700,rely=0.900,anchor="center")
    btn_cargar_juego = tk.Button(ventana_jugar,text="CARGAR JUEGO").place(relx=0.900,rely=0.900,anchor="center")

    """cuadricula_tiempo_horas= crear_cuadrados(ventana_jugar,3,3,80,40,"white",0.200,0.850) 
    cuadricula_tiempo_minutos= crear_cuadrados(ventana_jugar,3,3,80,40,"white",0.295,0.850)
    cuadricula_tiempo_segundos= crear_cuadrados(ventana_jugar,3,3,80,40,"white",0.390,0.850)  
    cuadricula_tiempo_horas_num= crear_cuadrados(ventana_jugar,3,3,80,60,"white",0.200,0.900) 
    cuadricula_tiempo_minutos_num= crear_cuadrados(ventana_jugar,3,3,80,60,"white",0.295,0.900)
    cuadricula_tiempo_segundos_num= crear_cuadrados(ventana_jugar,3,3,80,60,"white",0.390,0.900)"""  

def crear_cuadrados(ventana,x0,y0,x1,y1,bg,posx,posy):
  cuadrado=tk.Canvas(ventana)
  cuadrado.create_rectangle(x0, y0, x1, y1)
  cuadrado.place(relx=posx,rely=posy,anchor="center")
  return cuadrado
def crear_circulos(ventana,x0,y0,x1,y1,bg,posx,posy):
  circulo=tk.Canvas(ventana)
  circulo.create_oval(x0, y0, x1, y1)
  circulo.place(relx=posx,rely=posy,anchor="center")
  return circulo
def click():
  mensaje("1")
def colocar_numero(ventana,numero,cordx,cordy):
  tk.Button(ventana,text="1",bg="green",command= lambda:colocar_numero(1,0.850,0.170)).place(relx=cordx,rely=cordy,anchor="center")
  
  return numero



                                     ############################
                                     #     Opcion Configurar    #
                                     ############################
def configurar():

  ventana_configurar= crear_ventana("Configurar",500,500,ventana_principal)
  configuracion_datos = open("futoshiki2021configuración.dat","wb")#CREA EL DAT DE CONFIGURARCION
  configuracion = {"nivel":"facil","reloj":"si","posicion":"derecha"}
  pickle.dump(configuracion,configuracion_datos)
  configuracion_datos.close()
  #NIVEL
  nivel_label = tk.Label(ventana_configurar,text="1.  Nivel: ").place(relx=0.100,rely=0.050,anchor="center")
  facil_btn = tk.Checkbutton(ventana_configurar,text="Facil",command=lambda:guardar_nivel("facil")).place(relx=0.200,rely=0.100,anchor="center")
  intermedio_btn = tk.Checkbutton(ventana_configurar,text="Intermedio",command=lambda:guardar_nivel("intermedio")).place(relx=0.240,rely=0.150,anchor="center")
  dificil_btn = tk.Checkbutton(ventana_configurar,text="Dificil",command=lambda:guardar_nivel("Dificil")).place(relx=0.210,rely=0.200,anchor="center")
  
  #RELOJ
  reloj_label= tk.Label(ventana_configurar,text="2.  Reloj: ").place(relx=0.100,rely=0.300,anchor="center")
  si_reloj_btn = tk.Checkbutton(ventana_configurar,text="Si",command=lambda:guardar_reloj("Si")).place(relx=0.200,rely=0.350,anchor="center")
  no_reloj_btn = tk.Checkbutton(ventana_configurar,text="No",command=lambda:guardar_reloj("No")).place(relx=0.205,rely=0.400,anchor="center")
  timer_btn = tk.Checkbutton(ventana_configurar,text="Timer").place(relx=0.220,rely=0.450,anchor="center")
  timer_horas = tk.IntVar()
  timer_horas_label = tk.Label(ventana_configurar,text="Horas").place(relx=0.500,rely=0.350,anchor="center")
  timer_horas_entry = tk.Entry(ventana_configurar,textvariable=timer_horas,width=1).place(relx=0.500,rely=0.400,anchor="center")
  timer_minutos = tk.IntVar()
  timer_minutos_label = tk.Label(ventana_configurar,text="Minutos").place(relx=0.600,rely=0.350,anchor="center")
  timer_minutos_entry = tk.Entry(ventana_configurar,textvariable=timer_minutos,width=2).place(relx=0.600,rely=0.400,anchor="center")
  timer_segundos = tk.IntVar()
  timer_segundos_label = tk.Label(ventana_configurar,text="Segundos").place(relx=0.720,rely=0.350,anchor="center")
  timer_segundos_entry = tk.Entry(ventana_configurar,textvariable=timer_segundos,width=2).place(relx=0.720,rely=0.400,anchor="center")
                                                      ########################################
                                                      #realizar validaciones con las entradas#
                                                      ########################################
  #POSICION
  posicion_label= tk.Label(ventana_configurar,text="3.  Posición en la ventana del panel de digitos: ").place(relx=0.330,rely=0.500,anchor="center")
  derecha_btn = tk.Checkbutton(ventana_configurar,text="Derecha",command=lambda:guardar_posicion("derecha")).place(relx=0.700,rely=0.500,anchor="center")
  izquierda_btn = tk.Checkbutton(ventana_configurar,text="Izquierda",command=lambda:guardar_posicion("izquierda")).place(relx=0.700,rely=0.550,anchor="center")
  
  def guardar_nivel(nivel):
    configuracion_datos = leer_datos_binary("futoshiki2021configuración.dat")
    configuracion_datos["nivel"]= nivel
    configuracion=escribir_datos_binary("futoshiki2021configuración.dat",configuracion_datos)
    print(configuracion)
  def guardar_reloj(reloj_opcion):
    configuracion_datos = leer_datos_binary("futoshiki2021configuración.dat")
    configuracion_datos["reloj"]=reloj_opcion
    configuracion = escribir_datos_binary("futoshiki2021configuración.dat",configuracion_datos)
    print(configuracion)
  def guardar_posicion(posicion):
    configuracion_datos = leer_datos_binary("futoshiki2021configuración.dat")
    configuracion_datos["posicion"]= posicion
    configuracion=escribir_datos_binary("futoshiki2021configuración.dat",configuracion_datos)
    print(configuracion)
  
  #zona para guardar las partidas predeterminadas 
  def partidas():
    partidas_facil = [((">", 0,0), (">", 0,2), (">", 0,3),("4", 1,0), ("2", 1,4),("4", 2,2),("<", 3,3), ("4", 3,4),("<", 4,0), ("<", 4,1))]
    partidas = escribir_datos_binary("futoshiki2021partidas.dat",partidas_facil)
    
    

  
    
                                    


def ayuda():
  wb.open_new(r"manual_de_usuario_futoshiki.pdf")
                               ###############################
                               # Funcion para crear ventanas #
                               ###############################     
def crear_ventana(ventana_title,ancho_ventana,alto_ventana,ventana_anterior):
  ventana_actual = tk.Toplevel(ventana_anterior)
  ancho_ventana = ancho_ventana
  alto_ventana = alto_ventana
  x_ventana = ventana_actual.winfo_screenwidth() // 2 - ancho_ventana // 2
  y_ventana = ventana_actual.winfo_screenheight() // 2 - alto_ventana // 2
  posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
  ventana_anterior.state(newstate="withdraw") # esconde la ventana
  ventana_actual.state(newstate="normal") # muestra la ventana
  ventana_actual.geometry(posicion)
  ventana_actual.resizable(0,0)
  ventana_actual.title(ventana_title)
  ventana_actual.protocol("WM_DELETE_WINDOW",lambda:ventana_actual.state(newstate="withdraw")+ventana_anterior.state(newstate="normal"))
         ######################################################
         # Hace que el menu se vea en cada ventana en windows #
         ###################################################### 
  menubar = tk.Menu(ventana_actual)
  jugarmenu = tk.Menu(menubar,tearoff=0)
  jugarmenu.add_command(label="Jugar",command = lambda:jugar())
  menubar.add_cascade(label = "Jugar",menu=jugarmenu)
  configurarmenu = tk.Menu(menubar,tearoff=0)
  configurarmenu.add_command(label="Configurar",command = lambda:configurar())
  menubar.add_cascade(label = "Configurar",menu=configurarmenu)
  ayudamenu = tk.Menu(menubar,tearoff=0)
  ayudamenu.add_command(label="Ayuda",command = lambda:ayuda())
  menubar.add_cascade(label = "Ayuda",menu=ayudamenu)
  ventana_actual.config(menu=menubar)
  return ventana_actual

def leer_datos_binary(nombre):
  datos=open(nombre,"rb")
  datos_list=pickle.load(datos)
  datos.close()
  return datos_list
def escribir_datos_binary(nombre,configuracion):
  datos=open(nombre,"wb")
  pickle.dump(configuracion,datos)
  datos.close()
  return configuracion
  


ventana_principal.mainloop()