print()
print('Numarati elementele care nu se repeta dintr-o lista cu numere. \n')


print('introduceti de la tastatura numarul de elemente pe care lista il va avea lista:')
numar_elemente = int(input())
lista = []
elemente_care_nu_se_repeta = []

print('introduceti elementele listei:')
for i in range(numar_elemente):
    print(f'lista[{i}] = ', end=' ')
    element = int(input())
    lista.append(element)
    
print('Lista originala: ', lista)
    

for element in lista:
    if lista.count(element) < 2:  
        elemente_care_nu_se_repeta.append(element)
        
print('Numarul elementelor care nu se repeta: ', len(elemente_care_nu_se_repeta))