print()
print('Combinati doua liste sorate crescator intr-o noua lista sorata crescator. \n')


print('introduceti de la tastatura numarul de elemente pe care lista il va avea prima lista:')

numar_elemente = int(input())
lista1 = []
lista2 = []


print('introduceti elementele primei liste:')
for i in range(numar_elemente):
    print(f'lista1[{i}] = ', end=' ')
    element = int(input())
    lista1.append(element)
    
lista1_sortata_crescator = [x for x in lista1]

print('introduceti de la tastatura numarul de elemnte pe care lista il va avea a doua lista:')
numar_elemente = int(input())


print('introduceti elementele primei liste:')
for i in range(numar_elemente):
    print(f'lista2[{i}] = ', end=' ')
    element = int(input())
    lista2.append(element)
    
lista2_sortata_crescator = [x for x in lista2]

print()
print('Prima lista in original: ', lista1)
print('A doua lista in original: ', lista2)
print()

temp = ''
for i in range(len(lista1)):
    for j in range(len(lista1)):
        if lista1_sortata_crescator[j] > lista1_sortata_crescator[i]:
            temp = lista1_sortata_crescator[i]
            lista1_sortata_crescator[i] = lista1_sortata_crescator[j]
            lista1_sortata_crescator[j] = temp
            
temp = ''
for i in range(len(lista2)):
    for j in range(len(lista2)):
        if lista2_sortata_crescator[j] > lista2_sortata_crescator[i]:
            temp = lista2_sortata_crescator[i]
            lista2_sortata_crescator[i] = lista2_sortata_crescator[j]
            lista2_sortata_crescator[j] = temp

print('Prima lista sortata crescator: ', lista1_sortata_crescator)
print('A doua lista sortata crescator: ', lista2_sortata_crescator)
print()

lista3 = lista1 + lista2
lista3_sortata_crescator = [x for x in lista3]

print('Lista a treia in original: ', lista3)

temp = ''
for i in range(len(lista3)):
    for j in range(len(lista3)):
        if lista3_sortata_crescator[j] > lista3_sortata_crescator[i]:
            temp = lista3_sortata_crescator[i]
            lista3_sortata_crescator[i] = lista3_sortata_crescator[j]
            lista3_sortata_crescator[j] = temp

print('Lista a treia sortata crescator: ', lista3)