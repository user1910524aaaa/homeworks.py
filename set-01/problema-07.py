print()
print('Combinati doua liste sorate crescator intr-o noua lista sorata crescator. \n')


print('introduceti de la tastatura numarul de elemente pe care lista il va avea prima lista:')
numar_elemente = int(input())
lista1 = []

print('introduceti elementele primei liste:')
for i in range(numar_elemente):
    print(f'lista1[{i}] = ', end=' ')
    element = int(input())
    lista1.append(element)


print('introduceti de la tastatura numarul de elemnte pe care lista il va avea a doua lista:')
numar_elemente = int(input())
lista2 = []

print('introduceti elementele primei liste:')
for i in range(numar_elemente):
    print(f'lista2[{i}] = ', end=' ')
    element = int(input())
    lista2.append(element)
    
    
print('Prima lista in original: ', str(lista1))
print('A doua lista in original: ', str(lista2))

print('Prima lista sortata crescator: ', str(sorted(lista1)))
print('A doua lista sortata crescator: ', str(sorted(lista2)))

lista3 = lista1 + lista2
print('Lista a treia in original: ', str(lista3))
print('Lista a treia sortata crescator: ', str(sorted(lista3)))