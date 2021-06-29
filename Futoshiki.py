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
from datetime import date, datetime
import time
import tkinter.font as tkfont
import random as rm
class Jugar:
    ventana_jugar = ""
    nom_jugador = ""
    btn_num1 = ""
    btn_num2 = ""
    btn_num3 = ""
    btn_num4 = ""
    btn_num5 = ""
    num_seleccionado = ""
    lista_partidas = {}
    partida = {}
    jugadas = []
    bandera = False
    bandera_timer = False
    sec = ""
    min = ""
    hrs = "" 
    hora_inicio = ""
    hora_finalizacion = ""
 
    def __init__(self):
        self.btn_num1 = ""
        self.btn_num2 = ""
        self.btn_num3 = ""
        self.btn_num4 = ""
        self.btn_num5 = ""
        self.res0 = tk.Label()
        self.res1= tk.Label()
        self.res2= tk.Label()
        self.res3= tk.Label()
        self.res4= tk.Label()
        self.res5= tk.Label()
        self.res6= tk.Label()
        self.res7= tk.Label()
        self.res8= tk.Label()
        self.res9= tk.Label()
        self.res10= tk.Label()
        self.res_ver0 = tk.Label()
        self.res_ver2 = tk.Label()
        self.res_ver3 = tk.Label()
        self.res_ver4 = tk.Label()
        self.res_ver6 = tk.Label()
        self.res_ver7 = tk.Label()
        self.res_ver8 = tk.Label()
        self.res_ver9 = tk.Label()
        self.bandera = False
        self.num_seleccionado = ""
 #funcion que selecciona y deselecciona los digitos
    def toggle(self,num):
        self.num_seleccionado= num
        if self.btn_num1.config('relief')[-1] != 'sunken' and num ==1:
           self.btn_num1.config(relief="sunken",bg="green")
           self.btn_num2.config(relief="raised",bg="#f0f0ed")
           self.btn_num3.config(relief="raised",bg="#f0f0ed")
           self.btn_num4.config(relief="raised",bg="#f0f0ed")
           self.btn_num5.config(relief="raised",bg="#f0f0ed")
        elif self.btn_num2.config('relief')[-1] != 'sunken' and num ==2:
           self.btn_num1.config(relief="raised",bg="#f0f0ed")
           self.btn_num2.config(relief="sunken",bg="green")
           self.btn_num3.config(relief="raised",bg="#f0f0ed")
           self.btn_num4.config(relief="raised",bg="#f0f0ed")
           self.btn_num5.config(relief="raised",bg="#f0f0ed")
        elif self.btn_num3.config('relief')[-1] != 'sunken' and num ==3:
           self.btn_num1.config(relief="raised",bg="#f0f0ed")
           self.btn_num2.config(relief="raised",bg="#f0f0ed")
           self.btn_num3.config(relief="sunken",bg="green")
           self.btn_num4.config(relief="raised",bg="#f0f0ed")
           self.btn_num5.config(relief="raised",bg="#f0f0ed")
        elif self.btn_num4.config('relief')[-1] != 'sunken' and num ==4:
           self.btn_num1.config(relief="raised",bg="#f0f0ed")
           self.btn_num2.config(relief="raised",bg="#f0f0ed")
           self.btn_num3.config(relief="raised",bg="#f0f0ed")
           self.btn_num4.config(relief="sunken",bg="green")
           self.btn_num5.config(relief="raised",bg="#f0f0ed")
        elif self.btn_num5.config('relief')[-1] != 'sunken' and num ==5:
           self.btn_num1.config(relief="raised",bg="#f0f0ed")
           self.btn_num2.config(relief="raised",bg="#f0f0ed")
           self.btn_num3.config(relief="raised",bg="#f0f0ed")
           self.btn_num4.config(relief="raised",bg="#f0f0ed")
           self.btn_num5.config(relief="sunken",bg="green")
 #Funcion para borrar la ultima jugada
    def borrar_jugada(self):
        try:
            borrado = self.jugadas.pop()
            borrado.config(text="")
            print(self.jugadas)
        except IndexError:
            mensaje("NO HAY MAS JUGADAS PARA ELIMINAR")
 #Funcion para agregar la jugada 
    def agregar_jugada(self,btn):
        self.jugadas.append(btn)
        print(self.jugadas)
#Ventana Jugar
    def jugar(self):
        self.bandera= False
        self.num_partida = rm.randint(0,2)
        self.ventana_jugar = Creadores.crear_ventana("JUGAR",700,700,ventana_principal)
        """partidas_facil = [((">",0,0), (">",0,2), (">",0,3),("4",1,0), ("2",1,4),("4",2,2),("<",3,3), ("4",3,4),("<",4,0), ("<",4,1)),\
                         (("˅",1,0), (">",2,1), ("˄",2,1),("3",3,1), (">",3,1),("<",3,3),("4",4,0), (">",4,0),("2",4,4)),\
                         (("4",0,0), (">",0,3), ("˅",0,0),("˅",0,2), (">",1,0),(">",1,3),("˅",1,4), ("<",3,1),(">",3,3), (">",4,0))],\

                         [((">",0,0),("<",1,3),("˄",1,4),("<",2,1),("˄",2,4),(">",3,3),("˅",3,4),(">",4.0),("<",4,3)),\
                         ((">",0,0),("<",0,3),("4",0,4),("˄",0,4),(">",1,0),("<",2,1),(">",3,2),("˅",3,3),(">",4,3)),\
                         ((">",0,2),("<",0,3),("˄",0,0),(">",1,0),("2",2,2),("˄",3,1),("˅",3,3),("<",4,0),("3",4,1),(">",4,3))],\

                         [((">",0,0),("˄",0,1),("˄",0,3),("3",1,2),("˅",1,0),("<",2,2),("2",3,0),("˄",3,0),(">",4,1),("<",4,2),("3",4,4)),\
                         ((">",0,0),("3",0,1),(">",0,2),("<",2,1),("4",2,3),("˅",2,1),(">",3,3),("˅",3,0),(">",4,1),("2",4,4)),\
                         (("4",0,0),(">",0,2),(">",0,3),("˅",0,0),("2",2,2),(">",2,3),("3",3,1),("<",3,3),("˅",3,1),("˄",3,4),(">",4,1))]
        partidas = Creadores.escribir_datos_binary("futoshiki2021partidas.dat",partidas_facil)"""
        self.lista_partidas = Creadores.leer_datos_binary("futoshiki2021partidas.dat")
        #input(self.lista_partidas[self.num_partida])
        datos=Creadores.leer_datos_binary("futoshiki2021configuración.dat")
        self.nivel = datos["nivel"]
        titulo_label = tk.Label(self.ventana_jugar,text="FUTOSHIKI",font=fuente)
        titulo_label.config(bg="red",fg="white", width=10, height=1)
        titulo_label.place(relx = 0.500,rely = 0.035,anchor = 'center')
        nivel_label = tk.Label(self.ventana_jugar,text="NIVEL").place(relx=0.450,rely=0.090,anchor="center")
        self.nivel_seleccionado = tk.Label(self.ventana_jugar,text=self.nivel)
        self.nivel_seleccionado.place(relx=0.520,rely=0.090,anchor="center")
        self.nom_jugador =tk.StringVar()
        nom_jugador_label= tk.Label(self.ventana_jugar,text="Nombre del jugador: ").place(relx=0.100,rely=0.110,anchor="center")
        self.nom_jugador_entry= tk.Entry(self.ventana_jugar,textvariable=self.nom_jugador)
        self.nom_jugador_entry.bind("<Return>")#esto permite que al darle enter despues de ingresar el nombre lo guarde
        self.nom_jugador_entry.place(relx=0.300,rely=0.110,anchor="center")
        self.btn_num1= tk.Button(self.ventana_jugar,text="1",relief="raised",width=4,height=2,command=lambda:self.toggle(1))
        self.btn_num1.place(relx=0.850,rely=0.170,anchor="center")
        self.btn_num2= tk.Button(self.ventana_jugar,text="2",relief="raised",width=4,height=2,command=lambda:self.toggle(2))
        self.btn_num2.place(relx=0.850,rely=0.270,anchor="center")
        self.btn_num3 = tk.Button(self.ventana_jugar,text="3",relief="raised",width=4,height=2,command=lambda:self.toggle(3))
        self.btn_num3.place(relx=0.850,rely=0.370,anchor="center")
        self.btn_num4 = tk.Button(self.ventana_jugar,text="4",relief="raised",width=4,height=2,command=lambda:self.toggle(4))
        self.btn_num4.place(relx=0.850,rely=0.470,anchor="center")
        self.btn_num5 = tk.Button(self.ventana_jugar,text="5",relief="raised",width=4,height=2,command=lambda:self.toggle(5))
        self.btn_num5.place(relx=0.850,rely=0.570,anchor="center")
        #botones inferiores#
        #cuadrado1=crear_cuadrados(self.ventana_jugar,3,3,80,70,"red",0.200,0.750)   
        self.btn_iniciar_juego =tk.Button(self.ventana_jugar,text="INICIAR""\n""JUEGO",bg="red",activebackground="red",activeforeground="white",relief=GROOVE,cursor="hand2",command=lambda:(self.cuadricula(),self.activar_botones(),self.timer(),self.reloj()))
        self.btn_iniciar_juego.place(relx=0.080,rely=0.675,anchor="center")
        #cuadrado2=crear_cuadrados(self.ventana_jugar,3,3,80,70,"cyan",0.400,0.750)   
        self.btn_borrar_jugada=tk.Button(self.ventana_jugar,text="BORRAR" "\n""JUGADA",bg="cyan",activebackground="cyan",relief=GROOVE,cursor="hand2",state=DISABLED,command=lambda:self.borrar_jugada())
        self.btn_borrar_jugada.place(relx=0.280,rely=0.675,anchor="center")
        #cuadrado3=crear_cuadrados(self.ventana_jugar,3,3,90,70,"green",0.600,0.750)   
        self.btn_terminar_juego=tk.Button(self.ventana_jugar,text="TERMINAR""\n""JUEGO",bg="light green",activebackground="green",activeforeground="white",relief=GROOVE,cursor="hand2",state=DISABLED,command = lambda:self.pantalla_terminar_juego())
        self.btn_terminar_juego.place(relx=0.485,rely=0.675,anchor="center")
        #cuadrado4=crear_cuadrados(self.ventana_jugar,3,3,80,70,"light blue",0.800,0.750)   
        self.btn_borrar_juego=tk.Button(self.ventana_jugar,text="BORRAR""\n""JUEGO",bg="light blue",activebackground="light blue",activeforeground="white",relief=GROOVE,cursor="hand2",state=DISABLED,command= lambda:self.pantalla_borrar_juego())
        self.btn_borrar_juego.place(relx=0.680,rely=0.675,anchor="center")
        #cuadrado5=crear_cuadrados(self.ventana_jugar,3,3,80,70,"yellow",0.999,0.750) 
        btn_top=tk.Button(self.ventana_jugar,text="TOP""\n""10",bg="yellow",activebackground="yellow",relief="raised",cursor="hand2",command= lambda:self.top_10()).place(relx=0.880,rely=0.675,anchor="center")
        self.btn_guardar_juego = tk.Button(self.ventana_jugar,text="GUARDAR JUEGO",state=DISABLED,command=lambda:self.guardar_juego())
        self.btn_guardar_juego.place(relx=0.700,rely=0.900,anchor="center")
        self.btn_cargar_juego = tk.Button(self.ventana_jugar,text="CARGAR JUEGO",state=NORMAL,command=lambda:self.cargar_juego())
        self.btn_cargar_juego.place(relx=0.900,rely=0.900,anchor="center")
        
