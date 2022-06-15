import random as rd

class Celda:

    def __init__(self, pos, lista_celdas):
        self.pos = pos
        self.tieneBomba = rd.choice([True, False, False, False, False, False, False])
        self.lista_celdas = lista_celdas
        self.numero = 0
        self.revelado = False

    def __repr__(self):
        if(self.tieneBomba):
            return "Bomba"
        else:
            return str(self.numero)

    #cantidad de bombas cercanas
    def establecer_numero(self):
        if(not self.tieneBomba):
            self.numero = bombas_cerca_de(self.pos, self.lista_celdas)

    def revelar(self):
        self.revelado = True
        if self.tieneBomba:
            return '@'
        elif(self.numero == 0):
            return ' '
        else:
            return str(self.numero)

    



def bombas_cerca_de(pos, lista_celdas):
    fila = pos[0]
    col = pos[1]
    cant_bombas = 0
    for i in range(max(fila - 1, 0), min(fila + 2, cantidad_filas(lista_celdas))):
        for j in range(max(col - 1, 0), min(col + 2, cantidad_columnas(lista_celdas))):
            celda = lista_celdas[i][j]
            if(lista_celdas[i][j].tieneBomba):
                 cant_bombas = cant_bombas + 1
    return cant_bombas


def cantidad_filas(lista):
    return len(lista)

def cantidad_columnas(lista):
    return len(lista[0])

def contar_bombas(lista_celdas):
    bombas = 0
    for fila in range(cantidad_filas(lista_celdas)):
        for columna in range(cantidad_columnas(lista_celdas)):
            if (lista_celdas[fila][columna].tieneBomba):
                bombas = bombas + 1
    return bombas


def inicializar_celdas(filas, columnas, lista_celdas):
    for fila in range(filas):
        lista_celdas.append([])
        for columna in range(columnas):
            lista_celdas[fila].append(Celda((fila, columna), lista_celdas))
    return lista_celdas


#doy valor a celda.numero
def valorizar_celdas(lista_celdas):
    filas = len(lista_celdas)
    columnas = len(lista_celdas[0])

    print(filas)
    print(columnas)

    for fila in range(filas):
        for columna in range(columnas):
            celda = lista_celdas[fila][columna]
            celda.establecer_numero()
    return lista_celdas