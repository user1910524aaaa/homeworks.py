print()
print('Afisati elementele care se repeta dintr-o lista de numere. \n')


print('introduceti de la tastatura numarul de elemente pe care lista il va avea lista:')
numar_elemente = int(input())
lista = []
elemente_care_se_repeta = []

print('introduceti elementele listei:')
for i in range(numar_elemente):
    print(f'lista[{i}] = ', end=' ')
    element = int(input())
    lista.append(element)
    
print('Lista originala: ', lista)
    
    
for element in lista:
    if lista.count(element) > 1 and element not in elemente_care_se_repeta:
        elemente_care_se_repeta.append(element)
        
print('Elementele care se repeta: ', ', '.join(str(element) for element in elemente_care_se_repeta))