print()
print('Rotiti o lista de numere de la dreapta de n ori (se citeste n). \n')
print('introduceti de la tastatura numarul de elemente pe care lista il va avea:')

lista = []
numar_elemente = int(input())

for i in range(numar_elemente):
    print(f'lista[{i}] = ', end=' ')
    element = int(input())
    lista.append(element)
    
print('introduceti n de la tastatura:')
n = int(input())
print('n = ', n)
    
print('Lista originala: ', lista)
 
# rotirea listei de la dreapta cu ajutorul tehnicii slice
# EXEMPLU:

# lista = [1, 2, 3, 4, 5]
# n = 3

# lista_rotata_de_la_dreapta = [4, 5] + [1, 2, 3] = [4, 5, 1, 2, 3]

lista_rotata_de_la_dreapta = lista[n:] + lista[:n]
 
print (f'Lista dupa ce a fost facuta rotatia de la dreapta de {n} ori: ' + str(lista_rotata_de_la_dreapta))