#Funcion para agregar el numero al cuadro respectivo, aqui mismo se hacen las validaciones correspondientes
    def num_seleccionador(self,btn):
        
        if self.num_seleccionado !="": 
            self.agregar_jugada(btn)
            btn.config(text=self.num_seleccionado)
            if self.cuadro_1_1.cget("text") and self.cuadro_1_2.cget("text") and self.cuadro_1_3.cget("text") and self.cuadro_1_4.cget("text") and self.cuadro_1_5.cget("text")\
            and self.cuadro_2_1.cget("text") and self.cuadro_2_2.cget("text") and self.cuadro_2_3.cget("text") and self.cuadro_2_4.cget("text") and self.cuadro_2_5.cget("text")\
            and self.cuadro_3_1.cget("text")  and self.cuadro_3_2.cget("text") and self.cuadro_3_3.cget("text") and self.cuadro_3_4.cget("text") and self.cuadro_3_5.cget("text")\
            and self.cuadro_4_1.cget("text") and self.cuadro_4_2.cget("text") and self.cuadro_4_3.cget("text") and self.cuadro_4_4.cget("text") and self.cuadro_4_5.cget("text")\
            and self.cuadro_5_1.cget("text") and self.cuadro_5_2.cget("text") and self.cuadro_5_3.cget("text") and self.cuadro_5_4.cget("text") and self.cuadro_5_5.cget("text") != "":
                self.hora_finalizacion = time.strftime("%H:%M:%S")
                
                mensaje("FELICITACIONES JUEGO TERMINADO CON EXITO")
        
            if self.nivel == "facil":
                if self.num_partida == 0:
                    if self.cuadro_1_1.cget("text") != "" and self.cuadro_1_2.cget("text") != "" :
                        if int(self.cuadro_1_1.cget("text")) < int(self.cuadro_1_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_3.cget("text") != "" and self.cuadro_1_4.cget("text") != "" :
                        if int(self.cuadro_1_3.cget("text")) < int(self.cuadro_1_4.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_4.cget("text") != "" and self.cuadro_1_5.cget("text") != "" :
                        if int(self.cuadro_1_4.cget("text")) < int(self.cuadro_1_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_4.cget("text") != "" and self.cuadro_4_5.cget("text") != "" :
                        if int(self.cuadro_4_4.cget("text")) > int(self.cuadro_4_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_4.cget("text") != "" and self.cuadro_5_5.cget("text") != "" :
                        if int(self.cuadro_5_4.cget("text")) < int(self.cuadro_5_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                if self.num_partida == 2:
                    if self.cuadro_1_1.cget("text") != "" and self.cuadro_2_1.cget("text") != "" :
                        if int(self.cuadro_1_1.cget("text")) < int(self.cuadro_2_1.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_4.cget("text") != "" and self.cuadro_1_5.cget("text") != "" :
                        if int(self.cuadro_1_4.cget("text")) < int(self.cuadro_1_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_2_1.cget("text") != "" and self.cuadro_2_2.cget("text") != "" :
                        if int(self.cuadro_2_1.cget("text")) < int(self.cuadro_2_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_2_4.cget("text") != "" and self.cuadro_2_5.cget("text") != "" :
                        if int(self.cuadro_2_4.cget("text")) < int(self.cuadro_2_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_5.cget("text") != "" and self.cuadro_4_5.cget("text") != "" :
                        if int(self.cuadro_3_5.cget("text")) < int(self.cuadro_4_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_2.cget("text") != "" and self.cuadro_4_3.cget("text") != "" :
                        if int(self.cuadro_4_2.cget("text")) > int(self.cuadro_4_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_4.cget("text") != "" and self.cuadro_4_5.cget("text") != "" :
                        if int(self.cuadro_4_4.cget("text")) < int(self.cuadro_4_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_1.cget("text") != "" and self.cuadro_5_2.cget("text") != "" :
                        if int(self.cuadro_5_1.cget("text")) < int(self.cuadro_5_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                if self.num_partida == 1:
                    if self.cuadro_2_1.cget("text") != "" and self.cuadro_3_1.cget("text") != "" :
                        if int(self.cuadro_2_1.cget("text")) < int(self.cuadro_3_1.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_2.cget("text") != "" and self.cuadro_3_3.cget("text") != "" :
                        if int(self.cuadro_3_2.cget("text")) < int(self.cuadro_3_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_2.cget("text") != "" and self.cuadro_4_2.cget("text") != "" :
                        if int(self.cuadro_3_2.cget("text")) < int(self.cuadro_4_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_2.cget("text") != "" and self.cuadro_4_3.cget("text") != "" :
                        if int(self.cuadro_4_2.cget("text")) < int(self.cuadro_4_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_4.cget("text") != "" and self.cuadro_4_5.cget("text") != "" :
                        if int(self.cuadro_4_4.cget("text")) > int(self.cuadro_4_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_1.cget("text") != "" and self.cuadro_5_2.cget("text") != "" :
                        if int(self.cuadro_5_1.cget("text")) < int(self.cuadro_5_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
            if self.nivel == "intermedio":
                if self.num_partida == 0:
                    if self.cuadro_1_1.cget("text") != "" and self.cuadro_1_2.cget("text") != "" :
                        if int(self.cuadro_1_1.cget("text")) <= int(self.cuadro_1_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_4.cget("text") != "" and self.cuadro_1_5.cget("text") != "" :
                        if int(self.cuadro_1_4.cget("text")) >= int(self.cuadro_1_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_2_5.cget("text") != "" and self.cuadro_3_5.cget("text") != "" :
                        if int(self.cuadro_2_5.cget("text")) >= int(self.cuadro_3_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_2.cget("text") != "" and self.cuadro_3_3.cget("text") != "" :
                        if int(self.cuadro_3_2.cget("text")) >= int(self.cuadro_3_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_5.cget("text") != "" and self.cuadro_4_5.cget("text") != "" :
                        if int(self.cuadro_3_5.cget("text")) >= int(self.cuadro_4_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_3.cget("text") != "" and self.cuadro_4_4.cget("text") != "" :
                        if int(self.cuadro_4_3.cget("text")) <= int(self.cuadro_4_4.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_5.cget("text") != "" and self.cuadro_5_5.cget("text") != "" :
                        if int(self.cuadro_4_5.cget("text")) <= int(self.cuadro_5_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_1.cget("text") != "" and self.cuadro_5_2.cget("text") != "" :
                        if int(self.cuadro_5_1.cget("text")) <= int(self.cuadro_5_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_4.cget("text") != "" and self.cuadro_5_5.cget("text") != "" :
                        if int(self.cuadro_5_4.cget("text")) >= int(self.cuadro_5_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                if self.num_partida == 1:
                    if self.cuadro_1_1.cget("text") != "" and self.cuadro_1_2.cget("text") != "" :
                        if int(self.cuadro_1_1.cget("text")) <= int(self.cuadro_1_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_4.cget("text") != "" and self.cuadro_1_5.cget("text") != "" :
                        if int(self.cuadro_1_4.cget("text")) >= int(self.cuadro_1_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_5.cget("text") != "" and self.cuadro_2_5.cget("text") != "" :
                        if int(self.cuadro_1_5.cget("text")) >= int(self.cuadro_2_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_2_1.cget("text") != "" and self.cuadro_2_2.cget("text") != "" :
                        if int(self.cuadro_2_1.cget("text")) <= int(self.cuadro_2_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_2.cget("text") != "" and self.cuadro_3_3.cget("text") != "" :
                        if int(self.cuadro_3_2.cget("text")) >= int(self.cuadro_3_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_2.cget("text") != "" and self.cuadro_4_3.cget("text") != "" :
                        if int(self.cuadro_4_2.cget("text")) <= int(self.cuadro_4_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_3.cget("text") != "" and self.cuadro_5_3.cget("text") != "" :
                        if int(self.cuadro_4_3.cget("text")) <= int(self.cuadro_5_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_4.cget("text") != "" and self.cuadro_5_5.cget("text") != "" :
                        if int(self.cuadro_5_4.cget("text")) <= int(self.cuadro_5_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                if self.num_partida == 2:
                    if self.cuadro_1_1.cget("text") != "" and self.cuadro_2_1.cget("text") != "" :
                        if int(self.cuadro_1_1.cget("text")) >= int(self.cuadro_2_1.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_3.cget("text") != "" and self.cuadro_1_4.cget("text") != "" :
                        if int(self.cuadro_1_3.cget("text")) <= int(self.cuadro_1_4.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_4.cget("text") != "" and self.cuadro_1_5.cget("text") != "" :
                        if int(self.cuadro_1_4.cget("text")) >= int(self.cuadro_1_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_2_1.cget("text") != "" and self.cuadro_2_2.cget("text") != "" :
                        if int(self.cuadro_2_1.cget("text")) <= int(self.cuadro_2_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_2.cget("text") != "" and self.cuadro_5_2.cget("text") != "" :
                        if int(self.cuadro_4_2.cget("text")) >= int(self.cuadro_5_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_3.cget("text") != "" and self.cuadro_5_3.cget("text") != "" :
                        if int(self.cuadro_4_3.cget("text")) <= int(self.cuadro_5_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_1.cget("text") != "" and self.cuadro_5_2.cget("text") != "" :
                        if int(self.cuadro_5_1.cget("text")) >= int(self.cuadro_5_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_4.cget("text") != "" and self.cuadro_5_5.cget("text") != "" :
                        if int(self.cuadro_5_4.cget("text")) <= int(self.cuadro_5_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
            if self.nivel == "dificil":
                if self.num_partida == 0:
                    if self.cuadro_1_1.cget("text") != "" and self.cuadro_1_2.cget("text") != "" :
                        if int(self.cuadro_1_1.cget("text")) < int(self.cuadro_1_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_2.cget("text") != "" and self.cuadro_2_2.cget("text") != "" :
                        if int(self.cuadro_1_2.cget("text")) > int(self.cuadro_2_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_4.cget("text") != "" and self.cuadro_2_4.cget("text") != "" :
                        if int(self.cuadro_1_4.cget("text")) > int(self.cuadro_2_4.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_2_1.cget("text") != "" and self.cuadro_3_1.cget("text") != "" :
                        if int(self.cuadro_2_1.cget("text")) < int(self.cuadro_3_1.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_3.cget("text") != "" and self.cuadro_3_4.cget("text") != "" :
                        if int(self.cuadro_3_3.cget("text")) > int(self.cuadro_3_4.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_2.cget("text") != "" and self.cuadro_4_2.cget("text") != "" :
                        if int(self.cuadro_3_2.cget("text")) < int(self.cuadro_4_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_1.cget("text") != "" and self.cuadro_5_1.cget("text") != "" :
                        if int(self.cuadro_4_1.cget("text")) > int(self.cuadro_5_1.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_2.cget("text") != "" and self.cuadro_5_3.cget("text") != "" :
                        if int(self.cuadro_5_2.cget("text")) < int(self.cuadro_5_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_3.cget("text") != "" and self.cuadro_5_4.cget("text") != "" :
                        if int(self.cuadro_5_3.cget("text")) > int(self.cuadro_5_4.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                if self.num_partida == 1:
                    if self.cuadro_1_1.cget("text") != "" and self.cuadro_1_2.cget("text") != "" :
                        if int(self.cuadro_1_1.cget("text")) < int(self.cuadro_1_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_3.cget("text") != "" and self.cuadro_1_4.cget("text") != "" :
                        if int(self.cuadro_1_3.cget("text")) < int(self.cuadro_1_4.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_2.cget("text") != "" and self.cuadro_2_2.cget("text") != "" :
                        if int(self.cuadro_1_2.cget("text")) > int(self.cuadro_2_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_2.cget("text") != "" and self.cuadro_3_3.cget("text") != "" :
                        if int(self.cuadro_3_2.cget("text")) > int(self.cuadro_3_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_2.cget("text") != "" and self.cuadro_4_2.cget("text") != "" :
                        if int(self.cuadro_3_2.cget("text")) < int(self.cuadro_4_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_4.cget("text") != "" and self.cuadro_4_5.cget("text") != "" :
                        if int(self.cuadro_4_4.cget("text")) < int(self.cuadro_4_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_1.cget("text") != "" and self.cuadro_5_1.cget("text") != "" :
                        if int(self.cuadro_4_1.cget("text")) < int(self.cuadro_5_1.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_2.cget("text") != "" and self.cuadro_5_3.cget("text") != "" :
                        if int(self.cuadro_5_2.cget("text")) < int(self.cuadro_5_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                if self.num_partida == 2:
                    if self.cuadro_1_1.cget("text") != "" and self.cuadro_2_1.cget("text") != "" :
                        if int(self.cuadro_1_1.cget("text")) < int(self.cuadro_2_1.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_2.cget("text") != "" and self.cuadro_2_2.cget("text") != "" :
                        if int(self.cuadro_1_2.cget("text")) > int(self.cuadro_2_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_3.cget("text") != "" and self.cuadro_1_4.cget("text") != "" :
                        if int(self.cuadro_1_3.cget("text")) < int(self.cuadro_1_4.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_1_4.cget("text") != "" and self.cuadro_1_5.cget("text") != "" :
                        if int(self.cuadro_1_4.cget("text")) < int(self.cuadro_1_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_2.cget("text") != "" and self.cuadro_4_2.cget("text") != "" :
                        if int(self.cuadro_3_2.cget("text")) < int(self.cuadro_4_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_3_4.cget("text") != "" and self.cuadro_3_5.cget("text") != "" :
                        if int(self.cuadro_3_4.cget("text")) < int(self.cuadro_3_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_4.cget("text") != "" and self.cuadro_4_5.cget("text") != "" :
                        if int(self.cuadro_4_4.cget("text")) > int(self.cuadro_4_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_2.cget("text") != "" and self.cuadro_5_2.cget("text") != "" :
                        if int(self.cuadro_4_2.cget("text")) < int(self.cuadro_5_2.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_5_2.cget("text") != "" and self.cuadro_5_3.cget("text") != "" :
                        if int(self.cuadro_5_2.cget("text")) < int(self.cuadro_5_3.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
                    if self.cuadro_4_5.cget("text") != "" and self.cuadro_5_5.cget("text") != "" :
                        if int(self.cuadro_4_5.cget("text")) > int(self.cuadro_5_5.cget("text")):
                            btn.config(bg="red")
                            mensaje("JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
                            btn.config(bg="#f0f0ed")
                            btn.config(text="")
                            self.borrar_jugada()
        else:
            mensaje("FALTA QUE SELECCIONE UN DÍGITO")
    def timer(self):
        configuracion_datos = Creadores.leer_datos_binary("futoshiki2021configuración.dat")
        if configuracion_datos["timer"] == "si":

            #label del timer 
            horas_label = tk.Label(self.ventana_jugar,text="Horas",relief= GROOVE, bg = "#f0f0ed",height=2,width=6).place(relx=0.100,rely = 0.750,anchor = CENTER)
            minutos_label = tk.Label(self.ventana_jugar,text="Minutos",relief= GROOVE, bg = "#f0f0ed",height=2,width=8).place(relx=0.180,rely = 0.750,anchor = CENTER)
            segundos_label= tk.Label(self.ventana_jugar,text="Segundos",relief= GROOVE, bg = "#f0f0ed",height=2,width=8).place(relx=0.270,rely = 0.750,anchor = CENTER)
            
            self.sec = StringVar()
            tk.Label(self.ventana_jugar, textvariable=self.sec,relief = GROOVE,height=2,width=8).place(relx=0.270, rely=0.800,anchor=CENTER)
            self.sec.set(configuracion_datos["segundos"] )
            self.mins= StringVar()
            tk.Label(self.ventana_jugar, textvariable = self.mins,relief = GROOVE,height=2,width=8).place(relx=0.180, rely=0.800,anchor= CENTER)
            self.mins.set(configuracion_datos["minutos"])
            self.hrs= StringVar()
            tk.Label(self.ventana_jugar, textvariable = self.hrs,relief = GROOVE,height=2,width=6).place(relx = 0.100, rely=0.800,anchor= CENTER)
            self.hrs.set(configuracion_datos["horas"]) 

            secu = 30
            times = int(self.hrs.get())*3600+ int(self.mins.get())*60 + int(self.sec.get())
            while times > -1:
                minute,second = (times // 60 , times % 60)
                hour = 0
                if minute > 60:
                    hour , minute = (minute // 60 , minute % 60)
                self.sec.set(second)
                self.mins.set(minute)
                self.hrs.set(hour)
                #Update the time
                self.ventana_jugar.update()
                time.sleep(1)
                if(times == 0):
                    self.sec.set("00")
                    self.mins.set('00')
                    self.hrs.set('00')
                    mensaje("SE ACABÓ EL TIEMPO")
                times -= 1
    def reloj(self):
        configuracion_datos = Creadores.leer_datos_binary("futoshiki2021configuración.dat")
        if configuracion_datos["reloj"] == "si":
            self.hora_inicio = time.strftime("%H:%M:%S")
            print(self.hora_inicio)    
    def cuadricula(self):
        cuadros_lista = ["","","","","","","","","","","","","","","","","","","","","","","","",""]  
        if self.bandera == True:
            count = 0
            for ind in cuadros_lista:
                cuadros_lista[count] = self.partida["cuadro"+str(count)]
                count +=1   
            self.activar_botones()
        else:
            self.jugadas.clear()
        if self.nom_jugador.get() == "":
            mensaje("DIGITE SU NOMBRE PRIMERO")
            self.ventana_jugar.state(newstate="withdraw")
            ventana_principal.state(newstate="normal")
        self.btn_iniciar_juego.config(state=DISABLED)
        if self.nivel == "facil":
            if self.num_partida == 0:
                #restricciones horizontales 
                self.res0=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][0][0])
                self.res0.place(relx=0.150,rely=0.200,anchor="center")
                self.res1=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][1][0])
                self.res1.place(relx=0.350,rely=0.200,anchor="center")
                self.res2=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][2][0])
                self.res2.place(relx=0.450,rely=0.200,anchor="center")
                self.res6=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][6][0])
                self.res6.place(relx=0.450,rely=0.500,anchor="center")
                self.res8=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][8][0])
                self.res8.place(relx=0.450,rely=0.600,anchor="center")
                self.res9=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][9][0])
                self.res9.place(relx=0.450,rely=0.600,anchor="center")
                #cuadricula
                self.cuadro_1_1 = tk.Button(self.ventana_jugar,text=cuadros_lista[0],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_1) ))
                self.cuadro_1_1.place(relx=0.100,rely=0.200,anchor="center")
                self.cuadro_1_2= tk.Button(self.ventana_jugar,text=cuadros_lista[1],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_2) ))
                self.cuadro_1_2.place(relx=0.200,rely=0.200,anchor="center")
                self.cuadro_1_3= tk.Button(self.ventana_jugar,text=cuadros_lista[2],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_3)))
                self.cuadro_1_3.place(relx=0.300,rely=0.200,anchor="center")
                self.cuadro_1_4 = tk.Button(self.ventana_jugar,text=cuadros_lista[3],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_4)))
                self.cuadro_1_4.place(relx=0.400,rely=0.200,anchor="center")
                self.cuadro_1_5= tk.Button(self.ventana_jugar,text=cuadros_lista[4],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_5)))
                self.cuadro_1_5.place(relx=0.500,rely=0.200,anchor="center")

                self.cuadro_2_1= tk.Button(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][3][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_2_1)))
                self.cuadro_2_1.place(relx=0.100,rely=0.300,anchor="center")
                self.cuadro_2_2= tk.Button(self.ventana_jugar,text=cuadros_lista[6],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_2) ))
                self.cuadro_2_2.place(relx=0.200,rely=0.300,anchor="center")
                self.cuadro_2_3= tk.Button(self.ventana_jugar,text=cuadros_lista[7],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_3) ))
                self.cuadro_2_3.place(relx=0.300,rely=0.300,anchor="center")
                self.cuadro_2_4= tk.Button(self.ventana_jugar,text=cuadros_lista[8],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_4) ))
                self.cuadro_2_4.place(relx=0.400,rely=0.300,anchor="center")
                self.cuadro_2_5= tk.Button(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][4][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_2_5)))
                self.cuadro_2_5.place(relx=0.500,rely=0.300,anchor="center")

                self.cuadro_3_1= tk.Button(self.ventana_jugar,text=cuadros_lista[10],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_1) ))
                self.cuadro_3_1.place(relx=0.100,rely=0.400,anchor="center")
                self.cuadro_3_2= tk.Button(self.ventana_jugar,text=cuadros_lista[11],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_2) ))
                self.cuadro_3_2.place(relx=0.200,rely=0.400,anchor="center")
                self.cuadro_3_3= tk.Button(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][5][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_3_3)))
                self.cuadro_3_3.place(relx=0.300,rely=0.400,anchor="center")
                self.cuadro_3_4= tk.Button(self.ventana_jugar,text=cuadros_lista[13],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_4)))
                self.cuadro_3_4.place(relx=0.400,rely=0.400,anchor="center")
                self.cuadro_3_5= tk.Button(self.ventana_jugar,text=cuadros_lista[14],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_5)))
                self.cuadro_3_5.place(relx=0.500,rely=0.400,anchor="center")

                self.cuadro_4_1= tk.Button(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][3][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_4_1)))
                self.cuadro_4_1.place(relx=0.100,rely=0.500,anchor="center")
                self.cuadro_4_2= tk.Button(self.ventana_jugar,text=cuadros_lista[16],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_2)))
                self.cuadro_4_2.place(relx=0.200,rely=0.500,anchor="center")
                self.cuadro_4_3= tk.Button(self.ventana_jugar,text=cuadros_lista[17],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_3)))
                self.cuadro_4_3.place(relx=0.300,rely=0.500,anchor="center")
                self.cuadro_4_4= tk.Button(self.ventana_jugar,text=cuadros_lista[18],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_4)))
                self.cuadro_4_4.place(relx=0.400,rely=0.500,anchor="center")
                self.cuadro_4_5= tk.Button(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][7][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_4_5)))
                self.cuadro_4_5.place(relx=0.500,rely=0.500,anchor="center")

                self.cuadro_5_1= tk.Button(self.ventana_jugar,text=cuadros_lista[20],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_1)))
                self.cuadro_5_1.place(relx=0.100,rely=0.600,anchor="center")
                self.cuadro_5_2= tk.Button(self.ventana_jugar,text=cuadros_lista[21],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_2)))
                self.cuadro_5_2.place(relx=0.200,rely=0.600,anchor="center")
                self.cuadro_5_3= tk.Button(self.ventana_jugar,text=cuadros_lista[22],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_3)))
                self.cuadro_5_3.place(relx=0.300,rely=0.600,anchor="center")
                self.cuadro_5_4= tk.Button(self.ventana_jugar,text=cuadros_lista[23],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_4)))
                self.cuadro_5_4.place(relx=0.400,rely=0.600,anchor="center")
                self.cuadro_5_5= tk.Button(self.ventana_jugar,text=cuadros_lista[24],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_5)))
                self.cuadro_5_5.place(relx=0.500,rely=0.600,anchor="center")
            elif self.num_partida == 1:
                #restrcciones horizontales
                
                self.res1=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][1][0])
                self.res1.place(relx=0.250,rely=0.400,anchor="center")
                self.res4=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][4][0])
                self.res4.place(relx=0.250,rely=0.500,anchor="center")
                self.res5=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][5][0])
                self.res5.place(relx=0.450,rely=0.500,anchor="center")
                self.res7=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][7][0])
                self.res7.place(relx=0.150,rely=0.600,anchor="center")

                #restricciones verticales
                self.res_ver0=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][0][0])
                self.res_ver0.place(relx=0.100,rely=0.350,anchor="center")
                self.res_ver2=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][2][0])
                self.res_ver2.place(relx=0.200,rely=0.450,anchor="center")
                #cuadricula
                self.cuadro_1_1 = tk.Button(self.ventana_jugar,text=cuadros_lista[0],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_1) ))
                self.cuadro_1_1.place(relx=0.100,rely=0.200,anchor="center")
                self.cuadro_1_2= tk.Button(self.ventana_jugar,text=cuadros_lista[1],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_2) ))
                self.cuadro_1_2.place(relx=0.200,rely=0.200,anchor="center")
                self.cuadro_1_3= tk.Button(self.ventana_jugar,text=cuadros_lista[2],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_3) ))
                self.cuadro_1_3.place(relx=0.300,rely=0.200,anchor="center")
                self.cuadro_1_4 = tk.Button(self.ventana_jugar,text=cuadros_lista[3],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_4) ))
                self.cuadro_1_4.place(relx=0.400,rely=0.200,anchor="center")
                self.cuadro_1_5= tk.Button(self.ventana_jugar,text=cuadros_lista[4],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_5) ))
                self.cuadro_1_5.place(relx=0.500,rely=0.200,anchor="center")

                self.cuadro_2_1= tk.Button(self.ventana_jugar,text=cuadros_lista[5],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_1) ))
                self.cuadro_2_1.place(relx=0.100,rely=0.300,anchor="center")
                self.cuadro_2_2= tk.Button(self.ventana_jugar,text=cuadros_lista[6],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_2) ))
                self.cuadro_2_2.place(relx=0.200,rely=0.300,anchor="center")
                self.cuadro_2_3= tk.Button(self.ventana_jugar,text=cuadros_lista[7],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_3) ))
                self.cuadro_2_3.place(relx=0.300,rely=0.300,anchor="center")
                self.cuadro_2_4= tk.Button(self.ventana_jugar,text=cuadros_lista[8],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_4) ))
                self.cuadro_2_4.place(relx=0.400,rely=0.300,anchor="center")
                self.cuadro_2_5= tk.Button(self.ventana_jugar,text=cuadros_lista[9],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_5) ))
                self.cuadro_2_5.place(relx=0.500,rely=0.300,anchor="center")

                self.cuadro_3_1= tk.Button(self.ventana_jugar,text=cuadros_lista[10],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_1) ))
                self.cuadro_3_1.place(relx=0.100,rely=0.400,anchor="center")
                self.cuadro_3_2= tk.Button(self.ventana_jugar,text=cuadros_lista[11],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_2) ))
                self.cuadro_3_2.place(relx=0.200,rely=0.400,anchor="center")
                self.cuadro_3_3= tk.Button(self.ventana_jugar,text=cuadros_lista[12],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_3) ))
                self.cuadro_3_3.place(relx=0.300,rely=0.400,anchor="center")
                self.cuadro_3_4= tk.Button(self.ventana_jugar,text=cuadros_lista[13],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_4)))
                self.cuadro_3_4.place(relx=0.400,rely=0.400,anchor="center")
                self.cuadro_3_5= tk.Button(self.ventana_jugar,text=cuadros_lista[14],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_5)))
                self.cuadro_3_5.place(relx=0.500,rely=0.400,anchor="center")

                self.cuadro_4_1= tk.Button(self.ventana_jugar,text=cuadros_lista[15],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_1)))
                self.cuadro_4_1.place(relx=0.100,rely=0.500,anchor="center")
                self.cuadro_4_2= tk.Button(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][3][0],relief=GROOVE,width=4,height=2,command=lambda:self.numero_fijo(self.cuadro_4_2))
                self.cuadro_4_2.place(relx=0.200,rely=0.500,anchor="center")
                self.cuadro_4_3= tk.Button(self.ventana_jugar,text=cuadros_lista[17],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_3)))
                self.cuadro_4_3.place(relx=0.300,rely=0.500,anchor="center")
                self.cuadro_4_4= tk.Button(self.ventana_jugar,text=cuadros_lista[18],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_4)))
                self.cuadro_4_4.place(relx=0.400,rely=0.500,anchor="center")
                self.cuadro_4_5= tk.Button(self.ventana_jugar,text=cuadros_lista[19],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_5)))
                self.cuadro_4_5.place(relx=0.500,rely=0.500,anchor="center")

                self.cuadro_5_1= tk.Button(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][6][0],relief=GROOVE,width=4,height=2,command=lambda:self.numero_fijo(self.cuadro_5_1))
                self.cuadro_5_1.place(relx=0.100,rely=0.600,anchor="center")
                self.cuadro_5_2= tk.Button(self.ventana_jugar,text=cuadros_lista[21],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_2)))
                self.cuadro_5_2.place(relx=0.200,rely=0.600,anchor="center")
                self.cuadro_5_3= tk.Button(self.ventana_jugar,text=cuadros_lista[22],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_3)))
                self.cuadro_5_3.place(relx=0.300,rely=0.600,anchor="center")
                self.cuadro_5_4= tk.Button(self.ventana_jugar,text=cuadros_lista[23],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_4)))
                self.cuadro_5_4.place(relx=0.400,rely=0.600,anchor="center")
                self.cuadro_5_5= tk.Button(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][8][0],relief=GROOVE,width=4,height=2,command=lambda:self.numero_fijo(self.cuadro_5_5))
                self.cuadro_5_5.place(relx=0.500,rely=0.600,anchor="center")           
            elif self.num_partida == 2:
                #restricciones horizontales
                self.res1=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][1][0])
                self.res1.place(relx=0.450,rely=0.200,anchor="center")
                self.res5=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][4][0])
                self.res5.place(relx=0.150,rely=0.300,anchor="center")
                self.res6=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][5][0])
                self.res6.place(relx=0.450,rely=0.300,anchor="center")
                self.res7=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][7][0])
                self.res7.place(relx=0.250,rely=0.500,anchor="center")
                self.res8=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][8][0])
                self.res8.place(relx=0.450,rely=0.500,anchor="center")
                self.res9=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][9][0])
                self.res9.place(relx=0.150,rely=0.600,anchor="center")
                #restricciones verticales
                self.res_ver2=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][2][0])
                self.res_ver2.place(relx=0.100,rely=0.250,anchor="center")
                self.res_ver3=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][3][0])
                self.res_ver3.place(relx=0.100,rely=0.250,anchor="center")
                self.res_ver6=tk.Label(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][6][0])
                self.res_ver6.place(relx=0.500,rely=0.450,anchor="center")
                #cuadricula
                self.cuadro_1_1 = tk.Button(self.ventana_jugar,text=self.lista_partidas[0][self.num_partida][0][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_1_1)))
                self.cuadro_1_1.place(relx=0.100,rely=0.200,anchor="center")
                self.cuadro_1_2= tk.Button(self.ventana_jugar,text=cuadros_lista[1],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_2) ))
                self.cuadro_1_2.place(relx=0.200,rely=0.200,anchor="center")
                self.cuadro_1_3= tk.Button(self.ventana_jugar,text=cuadros_lista[2],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_3) ))
                self.cuadro_1_3.place(relx=0.300,rely=0.200,anchor="center")
                self.cuadro_1_4 = tk.Button(self.ventana_jugar,text=cuadros_lista[3],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_4) ))
                self.cuadro_1_4.place(relx=0.400,rely=0.200,anchor="center")
                self.cuadro_1_5= tk.Button(self.ventana_jugar,text=cuadros_lista[4],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_5) ))
                self.cuadro_1_5.place(relx=0.500,rely=0.200,anchor="center")

                self.cuadro_2_1= tk.Button(self.ventana_jugar,text=cuadros_lista[5],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_1) ))
                self.cuadro_2_1.place(relx=0.100,rely=0.300,anchor="center")
                self.cuadro_2_2= tk.Button(self.ventana_jugar,text=cuadros_lista[6],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_2) ))
                self.cuadro_2_2.place(relx=0.200,rely=0.300,anchor="center")
                self.cuadro_2_3= tk.Button(self.ventana_jugar,text=cuadros_lista[7],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_3) ))
                self.cuadro_2_3.place(relx=0.300,rely=0.300,anchor="center")
                self.cuadro_2_4= tk.Button(self.ventana_jugar,text=cuadros_lista[8],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_4) ))
                self.cuadro_2_4.place(relx=0.400,rely=0.300,anchor="center")
                self.cuadro_2_5= tk.Button(self.ventana_jugar,text=cuadros_lista[9],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_5) ))
                self.cuadro_2_5.place(relx=0.500,rely=0.300,anchor="center")

                self.cuadro_3_1= tk.Button(self.ventana_jugar,text=cuadros_lista[10],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_1) ))
                self.cuadro_3_1.place(relx=0.100,rely=0.400,anchor="center")
                self.cuadro_3_2= tk.Button(self.ventana_jugar,text=cuadros_lista[11],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_2) ))
                self.cuadro_3_2.place(relx=0.200,rely=0.400,anchor="center")
                self.cuadro_3_3= tk.Button(self.ventana_jugar,text=cuadros_lista[12],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_3) ))
                self.cuadro_3_3.place(relx=0.300,rely=0.400,anchor="center")
                self.cuadro_3_4= tk.Button(self.ventana_jugar,text=cuadros_lista[13],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_4)))
                self.cuadro_3_4.place(relx=0.400,rely=0.400,anchor="center")
                self.cuadro_3_5= tk.Button(self.ventana_jugar,text=cuadros_lista[14],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_5)))
                self.cuadro_3_5.place(relx=0.500,rely=0.400,anchor="center")

                self.cuadro_4_1= tk.Button(self.ventana_jugar,text=cuadros_lista[15],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_1)))
                self.cuadro_4_1.place(relx=0.100,rely=0.500,anchor="center")
                self.cuadro_4_2= tk.Button(self.ventana_jugar,text=cuadros_lista[16],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_2)))
                self.cuadro_4_2.place(relx=0.200,rely=0.500,anchor="center")
                self.cuadro_4_3= tk.Button(self.ventana_jugar,text=cuadros_lista[17],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_3)))
                self.cuadro_4_3.place(relx=0.300,rely=0.500,anchor="center")
                self.cuadro_4_4= tk.Button(self.ventana_jugar,text=cuadros_lista[18],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_4)))
                self.cuadro_4_4.place(relx=0.400,rely=0.500,anchor="center")
                self.cuadro_4_5= tk.Button(self.ventana_jugar,text=cuadros_lista[19],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_5)))
                self.cuadro_4_5.place(relx=0.500,rely=0.500,anchor="center")

                self.cuadro_5_1= tk.Button(self.ventana_jugar,text=cuadros_lista[20],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_1)))
                self.cuadro_5_1.place(relx=0.100,rely=0.600,anchor="center")
                self.cuadro_5_2= tk.Button(self.ventana_jugar,text=cuadros_lista[21],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_2)))
                self.cuadro_5_2.place(relx=0.200,rely=0.600,anchor="center")
                self.cuadro_5_3= tk.Button(self.ventana_jugar,text=cuadros_lista[22],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_3)))
                self.cuadro_5_3.place(relx=0.300,rely=0.600,anchor="center")
                self.cuadro_5_4= tk.Button(self.ventana_jugar,text=cuadros_lista[23],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_4)))
                self.cuadro_5_4.place(relx=0.400,rely=0.600,anchor="center")
                self.cuadro_5_5= tk.Button(self.ventana_jugar,text=cuadros_lista[24],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_5)))
                self.cuadro_5_5.place(relx=0.500,rely=0.600,anchor="center")
        elif self.nivel == "intermedio":
            if self.num_partida == 0:
                #restricciones horizontales
                self.res0=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][0][0])
                self.res0.place(relx=0.150,rely=0.200,anchor="center")
                self.res1=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][1][0])
                self.res1.place(relx=0.450,rely=0.200,anchor="center")
                self.res3=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][3][0])
                self.res3.place(relx=0.250,rely=0.400,anchor="center")
                self.res5=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][5][0])
                self.res5.place(relx=0.350,rely=0.500,anchor="center")
                self.res7=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][7][0])
                self.res7.place(relx=0.150,rely=0.600,anchor="center")
                self.res8=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][8][0])
                self.res8.place(relx=0.450,rely=0.600,anchor="center")
                #restricciones verticales
                self.res_ver2=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][2][0])
                self.res_ver2.place(relx=0.500,rely=0.350,anchor="center")
                self.res_ver4=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][4][0])
                self.res_ver4.place(relx=0.500,rely=0.450,anchor="center")
                self.res_ver6=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][6][0])
                self.res_ver6.place(relx=0.500,rely=0.550,anchor="center")
                #cuadricula
                self.cuadro_1_1 = tk.Button(self.ventana_jugar,text=cuadros_lista[0],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_1) ))
                self.cuadro_1_1.place(relx=0.100,rely=0.200,anchor="center")
                self.cuadro_1_2= tk.Button(self.ventana_jugar,text=cuadros_lista[1],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_2) ))
                self.cuadro_1_2.place(relx=0.200,rely=0.200,anchor="center")
                self.cuadro_1_3= tk.Button(self.ventana_jugar,text=cuadros_lista[2],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_3) ))
                self.cuadro_1_3.place(relx=0.300,rely=0.200,anchor="center")
                self.cuadro_1_4 = tk.Button(self.ventana_jugar,text=cuadros_lista[3],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_4) ))
                self.cuadro_1_4.place(relx=0.400,rely=0.200,anchor="center")
                self.cuadro_1_5= tk.Button(self.ventana_jugar,text=cuadros_lista[4],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_5) ))
                self.cuadro_1_5.place(relx=0.500,rely=0.200,anchor="center")

                self.cuadro_2_1= tk.Button(self.ventana_jugar,text=cuadros_lista[5],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_1) ))
                self.cuadro_2_1.place(relx=0.100,rely=0.300,anchor="center")
                self.cuadro_2_2= tk.Button(self.ventana_jugar,text=cuadros_lista[6],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_2) ))
                self.cuadro_2_2.place(relx=0.200,rely=0.300,anchor="center")
                self.cuadro_2_3= tk.Button(self.ventana_jugar,text=cuadros_lista[7],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_3) ))
                self.cuadro_2_3.place(relx=0.300,rely=0.300,anchor="center")
                self.cuadro_2_4= tk.Button(self.ventana_jugar,text=cuadros_lista[8],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_4) ))
                self.cuadro_2_4.place(relx=0.400,rely=0.300,anchor="center")
                self.cuadro_2_5= tk.Button(self.ventana_jugar,text=cuadros_lista[9],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_5) ))
                self.cuadro_2_5.place(relx=0.500,rely=0.300,anchor="center")

                self.cuadro_3_1= tk.Button(self.ventana_jugar,text=cuadros_lista[10],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_1) ))
                self.cuadro_3_1.place(relx=0.100,rely=0.400,anchor="center")
                self.cuadro_3_2= tk.Button(self.ventana_jugar,text=cuadros_lista[11],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_2) ))
                self.cuadro_3_2.place(relx=0.200,rely=0.400,anchor="center")
                self.cuadro_3_3= tk.Button(self.ventana_jugar,text=cuadros_lista[12],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_3) ))
                self.cuadro_3_3.place(relx=0.300,rely=0.400,anchor="center")
                self.cuadro_3_4= tk.Button(self.ventana_jugar,text=cuadros_lista[13],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_4)))
                self.cuadro_3_4.place(relx=0.400,rely=0.400,anchor="center")
                self.cuadro_3_5= tk.Button(self.ventana_jugar,text=cuadros_lista[14],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_5)))
                self.cuadro_3_5.place(relx=0.500,rely=0.400,anchor="center")

                self.cuadro_4_1= tk.Button(self.ventana_jugar,text=cuadros_lista[15],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_1)))
                self.cuadro_4_1.place(relx=0.100,rely=0.500,anchor="center")
                self.cuadro_4_2= tk.Button(self.ventana_jugar,text=cuadros_lista[16],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_2)))
                self.cuadro_4_2.place(relx=0.200,rely=0.500,anchor="center")
                self.cuadro_4_3= tk.Button(self.ventana_jugar,text=cuadros_lista[17],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_3)))
                self.cuadro_4_3.place(relx=0.300,rely=0.500,anchor="center")
                self.cuadro_4_4= tk.Button(self.ventana_jugar,text=cuadros_lista[18],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_4)))
                self.cuadro_4_4.place(relx=0.400,rely=0.500,anchor="center")
                self.cuadro_4_5= tk.Button(self.ventana_jugar,text=cuadros_lista[19],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_5)))
                self.cuadro_4_5.place(relx=0.500,rely=0.500,anchor="center")

                self.cuadro_5_1= tk.Button(self.ventana_jugar,text=cuadros_lista[20],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_1)))
                self.cuadro_5_1.place(relx=0.100,rely=0.600,anchor="center")
                self.cuadro_5_2= tk.Button(self.ventana_jugar,text=cuadros_lista[21],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_2)))
                self.cuadro_5_2.place(relx=0.200,rely=0.600,anchor="center")
                self.cuadro_5_3= tk.Button(self.ventana_jugar,text=cuadros_lista[22],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_3)))
                self.cuadro_5_3.place(relx=0.300,rely=0.600,anchor="center")
                self.cuadro_5_4= tk.Button(self.ventana_jugar,text=cuadros_lista[23],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_4)))
                self.cuadro_5_4.place(relx=0.400,rely=0.600,anchor="center")
                self.cuadro_5_5= tk.Button(self.ventana_jugar,text=cuadros_lista[24],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_5)))
                self.cuadro_5_5.place(relx=0.500,rely=0.600,anchor="center")
            elif self.num_partida == 1:
                 #restricciones horizontales
                self.res0=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][0][0])
                self.res0.place(relx=0.150,rely=0.200,anchor="center")
                self.res1=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][1][0])
                self.res1.place(relx=0.450,rely=0.200,anchor="center")
                self.res4=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][4][0])
                self.res4.place(relx=0.150,rely=0.300,anchor="center")
                self.res5=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][5][0])
                self.res5.place(relx=0.250,rely=0.400,anchor="center")
                self.res6=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][6][0])
                self.res6.place(relx=0.250,rely=0.500,anchor="center")  
                self.res8=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][8][0])
                self.res8.place(relx=0.450,rely=0.600,anchor="center")
                #restricciones verticales
                self.res_ver3=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][3][0])
                self.res_ver3.place(relx=0.500,rely=0.250,anchor="center")
                self.res_ver7=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][7][0])
                self.res_ver7.place(relx=0.300,rely=0.550,anchor="center")
                #cuadricula
                self.cuadro_1_1 = tk.Button(self.ventana_jugar,text=cuadros_lista[0],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_1) ))
                self.cuadro_1_1.place(relx=0.100,rely=0.200,anchor="center")
                self.cuadro_1_2= tk.Button(self.ventana_jugar,text=cuadros_lista[1],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_2) ))
                self.cuadro_1_2.place(relx=0.200,rely=0.200,anchor="center")
                self.cuadro_1_3= tk.Button(self.ventana_jugar,text=cuadros_lista[2],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_3) ))
                self.cuadro_1_3.place(relx=0.300,rely=0.200,anchor="center")
                self.cuadro_1_4 = tk.Button(self.ventana_jugar,text=cuadros_lista[3],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_4)))
                self.cuadro_1_4.place(relx=0.400,rely=0.200,anchor="center")
                self.cuadro_1_5= tk.Button(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][2][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_1_5)))
                self.cuadro_1_5.place(relx=0.500,rely=0.200,anchor="center")

                self.cuadro_2_1= tk.Button(self.ventana_jugar,text=cuadros_lista[5],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_1) ))
                self.cuadro_2_1.place(relx=0.100,rely=0.300,anchor="center")
                self.cuadro_2_2= tk.Button(self.ventana_jugar,text=cuadros_lista[6],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_2) ))
                self.cuadro_2_2.place(relx=0.200,rely=0.300,anchor="center")
                self.cuadro_2_3= tk.Button(self.ventana_jugar,text=cuadros_lista[7],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_3) ))
                self.cuadro_2_3.place(relx=0.300,rely=0.300,anchor="center")
                self.cuadro_2_4= tk.Button(self.ventana_jugar,text=cuadros_lista[8],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_4) ))
                self.cuadro_2_4.place(relx=0.400,rely=0.300,anchor="center")
                self.cuadro_2_5= tk.Button(self.ventana_jugar,text=cuadros_lista[9],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_5) ))
                self.cuadro_2_5.place(relx=0.500,rely=0.300,anchor="center")

                self.cuadro_3_1= tk.Button(self.ventana_jugar,text=cuadros_lista[10],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_1) ))
                self.cuadro_3_1.place(relx=0.100,rely=0.400,anchor="center")
                self.cuadro_3_2= tk.Button(self.ventana_jugar,text=cuadros_lista[11],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_2) ))
                self.cuadro_3_2.place(relx=0.200,rely=0.400,anchor="center")
                self.cuadro_3_3= tk.Button(self.ventana_jugar,text=cuadros_lista[12],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_3) ))
                self.cuadro_3_3.place(relx=0.300,rely=0.400,anchor="center")
                self.cuadro_3_4= tk.Button(self.ventana_jugar,text=cuadros_lista[13],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_4)))
                self.cuadro_3_4.place(relx=0.400,rely=0.400,anchor="center")
                self.cuadro_3_5= tk.Button(self.ventana_jugar,text=cuadros_lista[14],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_5)))
                self.cuadro_3_5.place(relx=0.500,rely=0.400,anchor="center")

                self.cuadro_4_1= tk.Button(self.ventana_jugar,text=cuadros_lista[15],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_1)))
                self.cuadro_4_1.place(relx=0.100,rely=0.500,anchor="center")
                self.cuadro_4_2= tk.Button(self.ventana_jugar,text=cuadros_lista[16],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_2)))
                self.cuadro_4_2.place(relx=0.200,rely=0.500,anchor="center")
                self.cuadro_4_3= tk.Button(self.ventana_jugar,text=cuadros_lista[17],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_3)))
                self.cuadro_4_3.place(relx=0.300,rely=0.500,anchor="center")
                self.cuadro_4_4= tk.Button(self.ventana_jugar,text=cuadros_lista[18],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_4)))
                self.cuadro_4_4.place(relx=0.400,rely=0.500,anchor="center")
                self.cuadro_4_5= tk.Button(self.ventana_jugar,text=cuadros_lista[19],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_5)))
                self.cuadro_4_5.place(relx=0.500,rely=0.500,anchor="center")

                self.cuadro_5_1= tk.Button(self.ventana_jugar,text=cuadros_lista[20],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_1)))
                self.cuadro_5_1.place(relx=0.100,rely=0.600,anchor="center")
                self.cuadro_5_2= tk.Button(self.ventana_jugar,text=cuadros_lista[21],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_2)))
                self.cuadro_5_2.place(relx=0.200,rely=0.600,anchor="center")
                self.cuadro_5_3= tk.Button(self.ventana_jugar,text=cuadros_lista[22],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_3)))
                self.cuadro_5_3.place(relx=0.300,rely=0.600,anchor="center")
                self.cuadro_5_4= tk.Button(self.ventana_jugar,text=cuadros_lista[23],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_4)))
                self.cuadro_5_4.place(relx=0.400,rely=0.600,anchor="center")
                self.cuadro_5_5= tk.Button(self.ventana_jugar,text=cuadros_lista[24],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_5)))
                self.cuadro_5_5.place(relx=0.500,rely=0.600,anchor="center")
            elif self.num_partida == 2:
                 #restricciones horizontales
                self.res0=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][0][0])
                self.res0.place(relx=0.350,rely=0.200,anchor="center")
                self.res1=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][1][0])
                self.res1.place(relx=0.450,rely=0.200,anchor="center")
                self.res3=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][3][0])
                self.res3.place(relx=0.150,rely=0.300,anchor="center")
                
                self.res7=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][7][0])
                self.res7.place(relx=0.150,rely=0.600,anchor="center")
                self.res9=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][9][0])
                self.res9.place(relx=0.450,rely=0.600,anchor="center")
                #restricciones verticales
                self.res_ver2=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][2][0])
                self.res_ver2.place(relx=0.100,rely=0.250,anchor="center")
                self.res_ver5=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][5][0])
                self.res_ver5.place(relx=0.200,rely=0.550,anchor="center")
                self.res_ver6=tk.Label(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][6][0])
                self.res_ver6.place(relx=0.300,rely=0.550,anchor="center")
                #cuadricula
                self.cuadro_1_1 = tk.Button(self.ventana_jugar,text=cuadros_lista[0],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_1) ))
                self.cuadro_1_1.place(relx=0.100,rely=0.200,anchor="center")
                self.cuadro_1_2= tk.Button(self.ventana_jugar,text=cuadros_lista[1],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_2) ))
                self.cuadro_1_2.place(relx=0.200,rely=0.200,anchor="center")
                self.cuadro_1_3= tk.Button(self.ventana_jugar,text=cuadros_lista[2],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_3) ))
                self.cuadro_1_3.place(relx=0.300,rely=0.200,anchor="center")
                self.cuadro_1_4 = tk.Button(self.ventana_jugar,text=cuadros_lista[3],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_4) ))
                self.cuadro_1_4.place(relx=0.400,rely=0.200,anchor="center")
                self.cuadro_1_5= tk.Button(self.ventana_jugar,text=cuadros_lista[4],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_5) ))
                self.cuadro_1_5.place(relx=0.500,rely=0.200,anchor="center")

                self.cuadro_2_1= tk.Button(self.ventana_jugar,text=cuadros_lista[5],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_1) ))
                self.cuadro_2_1.place(relx=0.100,rely=0.300,anchor="center")
                self.cuadro_2_2= tk.Button(self.ventana_jugar,text=cuadros_lista[6],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_2) ))
                self.cuadro_2_2.place(relx=0.200,rely=0.300,anchor="center")
                self.cuadro_2_3= tk.Button(self.ventana_jugar,text=cuadros_lista[7],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_3) ))
                self.cuadro_2_3.place(relx=0.300,rely=0.300,anchor="center")
                self.cuadro_2_4= tk.Button(self.ventana_jugar,text=cuadros_lista[8],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_4) ))
                self.cuadro_2_4.place(relx=0.400,rely=0.300,anchor="center")
                self.cuadro_2_5= tk.Button(self.ventana_jugar,text=cuadros_lista[9],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_5) ))
                self.cuadro_2_5.place(relx=0.500,rely=0.300,anchor="center")

                self.cuadro_3_1= tk.Button(self.ventana_jugar,text=cuadros_lista[10],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_1) ))
                self.cuadro_3_1.place(relx=0.100,rely=0.400,anchor="center")
                self.cuadro_3_2= tk.Button(self.ventana_jugar,text=cuadros_lista[11],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_2) ))
                self.cuadro_3_2.place(relx=0.200,rely=0.400,anchor="center")
                self.cuadro_3_3= tk.Button(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][4][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_3_3)))
                self.cuadro_3_3.place(relx=0.300,rely=0.400,anchor="center")
                self.cuadro_3_4= tk.Button(self.ventana_jugar,text=cuadros_lista[13],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_4)))
                self.cuadro_3_4.place(relx=0.400,rely=0.400,anchor="center")
                self.cuadro_3_5= tk.Button(self.ventana_jugar,text=cuadros_lista[14],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_5)))
                self.cuadro_3_5.place(relx=0.500,rely=0.400,anchor="center")

                self.cuadro_4_1= tk.Button(self.ventana_jugar,text=cuadros_lista[15],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_1)))
                self.cuadro_4_1.place(relx=0.100,rely=0.500,anchor="center")
                self.cuadro_4_2= tk.Button(self.ventana_jugar,text=cuadros_lista[16],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_2)))
                self.cuadro_4_2.place(relx=0.200,rely=0.500,anchor="center")
                self.cuadro_4_3= tk.Button(self.ventana_jugar,text=cuadros_lista[17],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_3)))
                self.cuadro_4_3.place(relx=0.300,rely=0.500,anchor="center")
                self.cuadro_4_4= tk.Button(self.ventana_jugar,text=cuadros_lista[18],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_4)))
                self.cuadro_4_4.place(relx=0.400,rely=0.500,anchor="center")
                self.cuadro_4_5= tk.Button(self.ventana_jugar,text=cuadros_lista[19],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_5)))
                self.cuadro_4_5.place(relx=0.500,rely=0.500,anchor="center")

                self.cuadro_5_1= tk.Button(self.ventana_jugar,text=cuadros_lista[20],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_1)))
                self.cuadro_5_1.place(relx=0.100,rely=0.600,anchor="center")
                self.cuadro_5_2= tk.Button(self.ventana_jugar,text=self.lista_partidas[1][self.num_partida][8][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_5_3)))
                self.cuadro_5_2.place(relx=0.200,rely=0.600,anchor="center")
                self.cuadro_5_3= tk.Button(self.ventana_jugar,text=cuadros_lista[22],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_3)))
                self.cuadro_5_3.place(relx=0.300,rely=0.600,anchor="center")
                self.cuadro_5_4= tk.Button(self.ventana_jugar,text=cuadros_lista[23],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_4)))
                self.cuadro_5_4.place(relx=0.400,rely=0.600,anchor="center")
                self.cuadro_5_5= tk.Button(self.ventana_jugar,text=cuadros_lista[24],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_5)))
                self.cuadro_5_5.place(relx=0.500,rely=0.600,anchor="center")
        elif self.nivel == "dificil":
            if self.num_partida == 0:
                 #restricciones horizontales
                self.res0=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][0][0])
                self.res0.place(relx=0.150,rely=0.200,anchor="center")
                
                self.res5=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][5][0])
                self.res5.place(relx=0.350,rely=0.400,anchor="center")
                self.res8=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][8][0])
                self.res8.place(relx=0.250,rely=0.600,anchor="center")
                
                self.res9=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][9][0])
                self.res9.place(relx=0.350,rely=0.600,anchor="center")
                #restricciones verticales
                self.res_ver1=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][1][0])
                self.res_ver1.place(relx=0.200,rely=0.250,anchor="center")
                self.res_ver2=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][2][0])
                self.res_ver2.place(relx=0.400,rely=0.250,anchor="center")
                self.res_ver4=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][4][0])
                self.res_ver4.place(relx=0.100,rely=0.350,anchor="center")
                self.res_ver7=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][7][0])
                self.res_ver7.place(relx=0.100,rely=0.550,anchor="center")
                #cuadricula
                self.cuadro_1_1 = tk.Button(self.ventana_jugar,text=cuadros_lista[0],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_1) ))
                self.cuadro_1_1.place(relx=0.100,rely=0.200,anchor="center")
                self.cuadro_1_2= tk.Button(self.ventana_jugar,text=cuadros_lista[1],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_2) ))
                self.cuadro_1_2.place(relx=0.200,rely=0.200,anchor="center")
                self.cuadro_1_3= tk.Button(self.ventana_jugar,text=cuadros_lista[2],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_3) ))
                self.cuadro_1_3.place(relx=0.300,rely=0.200,anchor="center")
                self.cuadro_1_4 = tk.Button(self.ventana_jugar,text=cuadros_lista[3],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_4) ))
                self.cuadro_1_4.place(relx=0.400,rely=0.200,anchor="center")
                self.cuadro_1_5= tk.Button(self.ventana_jugar,text=cuadros_lista[4],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_5) ))
                self.cuadro_1_5.place(relx=0.500,rely=0.200,anchor="center")

                self.cuadro_2_1= tk.Button(self.ventana_jugar,text=cuadros_lista[5],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_1) ))
                self.cuadro_2_1.place(relx=0.100,rely=0.300,anchor="center")
                self.cuadro_2_2= tk.Button(self.ventana_jugar,text=cuadros_lista[6],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_2) ))
                self.cuadro_2_2.place(relx=0.200,rely=0.300,anchor="center")
                self.cuadro_2_3= tk.Button(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][3][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_2_3)))
                self.cuadro_2_3.place(relx=0.300,rely=0.300,anchor="center")
                self.cuadro_2_4= tk.Button(self.ventana_jugar,text=cuadros_lista[8],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_4) ))
                self.cuadro_2_4.place(relx=0.400,rely=0.300,anchor="center")
                self.cuadro_2_5= tk.Button(self.ventana_jugar,text=cuadros_lista[9],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_5) ))
                self.cuadro_2_5.place(relx=0.500,rely=0.300,anchor="center")

                self.cuadro_3_1= tk.Button(self.ventana_jugar,text=cuadros_lista[10],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_1) ))
                self.cuadro_3_1.place(relx=0.100,rely=0.400,anchor="center")
                self.cuadro_3_2= tk.Button(self.ventana_jugar,text=cuadros_lista[11],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_2) ))
                self.cuadro_3_2.place(relx=0.200,rely=0.400,anchor="center")
                self.cuadro_3_3= tk.Button(self.ventana_jugar,text=cuadros_lista[12],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_3) ))
                self.cuadro_3_3.place(relx=0.300,rely=0.400,anchor="center")
                self.cuadro_3_4= tk.Button(self.ventana_jugar,text=cuadros_lista[13],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_4)))
                self.cuadro_3_4.place(relx=0.400,rely=0.400,anchor="center")
                self.cuadro_3_5= tk.Button(self.ventana_jugar,text=cuadros_lista[14],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_5)))
                self.cuadro_3_5.place(relx=0.500,rely=0.400,anchor="center")

                self.cuadro_4_1= tk.Button(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][6][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_4_1)))
                self.cuadro_4_1.place(relx=0.100,rely=0.500,anchor="center")
                self.cuadro_4_2= tk.Button(self.ventana_jugar,text=cuadros_lista[16],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_2)))
                self.cuadro_4_2.place(relx=0.200,rely=0.500,anchor="center")
                self.cuadro_4_3= tk.Button(self.ventana_jugar,text=cuadros_lista[17],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_3)))
                self.cuadro_4_3.place(relx=0.300,rely=0.500,anchor="center")
                self.cuadro_4_4= tk.Button(self.ventana_jugar,text=cuadros_lista[18],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_4)))
                self.cuadro_4_4.place(relx=0.400,rely=0.500,anchor="center")
                self.cuadro_4_5= tk.Button(self.ventana_jugar,text=cuadros_lista[19],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_5)))
                self.cuadro_4_5.place(relx=0.500,rely=0.500,anchor="center")

                self.cuadro_5_1= tk.Button(self.ventana_jugar,text=cuadros_lista[20],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_1)))
                self.cuadro_5_1.place(relx=0.100,rely=0.600,anchor="center")
                self.cuadro_5_2= tk.Button(self.ventana_jugar,text=cuadros_lista[21],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_2)))
                self.cuadro_5_2.place(relx=0.200,rely=0.600,anchor="center")
                self.cuadro_5_3= tk.Button(self.ventana_jugar,text=cuadros_lista[22],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_3)))
                self.cuadro_5_3.place(relx=0.300,rely=0.600,anchor="center")
                self.cuadro_5_4= tk.Button(self.ventana_jugar,text=cuadros_lista[23],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_4)))
                self.cuadro_5_4.place(relx=0.400,rely=0.600,anchor="center")
                self.cuadro_5_5= tk.Button(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][10][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_5_5)))
                self.cuadro_5_5.place(relx=0.500,rely=0.600,anchor="center")
            elif self.num_partida == 1:
                 #restricciones horizontales
                self.res0=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][0][0])
                self.res0.place(relx=0.150,rely=0.200,anchor="center")
                self.res2=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][2][0])
                self.res2.place(relx=0.350,rely=0.200,anchor="center")
                self.res3=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][3][0])
                self.res3.place(relx=0.250,rely=0.400,anchor="center")
                
                self.res6=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][6][0])
                self.res6.place(relx=0.450,rely=0.500,anchor="center")
                
                self.res8=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][8][0])
                self.res8.place(relx=0.250,rely=0.600,anchor="center")
                #restricciones verticales
                self.res_ver5=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][5][0])
                self.res_ver5.place(relx=0.200,rely=0.450,anchor="center")
                self.res_ver7=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][7][0])
                self.res_ver7.place(relx=0.100,rely=0.550,anchor="center")
                #cuadricula
                self.cuadro_1_1 = tk.Button(self.ventana_jugar,text=cuadros_lista[0],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_1) ))
                self.cuadro_1_1.place(relx=0.100,rely=0.200,anchor="center")
                self.cuadro_1_2= tk.Button(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][1][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_1_2)))
                self.cuadro_1_2.place(relx=0.200,rely=0.200,anchor="center")
                self.cuadro_1_3= tk.Button(self.ventana_jugar,text=cuadros_lista[2],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_3) ))
                self.cuadro_1_3.place(relx=0.300,rely=0.200,anchor="center")
                self.cuadro_1_4 = tk.Button(self.ventana_jugar,text=cuadros_lista[3],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_4) ))
                self.cuadro_1_4.place(relx=0.400,rely=0.200,anchor="center")
                self.cuadro_1_5= tk.Button(self.ventana_jugar,text=cuadros_lista[4],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_5) ))
                self.cuadro_1_5.place(relx=0.500,rely=0.200,anchor="center")

                self.cuadro_2_1= tk.Button(self.ventana_jugar,text=cuadros_lista[5],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_1) ))
                self.cuadro_2_1.place(relx=0.100,rely=0.300,anchor="center")
                self.cuadro_2_2= tk.Button(self.ventana_jugar,text=cuadros_lista[6],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_2) ))
                self.cuadro_2_2.place(relx=0.200,rely=0.300,anchor="center")
                self.cuadro_2_3= tk.Button(self.ventana_jugar,text=cuadros_lista[7],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_3) ))
                self.cuadro_2_3.place(relx=0.300,rely=0.300,anchor="center")
                self.cuadro_2_4= tk.Button(self.ventana_jugar,text=cuadros_lista[8],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_4) ))
                self.cuadro_2_4.place(relx=0.400,rely=0.300,anchor="center")
                self.cuadro_2_5= tk.Button(self.ventana_jugar,text=cuadros_lista[9],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_5) ))
                self.cuadro_2_5.place(relx=0.500,rely=0.300,anchor="center")

                self.cuadro_3_1= tk.Button(self.ventana_jugar,text=cuadros_lista[10],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_1) ))
                self.cuadro_3_1.place(relx=0.100,rely=0.400,anchor="center")
                self.cuadro_3_2= tk.Button(self.ventana_jugar,text=cuadros_lista[11],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_2) ))
                self.cuadro_3_2.place(relx=0.200,rely=0.400,anchor="center")
                self.cuadro_3_3= tk.Button(self.ventana_jugar,text=cuadros_lista[12],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_3) ))
                self.cuadro_3_3.place(relx=0.300,rely=0.400,anchor="center")
                self.cuadro_3_4= tk.Button(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][4][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_3_4)))
                self.cuadro_3_4.place(relx=0.400,rely=0.400,anchor="center")
                self.cuadro_3_5= tk.Button(self.ventana_jugar,text=cuadros_lista[14],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_5)))
                self.cuadro_3_5.place(relx=0.500,rely=0.400,anchor="center")

                self.cuadro_4_1= tk.Button(self.ventana_jugar,text=cuadros_lista[15],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_1)))
                self.cuadro_4_1.place(relx=0.100,rely=0.500,anchor="center")
                self.cuadro_4_2= tk.Button(self.ventana_jugar,text=cuadros_lista[16],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_2)))
                self.cuadro_4_2.place(relx=0.200,rely=0.500,anchor="center")
                self.cuadro_4_3= tk.Button(self.ventana_jugar,text=cuadros_lista[17],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_3)))
                self.cuadro_4_3.place(relx=0.300,rely=0.500,anchor="center")
                self.cuadro_4_4= tk.Button(self.ventana_jugar,text=cuadros_lista[18],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_4)))
                self.cuadro_4_4.place(relx=0.400,rely=0.500,anchor="center")
                self.cuadro_4_5= tk.Button(self.ventana_jugar,text=cuadros_lista[19],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_5)))
                self.cuadro_4_5.place(relx=0.500,rely=0.500,anchor="center")

                self.cuadro_5_1= tk.Button(self.ventana_jugar,text=cuadros_lista[20],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_1)))
                self.cuadro_5_1.place(relx=0.100,rely=0.600,anchor="center")
                self.cuadro_5_2= tk.Button(self.ventana_jugar,text=cuadros_lista[21],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_2)))
                self.cuadro_5_2.place(relx=0.200,rely=0.600,anchor="center")
                self.cuadro_5_3= tk.Button(self.ventana_jugar,text=cuadros_lista[22],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_3)))
                self.cuadro_5_3.place(relx=0.300,rely=0.600,anchor="center")
                self.cuadro_5_4= tk.Button(self.ventana_jugar,text=cuadros_lista[23],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_4)))
                self.cuadro_5_4.place(relx=0.400,rely=0.600,anchor="center")
                self.cuadro_5_5= tk.Button(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][9][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_5_5)))
                self.cuadro_5_5.place(relx=0.500,rely=0.600,anchor="center")
            elif self.num_partida == 2:
                 #restricciones horizontales
                
                self.res1=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][1][0])
                self.res1.place(relx=0.350,rely=0.200,anchor="center")
                self.res2=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][2][0])
                self.res2.place(relx=0.450,rely=0.200,anchor="center")
                self.res5=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][5][0])
                self.res5.place(relx=0.450,rely=0.400,anchor="center")
                
                self.res7=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][7][0])
                self.res7.place(relx=0.450,rely=0.500,anchor="center")
                self.res10=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][10][0])
                self.res10.place(relx=0.250,rely=0.600,anchor="center")
                #restricciones verticales
                self.res_ver3=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][3][0])
                self.res_ver3.place(relx=0.100,rely=0.250,anchor="center")
                self.res_ver8=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][8][0])
                self.res_ver8.place(relx=0.200,rely=0.550,anchor="center")
                self.res_ver9=tk.Label(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][9][0])
                self.res_ver9.place(relx=0.500,rely=0.550,anchor="center")
                #cuadricula
                self.cuadro_1_1 = tk.Button(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][0][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_1_1)))
                self.cuadro_1_1.place(relx=0.100,rely=0.200,anchor="center")
                self.cuadro_1_2= tk.Button(self.ventana_jugar,text=cuadros_lista[1],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_2) ))
                self.cuadro_1_2.place(relx=0.200,rely=0.200,anchor="center")
                self.cuadro_1_3= tk.Button(self.ventana_jugar,text=cuadros_lista[2],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_3) ))
                self.cuadro_1_3.place(relx=0.300,rely=0.200,anchor="center")
                self.cuadro_1_4 = tk.Button(self.ventana_jugar,text=cuadros_lista[3],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_4) ))
                self.cuadro_1_4.place(relx=0.400,rely=0.200,anchor="center")
                self.cuadro_1_5= tk.Button(self.ventana_jugar,text=cuadros_lista[4],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_1_5) ))
                self.cuadro_1_5.place(relx=0.500,rely=0.200,anchor="center")

                self.cuadro_2_1= tk.Button(self.ventana_jugar,text=cuadros_lista[5],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_1) ))
                self.cuadro_2_1.place(relx=0.100,rely=0.300,anchor="center")
                self.cuadro_2_2= tk.Button(self.ventana_jugar,text=cuadros_lista[6],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_2) ))
                self.cuadro_2_2.place(relx=0.200,rely=0.300,anchor="center")
                self.cuadro_2_3= tk.Button(self.ventana_jugar,text=cuadros_lista[7],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_3) ))
                self.cuadro_2_3.place(relx=0.300,rely=0.300,anchor="center")
                self.cuadro_2_4= tk.Button(self.ventana_jugar,text=cuadros_lista[8],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_4) ))
                self.cuadro_2_4.place(relx=0.400,rely=0.300,anchor="center")
                self.cuadro_2_5= tk.Button(self.ventana_jugar,text=cuadros_lista[9],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_2_5) ))
                self.cuadro_2_5.place(relx=0.500,rely=0.300,anchor="center")

                self.cuadro_3_1= tk.Button(self.ventana_jugar,text=cuadros_lista[10],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_1) ))
                self.cuadro_3_1.place(relx=0.100,rely=0.400,anchor="center")
                self.cuadro_3_2= tk.Button(self.ventana_jugar,text=cuadros_lista[11],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_2) ))
                self.cuadro_3_2.place(relx=0.200,rely=0.400,anchor="center")
                self.cuadro_3_3= tk.Button(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][4][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_3_3)))
                self.cuadro_3_3.place(relx=0.300,rely=0.400,anchor="center")
                self.cuadro_3_4= tk.Button(self.ventana_jugar,text=cuadros_lista[13],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_4)))
                self.cuadro_3_4.place(relx=0.400,rely=0.400,anchor="center")
                self.cuadro_3_5= tk.Button(self.ventana_jugar,text=cuadros_lista[14],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_3_5)))
                self.cuadro_3_5.place(relx=0.500,rely=0.400,anchor="center")

                self.cuadro_4_1= tk.Button(self.ventana_jugar,text=cuadros_lista[16],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_1)))
                self.cuadro_4_1.place(relx=0.100,rely=0.500,anchor="center")
                self.cuadro_4_2= tk.Button(self.ventana_jugar,text=self.lista_partidas[2][self.num_partida][6][0],relief=GROOVE,width=4,height=2,command=lambda:(self.numero_fijo(self.cuadro_4_2)))
                self.cuadro_4_2.place(relx=0.200,rely=0.500,anchor="center")
                self.cuadro_4_3= tk.Button(self.ventana_jugar,text=cuadros_lista[17],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_3)))
                self.cuadro_4_3.place(relx=0.300,rely=0.500,anchor="center")
                self.cuadro_4_4= tk.Button(self.ventana_jugar,text=cuadros_lista[18],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_4)))
                self.cuadro_4_4.place(relx=0.400,rely=0.500,anchor="center")
                self.cuadro_4_5= tk.Button(self.ventana_jugar,text=cuadros_lista[19],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_4_5)))
                self.cuadro_4_5.place(relx=0.500,rely=0.500,anchor="center")

                self.cuadro_5_1= tk.Button(self.ventana_jugar,text=cuadros_lista[20],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_1)))
                self.cuadro_5_1.place(relx=0.100,rely=0.600,anchor="center")
                self.cuadro_5_2= tk.Button(self.ventana_jugar,text=cuadros_lista[21],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_2)))
                self.cuadro_5_2.place(relx=0.200,rely=0.600,anchor="center")
                self.cuadro_5_3= tk.Button(self.ventana_jugar,text=cuadros_lista[22],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_3)))
                self.cuadro_5_3.place(relx=0.300,rely=0.600,anchor="center")
                self.cuadro_5_4= tk.Button(self.ventana_jugar,text=cuadros_lista[23],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_4)))
                self.cuadro_5_4.place(relx=0.400,rely=0.600,anchor="center")
                self.cuadro_5_5= tk.Button(self.ventana_jugar,text=cuadros_lista[24],relief=GROOVE,width=4,height=2,command=lambda:(self.num_seleccionador(self.cuadro_5_5)))
                self.cuadro_5_5.place(relx=0.500,rely=0.600,anchor="center")
