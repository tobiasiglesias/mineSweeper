from tkinter import *
from tkinter import messagebox
import tkinter
from celdas import Celda, cantidad_columnas, cantidad_filas, contar_bombas, inicializar_celdas, valorizar_celdas

ventana = Tk()
botones_celdas = []
lista_celdas = []
perdiste = False
# filas_num = int(input("Filas?"))
# columnas_num = int(input("Columnas?"))
filas_num = 30
columnas_num = 30
normales_restantes = filas_num * columnas_num


def iniciar_programa(filas, columnas, lista_celdas):
    lista_celdas = inicializar_celdas(filas, columnas, lista_celdas)
    lista_celdas = valorizar_celdas(lista_celdas)
    crear_grid(filas, columnas)
    return lista_celdas



def revelar_aledanias_sin_bomba(fila, columna, lista_celdas):   
    for i in range(max(fila - 1, 0), min(fila + 2, cantidad_filas(lista_celdas))):
            for j in range(max(columna - 1, 0), min(columna + 2, cantidad_columnas(lista_celdas))):
                celda = lista_celdas[i][j]
                if(not celda.tieneBomba and not celda.revelado):
                    click_izquierdo(i, j)

def click_izquierdo(fila, columna):
    print("{},{}".format(fila, columna))
    boton = botones_celdas[fila][columna]
    celda = lista_celdas[fila][columna]
    valor = celda.revelar()
    global normales_restantes
    if(valor == '@'):
        boton.config(state = "disabled", bg = '#f75757')
        if(messagebox.showinfo(message=":(", title = "Perdiste!")):
            ventana.destroy()

    elif(valor == ' '):
        boton.config(state = "disabled", bg = '#FFEDBB', fg = '#000000')
        normales_restantes -= 1
        revelar_aledanias_sin_bomba(fila, columna, lista_celdas)
    else:
        boton.config(state = "disabled", bg = '#FFEDBB', fg = '#000000')
        normales_restantes -= 1
        print(normales_restantes)
        if(normales_restantes == 0):
            if(messagebox.showinfo(message=":)", title = "Ganaste!")):
                ventana.destroy()

    boton['text'] = valor    

def click_derecho(fila, columna):
    print("{},{}".format(fila, columna))
    boton = botones_celdas[fila][columna]
    if(boton['text'] == 'F'):
        boton['text'] = ' '
        boton.config(bg = '#FFFBF0', fg = '#000000')
    else:
        boton['text'] = 'F'    
        boton.config(bg = '#B3FF6F', fg = '#000000')
    

def crear_grid(filas, columnas):
    for fila in range(filas):
        botones_celdas.append([])
        for columna in range(columnas):
            botones_celdas[fila].append(tkinter.Button(ventana, width = 2, height = 1,bg = '#FFFBF0', font = ("Arial", 9)))
            botones_celdas[fila][columna].grid(row = fila, column = columna)
            botones_celdas[fila][columna].bind("<Button-1>", lambda tt = fila, fila_boton = fila, columna_boton = columna: click_izquierdo(fila_boton, columna_boton))
            botones_celdas[fila][columna].bind("<Button-3>", lambda tt = fila, fila_boton = fila, columna_boton = columna: click_derecho(fila_boton, columna_boton))


iniciar_programa(filas_num, columnas_num, lista_celdas)
normales_restantes = normales_restantes - contar_bombas(lista_celdas)
ventana.eval('tk::PlaceWindow . center')

print(lista_celdas)
ventana.mainloop()




