print()
print('Verificati daca doua liste de numere sunt disjuncte (nu au elemente comune).')
print('introduceti numarul de elemente pe care doriti ca listele sa le aiba:')

numar_elemente = int(input())

lista1 = []
lista2 = []
elemente_comune = []

print('introduceti elementele primei liste:')
for i in range(numar_elemente):
    print(f'lista1[{i}] = ', end=' ')
    element = int(input())
    lista1.append(element)
    
    
print('introduceti elementele celei de-a doua liste:')

for i in range(numar_elemente):
    print(f'lista2[{i}] = ', end=' ')
    element = int(input())
    lista2.append(element)
    

for i in lista1:
    for j in lista2:
        if i == j:
            elemente_comune.append(i)
            
if len(elemente_comune) < 1:
    print('liste1 si lista2 sunt disjuncte.')
else:
    print(str(elemente_comune))
