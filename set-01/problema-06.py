print()
print('Rotiti o lista de numere de la stanga de n ori (se citeste n). \n')
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
    
print ('Lista originala: ' + lista)
 
# rotirea listei de la stanga cu ajutorul tehnicii slice
lista_rotata_de_la_stanga = lista[-n:] + lista[:-n]
 
print (f'Lista dupa ce a fost facuta rotatia de la stanga de {n} ori: ' + str(lista_rotata_de_la_stanga))
 