#Confirmacion de terminar el juego
    def pantalla_terminar_juego(self):
        self.ventana_escoger = Creadores.crear_ventana("Escoger",300,300,ventana_principal)
        opcion_label = tk.Label(self.ventana_escoger,text= "¿ESTÁ SEGURO DE TERMINAR EL JUEGO (SI o NO)?").place(relx= 0.500,rely=0.050,anchor="center")
        si_btn = tk.Button(self.ventana_escoger,text= "SI",command=lambda:self.terminar_juego()).place(relx=0.400,rely=0.150,anchor="center")
        no_btn = tk.Button(self.ventana_escoger,text= "NO",command=lambda:self.ventana_escoger.destroy()).place(relx=0.500,rely=0.150,anchor="center")
 #funcion para terminar el juego
    def terminar_juego(self):
        self.res0.config(text="")
        self.res1.config(text="")
        self.res2.config(text="")
        self.res3.config(text="")
        self.res4.config(text="")
        self.res5.config(text="")
        self.res6.config(text="")
        self.res7.config(text="")
        self.res8.config(text="")
        self.res9.config(text="")
        self.res10.config(text="")
        self.res_ver0.config(text="")
        self.res_ver2.config(text="")
        self.res_ver3.config(text="")
        self.res_ver4.config(text="")
        self.res_ver6.config(text="")
        self.res_ver7.config(text="")
        self.res_ver8.config(text="")
        self.res_ver9.config(text="")
        self.num_partida = rm.randint(0,2)
        self.jugadas.clear()
        self.bandera = False
        self.ventana_escoger.destroy()
        Jugar.cuadricula(self)
 #Funcion que avtica el resto de botones al iniciar el juego
    def activar_botones(self):
        self.btn_borrar_jugada.config(state=NORMAL)
        self.btn_terminar_juego.config(state=NORMAL)
        self.btn_borrar_juego.config(state=NORMAL)
        self.btn_guardar_juego.config(state=NORMAL)
        self.btn_cargar_juego.config(state=DISABLED)
 #Funcion para guardar el juego actual
    def guardar_juego(self):
        partida_actual = {"nombre":self.nom_jugador.get(),"nivel":self.nivel,"partida":self.num_partida,\
                            "cuadro0":self.cuadro_1_1.cget("text"),"cuadro1":self.cuadro_1_2.cget("text"),"cuadro2":self.cuadro_1_3.cget("text"),"cuadro3":self.cuadro_1_4.cget("text"),"cuadro4":self.cuadro_1_5.cget("text"),\
                            "cuadro5":self.cuadro_2_1.cget("text"),"cuadro6":self.cuadro_2_2.cget("text"),"cuadro7":self.cuadro_2_3.cget("text"),"cuadro8":self.cuadro_2_4.cget("text"),"cuadro9":self.cuadro_2_5.cget("text"),\
                            "cuadro10":self.cuadro_3_1.cget("text"),"cuadro11":self.cuadro_3_2.cget("text"),"cuadro12":self.cuadro_3_3.cget("text"),"cuadro13":self.cuadro_3_4.cget("text"),"cuadro14":self.cuadro_3_5.cget("text"),\
                            "cuadro15":self.cuadro_4_1.cget("text"),"cuadro16":self.cuadro_4_2.cget("text"),"cuadro17":self.cuadro_4_3.cget("text"),"cuadro18":self.cuadro_4_4.cget("text"),"cuadro19":self.cuadro_4_5.cget("text"),\
                            "cuadro20":self.cuadro_5_1.cget("text"),"cuadro21":self.cuadro_5_2.cget("text"),"cuadro22":self.cuadro_5_3.cget("text"),"cuadro23":self.cuadro_5_4.cget("text"),"cuadro24":self.cuadro_5_5.cget("text")}
        guardar_partida = Creadores.escribir_datos_binary("futoshiki2021juegoactual.dat",partida_actual)
 #Funcion para cargar el juego que esté guardado
    def cargar_juego(self):
        self.partida =Creadores.leer_datos_binary("futoshiki2021juegoactual.dat")
        self.nom_jugador.set(self.partida["nombre"])
        self.num_partida = self.partida["partida"]
        self.nivel_seleccionado.config(text=self.partida["nivel"])
        self.bandera = True
        self.cuadricula()
 #Pantalla de confirmacion de borrar juego
    def pantalla_borrar_juego(self):
        ventana_escoger = Creadores.crear_ventana("Escoger",300,300,ventana_principal)
        opcion_label = tk.Label(ventana_escoger,text= "¿ESTÁ SEGURO DE BORRAR EL JUEGO (SI o NO)?").place(relx= 0.500,rely=0.050,anchor="center")
        si_btn = tk.Button(ventana_escoger,text= "SI",command=lambda:(self.borrar_juego(),ventana_escoger.destroy())).place(relx=0.400,rely=0.150,anchor="center")
        no_btn = tk.Button(ventana_escoger,text= "NO",command=lambda:(ventana_escoger.destroy())).place(relx=0.500,rely=0.150,anchor="center")
 #Funcion para borrar juego
    def borrar_juego(self):
        self.jugadas.clear()
        self.cuadricula()
    def top_10(self):
        
        
        entrada = datetime.strptime(self.hora_inicio,"%H:%M:%S")
        salida = datetime.strptime(self.hora_finalizacion,"%H:%M:%S")
        tiempo_total = salida - entrada
        ventana_top = Creadores.crear_ventana("TOP 10",1000,500,ventana_principal)
        top_10_label= tk.Label(ventana_top,text="TOP 10").place(relx=0.500,rely=0.050,anchor=CENTER)
        top_facil_label = tk.Label(ventana_top,text="NIVEL FACIL").place(relx=0.100,rely=0.100,anchor=CENTER)
        top_intermedio_label = tk.Label(ventana_top,text="NIVEL INTERMEDIO").place(relx=0.500,rely=0.100,anchor=CENTER)
        top_dificil_label = tk.Label(ventana_top,text="NIVEL DIFICIL").place(relx=0.850,rely=0.100,anchor=CENTER)
        top_lista = [["","","","","","","","","",""],["","","","","","","","","",""],["","","","","","","","","",""]]
        top_10 = Creadores.escribir_datos_binary("futoshiki2021top10.dat",top_lista)

        if self.nivel == "facil":
            top = Creadores.leer_datos_binary("futoshiki2021top10.dat")
            """top1_facil_nombre= tk.Label(ventana_top,text=self.nom_jugador.get()).place(relx=0.050,rely=0.150,anchor=CENTER)
            top1_facil_tiempo = tk.Label(ventana_top,text=tiempo_total).place(relx=0.150,rely=0.150,anchor=CENTER)"""
            top1 = self.nom_jugador.get() + str(tiempo_total)

            top_facil = []
            top.insert(0,top1)
            """top.insert([0][2],"")
            top.insert([0][3],"")
            top.insert([0][4],"")
            top.insert([0][5],"")"""
            to = Creadores.escribir_datos_binary("futoshiki2021top10.dat",top)
            top_label = tk.Label(ventana_top,text=to[0]).place(relx=0.050,rely=0.150,anchor=CENTER)
        if self.nivel == "intermedio":
            pass
        if self.nivel == "dificil":
            pass

        #top = Creadores.escribir_datos_binary("futoshiki2021top10.dat",top_lista)
