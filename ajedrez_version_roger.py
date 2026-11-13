
tablero = [
        [None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None], 
        [None, None, None, None, None, None, None, None], 
        ]


def PeonBlanco(fila, columna):
    lista = [(fila-1, columna+1), (fila+1, columna-1)]

    lista_final = []
    for i in lista:
        if i[1] < 8 and i[1] >= 0:
            lista_final.append(i)
    return lista_final

def PeonNegro(fila, columna):
    lista = [(fila+1, columna+1), (fila-1, columna-1)]

    lista_final = []
    for i in lista:
        if i[1] < 8 and i[1] >= 0:
            lista_final.append(i)
    return lista_final




def Torre(fila, columna):
    coord = (fila, columna)
    lista_final = []

    trozo_arriba    = comprobar_linea(coord, (-1,0))
    trozo_derecha   = comprobar_linea(coord, (0,1))
    trozo_abajo     = comprobar_linea(coord, (1,0))
    trozo_izquierda = comprobar_linea(coord, (0,-1))
    
    lista_final.extend(trozo_abajo)
    lista_final.extend(trozo_arriba)
    lista_final.extend(trozo_derecha)
    lista_final.extend(trozo_izquierda)
    
    return lista_final


def comprobar_linea(coord, dir):
    lista_trozo = []
    contador_v = coord[0] + 1*dir[0]
    contador_h = coord[1] + 1*dir[1]

    while contador_h >= 0 and contador_h < 8 and contador_v >= 0 and contador_v < 8:
        lista_trozo.append((contador_v, contador_h))
        if tablero[contador_v][contador_h] != None:
            break
        contador_v += 1*dir[0]
        contador_h += 1*dir[1]
    
    return lista_trozo





    
    
        

#def Alfil(fila, columna):

#def Caballo(fila, columna):

#def Dama(fila, columna):




    
















#print(tablero[3][6])
print(Torre(3, 5))
