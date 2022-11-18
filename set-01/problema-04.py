print()
print('Verificati daca doua liste de numere sunt disjuncte (nu au elemente comune). \n')
print('introduceti numarul de elemente pe care doriti ca listele sa le aiba:')

numar_elemente = int(input())

lista1 = []
lista2 = []
elemente_comune = []

print('introduceti elementele primei liste:')
# folosim bucla for pentru a putea introduce in mod dinamic valori in lista1 sub forma de elemente.
# numarul de elemente pe care il va avea lista este stabilit de valoarea atribuita dinamic variabilei 
# numar_elemente.pentru a parcurge bucla for in functie de valoarea atribuita variabilei numar_elemente, 
# vom folosi bucla for impreuna cu functia range(parametru), care preia in parametru numarul pana la care 
# sa faca iteratia, incepand de la 0.
for i in range(numar_elemente):
    # parametrul end din functia print, reprezinta ultimul caracter care este adaugat la capatul a ceea ce urmeaza sa fie afisat.
    # in mod standard valoarea parametrului este '\n' (linie noua), iar noi o rescriem, inlocuind-o cu ' ' (spatiu).
    # motivul pentru care facem acest lucru, este acela ca vrem sa afisam pe aceasi linie atat elementul, 
    # cat si valoarea atribuita dinamic
    print(f'lista1[{i}] = ', end=' ')
    
    # declaram variabila element, la care ii atribuim la fiecare iteratie, o valoare preluata dinamic prin functia input()
    element = int(input())
    # adaugam valoarea preluata prin variabila element in lista1
    lista1.append(element)
    
    
print('introduceti elementele celei de-a doua liste:')

for i in range(numar_elemente):
    print(f'lista2[{i}] = ', end=' ')
    element = int(input())
    lista2.append(element)
    
# pentru a vedea daca cele doua liste au elemente comune, vom avea nevoie de o 
# a treia lista in care sa adaugam elementele comune din cele doua liste, iar la final, 
# vom verifica daca numarul elementelor din lista cu elemente comune este mai mic decat 1

# folosim doua bucle for, una in interiorul celeilalte, pentru a parcurge cele doua liste.

# in timp ce prima bucla for selecteaza un element din prima lista,
for element_lista1 in lista1:
    # ce-a de-a doua bucla parcurge toate elemente din a doua lista.
    for element_lista2 in lista2:
        # se verifica daca elementul selectat de prima bucla for (element_lista1), 
        # este egal cu elementul selectat de a doua bucla for (element_lista2)
        if element_lista1 == element_lista2:
            # in cazul in care exista o egalitate intre un element din lista1 si un element din lista2,
            # elementul respectiv este adaugat in cea de-a treia lista (elemente_comune)
            elemente_comune.append(i)
            
print('Lista 1 originala: ', lista1)
print('Lista 2 originala: ', lista2)

if len(elemente_comune) < 1: print('liste1 si lista2 sunt disjuncte.')
else: print(f'lista1 si lista2 nu sunt disjuncte. Au {len(elemente_comune)} elemente comune')