# esta funcion es la restriccion para los numeros fijos en la cuadricula
    def numero_fijo(self,btn): 
        btn.config(bg="red")
        mensaje("JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")
        btn.config(bg="#f0f0ed")    
def mensaje(mensaje):
  messagebox.showinfo("Mensaje",mensaje)
#clases que crean datos fijos
class Creadores:
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
        jugarmenu.add_command(label="Jugar",command = lambda:jugar.jugar())
        menubar.add_cascade(label = "Jugar",menu=jugarmenu)
        configurarmenu = tk.Menu(menubar,tearoff=0)
        configurarmenu.add_command(label="Configurar",command = lambda:configuracion.configurar())
        menubar.add_cascade(label = "Configurar",menu=configurarmenu)
        ayudamenu = tk.Menu(menubar,tearoff=0)
        ayudamenu.add_command(label="Ayuda",command = lambda:extras.ayuda())
        menubar.add_cascade(label = "Ayuda",menu=ayudamenu)
        acercamenu = tk.Menu(menubar,tearoff=0)
        acercamenu.add_command(label="Acerca de",command = lambda:extras.acerca_de())
        menubar.add_cascade(label = "Acerca de",menu=acercamenu)
        salirmenu = tk.Menu(menubar,tearoff=0)
        salirmenu.add_command(label="Salir",command = lambda:extras.salir())
        menubar.add_cascade(label = "Salir",menu=salirmenu)
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
    def consultar_dat_byString(nombre):
        config_init_list=[]
        config_init=open(nombre,"r")
        while config_init:
            line = config_init.readline().rstrip('\n')
            config_init_list.append(line)
            if line == "":
                break
        config_init.close()
        return config_init_list
