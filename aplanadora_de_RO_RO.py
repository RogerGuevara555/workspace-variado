
def aplanadora (lista):
    
    if lista == []:
        return []
    
    elif type(lista[0]) != list:
        return [lista[0]] + aplanadora(lista[1:])
    
    else:
        return aplanadora(lista[0]) + aplanadora(lista[1:])

repre = lambda x : print(aplanadora(x))

lista1 = [1, 2, [3,5,[7]], 8, 2]
lista2 = [[1, 2], [3, [4,[5]]]]
lista3 = []

repre(lista1)
repre(lista2)
repre(lista3)

