print()
print('Numarati elementele care se repeta dintr-o lista cu numere')


print('introduceti de la tastatura numarul de elemnte pe care lista il va avea lista:')
numar_elemente = int(input())
lista = []
elemente_care_se_repeta = []


print('introduceti elementele liste:')
for i in range(numar_elemente):
    print(f'lista[{i}] = ', end=' ')
    element = int(input())
    lista.append(element)
    
print(str(lista))
    
    
for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] == lista[j]:
            elemente_care_se_repeta.append(lista[i])
        
print('Elementele care se repeta: ', str(elemente_care_se_repeta))