# Ventana configuracion 
class Configuracion:   
    nivel = ""
    reloj = ""
    posicion_digitos = "" 
    horas = 0
    minutos = 0
    segundos = 0
    def __init__(self):
        self.nivel = "facil"
        self.reloj = "si"
        self.posicion_digitos = "derecha"
        self.minutos = tk.StringVar()
        self.segundos = tk.StringVar()
        self.horas = tk.StringVar()
    def configurar(self):
        ventana_configurar= Creadores.crear_ventana("Configurar",500,500,ventana_principal)
        configuracion_datos = open("futoshiki2021configuración.dat","wb")#CREA EL DAT DE CONFIGURARCION
        configuracion = {"nivel":"facil","reloj":"si","timer":"no","horas":0,"minutos":0,"segundos":0,"posicion":"derecha"}
        pickle.dump(configuracion,configuracion_datos)
        configuracion_datos.close()
        #NIVEL
        nivel_label = tk.Label(ventana_configurar,text="1.  Nivel: ").place(relx=0.100,rely=0.050,anchor="center")
        facil_btn = tk.Radiobutton(ventana_configurar,text="Facil",command=lambda:self.guardar_nivel("facil")).place(relx=0.200,rely=0.100,anchor="center")
        intermedio_btn = tk.Radiobutton(ventana_configurar,text="Intermedio",command=lambda:self.guardar_nivel("intermedio")).place(relx=0.240,rely=0.150,anchor="center")
        dificil_btn = tk.Radiobutton(ventana_configurar,text="Dificil",command=lambda:self.guardar_nivel("dificil")).place(relx=0.210,rely=0.200,anchor="center")
        #RELOJ
        reloj_label= tk.Label(ventana_configurar,text="2.  Reloj: ").place(relx=0.100,rely=0.300,anchor="center")
        si_reloj_btn = tk.Radiobutton(ventana_configurar,text="Si",command=lambda:self.guardar_reloj("Si")).place(relx=0.200,rely=0.350,anchor="center")
        no_reloj_btn = tk.Radiobutton(ventana_configurar,text="No",command=lambda:self.guardar_reloj("No")).place(relx=0.205,rely=0.400,anchor="center")
        timer_btn = tk.Radiobutton(ventana_configurar,text="Timer").place(relx=0.220,rely=0.450,anchor="center")
        self.horas_label = tk.Label(ventana_configurar,text="Horas").place(relx=0.500,rely=0.350,anchor="center")
        self.horas_entry = tk.Entry(ventana_configurar,textvariable=self.horas,width=1)
        self.horas_entry.bind("<Return>",self.guardar_horas)
        self.horas_entry.place(relx=0.500,rely=0.400,anchor="center")
        timer_minutos_label = tk.Label(ventana_configurar,text="Minutos").place(relx=0.600,rely=0.350,anchor="center")
        timer_minutos_entry = tk.Entry(ventana_configurar,textvariable=self.minutos,width=2)
        timer_minutos_entry.bind("<Return>",self.guardar_minutos)
        timer_minutos_entry.place(relx=0.600,rely=0.400,anchor="center")
        timer_segundos_label = tk.Label(ventana_configurar,text="Segundos").place(relx=0.720,rely=0.350,anchor="center")
        timer_segundos_entry = tk.Entry(ventana_configurar,textvariable=self.segundos,width=2)
        timer_segundos_entry.bind("<Return>",self.guardar_segundos)
        timer_segundos_entry.place(relx=0.720,rely=0.400,anchor="center")
                                                            ########################################
                                                            #realizar validaciones con las entradas#
                                                            ########################################
        #POSICION
        posicion_label= tk.Label(ventana_configurar,text="3.  Posición en la ventana del panel de digitos: ").place(relx=0.330,rely=0.500,anchor="center")
        derecha_btn = tk.Radiobutton(ventana_configurar,text="Derecha",command=lambda:self.guardar_posicion("derecha")).place(relx=0.700,rely=0.500,anchor="center")
        izquierda_btn = tk.Radiobutton(ventana_configurar,text="Izquierda",command=lambda:self.guardar_posicion("izquierda")).place(relx=0.700,rely=0.550,anchor="center")
    def guardar_nivel(self,nivel):
        configuracion_datos = Creadores.leer_datos_binary("futoshiki2021configuración.dat")
        configuracion_datos["nivel"]= nivel
        configuracion=Creadores.escribir_datos_binary("futoshiki2021configuración.dat",configuracion_datos)
        print(configuracion_datos)
    def guardar_reloj(self,reloj_opcion):
        configuracion_datos = Creadores.leer_datos_binary("futoshiki2021configuración.dat")
        configuracion_datos["reloj"]=reloj_opcion
        configuracion = Creadores.escribir_datos_binary("futoshiki2021configuración.dat",configuracion_datos)
        print(configuracion)
    def guardar_horas(self,event):

        hrs = int(self.horas.get())
        if hrs != 0:
            configuracion_datos = Creadores.leer_datos_binary("futoshiki2021configuración.dat")
            configuracion_datos["timer"] ="si" 
            configuracion_datos["horas"]= hrs
            configuracion = Creadores.escribir_datos_binary("futoshiki2021configuración.dat",configuracion_datos)
            print(configuracion)
    def guardar_minutos(self,event):
        min = int(self.minutos.get())
        if min != 0:
            configuracion_datos = Creadores.leer_datos_binary("futoshiki2021configuración.dat")
            configuracion_datos["timer"]= "si"
            configuracion_datos["minutos"]= min
            configuracion = Creadores.escribir_datos_binary("futoshiki2021configuración.dat",configuracion_datos)
            print(configuracion)
        
    def guardar_segundos(self,event):
        sec = int(self.segundos.get())
        if sec != 0:
            configuracion_datos = Creadores.leer_datos_binary("futoshiki2021configuración.dat")
            configuracion_datos["timer"]= "si"
            configuracion_datos["segundos"]= sec
            configuracion = Creadores.escribir_datos_binary("futoshiki2021configuración.dat",configuracion_datos)
            print(configuracion)
        
    def guardar_posicion(self,posicion):
      configuracion_datos = Creadores.leer_datos_binary("futoshiki2021configuración.dat")
      configuracion_datos["posicion"]= posicion
      configuracion=Creadores.escribir_datos_binary("futoshiki2021configuración.dat",configuracion_datos)
      print(configuracion)
