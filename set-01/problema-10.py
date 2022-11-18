print()
print('Afisati in ordine inversa o lista de numere. \n')


print('introduceti de la tastatura numarul de elemente pe care lista il va avea lista:')
numar_elemente = int(input())
lista = []

print('introduceti elementele listei:')
for i in range(numar_elemente):
    print(f'lista[{i}] = ', end=' ')
    element = int(input())
    lista.append(element)
    
print('Lista originala: ', lista)

# pentru fiecare element din lista, bucla for parcurge un ciclu
# EXEMPLU:

# lista = [1, 2, 3, 4, 5]

# inversa_listei = []

# primul ciclu:
# for 1 in lista
    # inversa_listei = [1] + inversa_listei => inversa_listei = [1]
    
# sfarsitul unui ciclu al buclei
    
    
# al doilea ciclu:
# for 2 in lista
    # inversa_listei = [2] + inversa_listei => inversa_listei = [2, 1]
    
# sfarsitul unui ciclu al buclei

    
# al treilea ciclu:
# for 3 in lista
    # inversa_listei = [3] + inversa_listei => inversa_listei = [3, 2, 1]
    
# sfarsitul unui ciclu al buclei
    
    
# al patrulea ciclu:
# for 4 in lista
    # inversa_listei = [4] + inversa_listei => inversa_listei = [4, 3, 2, 1]
    
# sfarsitul unui ciclu al buclei
    
    
# al cincilea ciclu:
# for 5 in lista
    # inversa_listei = [5] + inversa_listei => inversa_listei = [5, 4, 3, 2, 1]

# sfarsitul unui ciclu al buclei



# pentru fiecare element din lista, bucla for parcurge un ciclu
for valoare in lista:
    inversa_listei = [valoare] + inversa_listei
# sfarsitul unui ciclu al buclei
# bucla incepe un nou ciclu pentru fiecare element al listei atrbuita variabilei lista


# inversa_listei = lista[::-1]
print('Inversa listei : ', inversa_listei)