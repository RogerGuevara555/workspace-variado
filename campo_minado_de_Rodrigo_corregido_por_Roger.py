

def tablero_de_pistas(campo : list[list], func) -> tuple:
    pistas = []
    casilla_mas_peligrosa_valor = -1

    for i in range(len(campo)):
        pistas.append([])

        for j in range(len(campo[i])):

            if campo[i][j] == 0:
                suma = sum(func(campo, i, j))

                if suma > casilla_mas_peligrosa_valor:
                    casilla_mas_peligrosa_valor = suma
                    casilla_mas_peligrosa_fila = i
                    casilla_mas_peligrosa_columna = j

                pistas[i].append(suma)

            else:
                pistas[i].append(-1)

    if casilla_mas_peligrosa_valor == -1:
        return (pistas, -1, -1)
    
    return (pistas, casilla_mas_peligrosa_fila, casilla_mas_peligrosa_columna)
            

def ForEachDir(campo: list[list], a: int, b: int) -> list:
    casillas_en_derredor = []
    a_no_2 = a < len(campo) - 1
    b_no_2 = b < len(campo[1]) - 1
    # a=2
    # b=0
    
    if a_no_2:
        casillas_en_derredor.append(campo[a+1][b])

    if a > 0:
        casillas_en_derredor.append(campo[a-1][b])

    if b_no_2:
        casillas_en_derredor.append(campo[a][b+1])

    if b > 0:
        casillas_en_derredor.append(campo[a][b-1])

    if a_no_2 and b_no_2:
        casillas_en_derredor.append(campo[a+1][b+1])

    if a_no_2 and b > 0:
        casillas_en_derredor.append(campo[a+1][b-1])

    if a > 0 and b_no_2:
        casillas_en_derredor.append(campo[a-1][b+1])

    if a > 0 and b > 0:  # ese último "b > 0" era "b_no_2" y por eso se bugueaba, aunque el bug no afectaba mucho 
        casillas_en_derredor.append(campo[a-1][b-1]) # en este caso ya que solo ocurría con las casillas minadas

    return casillas_en_derredor

    
def ForEachDirR (campo: list[list], a: int, b: int) -> list:
    casillas_en_derredor = []

    for i in [-1,0,1]:
        for j in [-1,0,1]:
            in_range_y : bool = a+i >= 0 and a+i <= len(campo) - 1
            in_range_x : bool = b+j >= 0 and b+j <= len(campo[0]) - 1
            if i==0 and j==0: continue
            if in_range_y and in_range_x: 
                casillas_en_derredor.append(campo[a+i][b+j])

    return casillas_en_derredor


campo = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

campo2 = [
    [1, 1],
    [1, 1]
]

campo3 = [
    [0, 0],
    [0, 0]
]



if __name__ == "__main__":

    for i in range(len(campo)):
        for j in range(len(campo[0])):
            print(f"{i}x{j}")
            print("Rodrigo: ", ForEachDir (campo, i, j))
            print("Roger:   ", ForEachDirR(campo, i, j))
            print()
    print(tablero_de_pistas(campo, ForEachDir ))
    print(tablero_de_pistas(campo, ForEachDirR))