#Funciones extras 
class Extras: 
    def ayuda(self):
        wb.open_new(r"manual_de_usuario_futoshiki.pdf")
    def acerca_de(self):
        ventana_acerca = Creadores.crear_ventana("Acerca de",400,300,ventana_principal)
        autor = tk.Label(ventana_acerca,text="David Morales Vargas",font= "arial 20").place(relx = 0.500, rely = 0.250,anchor=CENTER)
        trabajo = tk.Label(ventana_acerca,text = "Programa 3: Futoshiki",font="arial 20").place(relx=0.500,rely=0.370,anchor="center")
        fecha = tk.Label(ventana_acerca,text=date.today(),font="arial 20").place(relx=0.500,rely=0.490,anchor=CENTER)
        version = tk.Label(ventana_acerca,text="Ver: Alpha 1.0",font="arial 20").place(relx=0.500,rely=0.610,anchor=CENTER)
    def salir(self):
        ventana_principal.quit()
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
jugar = Jugar()
configuracion = Configuracion()
extras = Extras()
jugarmenu.add_command(label="Jugar",command = lambda: jugar.jugar())
menubar.add_cascade(label = "Jugar",menu=jugarmenu)
configurarmenu = tk.Menu(menubar,tearoff=0)
configurarmenu.add_command(label="Configurar",command = lambda:configuracion.configurar())
menubar.add_cascade(label = "Configurar",menu=configurarmenu)
ayudamenu = tk.Menu(menubar,tearoff=0)
ayudamenu.add_command(label="Ayuda",command = lambda:extras.ayuda())
menubar.add_cascade(label = "Ayuda",menu=ayudamenu)
acercamenu = tk.Menu(menubar,tearoff=0)
acercamenu.add_command(label="Acerca de",command = lambda:extras.acerca_de())
menubar.add_cascade(label = "Acerca de",menu=acercamenu)
salirmenu = tk.Menu(menubar,tearoff=0)
salirmenu.add_command(label="Salir",command = lambda:extras.salir())
menubar.add_cascade(label = "Salir",menu=salirmenu)
ventana_principal.config(menu=menubar)
fuente = tkfont.Font(family="Arial",size=30)


     
ventana_principal.mainloop()
