print()
print('Combinati doua liste sorate crescator intr-o noua lista sorata crescator. \n')


print('introduceti de la tastatura numarul de elemente pe care lista il va avea prima lista:')

numar_elemente = int(input())
lista1 = []
lista2 = []

# folosim bucla for pentru a introduce manual elementele primei liste
print('introduceti elementele primei liste:')
for i in range(numar_elemente):
    print(f'lista1[{i}] = ', end=' ')
    element = int(input())
    lista1.append(element)

# declaram o noua variabila pentru a stoca lista1, 
# deoarece elementele listei stocata in aceasta variabila, 
# urmeaza sa fie ordonate crescator cu ajutorul algoritmului bubble sort    
lista1_sortata_crescator = [x for x in lista1]

print('introduceti de la tastatura numarul de elemnte pe care lista il va avea a doua lista:')

numar_elemente = int(input())

# folosim bucla for pentru a introduce manual elementele celei de-a doua liste
print('introduceti elementele celei de-a doua liste:')
for i in range(numar_elemente):
    print(f'lista2[{i}] = ', end=' ')
    element = int(input())
    lista2.append(element)

# declaram o noua variabila pentru a stoca lista2, 
# deoarece elementele listei stocata in aceasta variabila, 
# urmeaza sa fie ordonate crescator cu ajutorul algoritmului bubble sort
lista2_sortata_crescator = [x for x in lista2]

print()

# sortam in ordine crescatoare lista1, folosind algoritmul bubble sort

# EXPLICAREA ALOGORITMUL BUBBLE SORT
# declaram variabila temp, pe care o folosim pentru a stoca temporar elemente din lista
temp = ''

# folosim doua bucle for, una in interiorul celeilalte, 
# deoarece avem nevoie de doi selectori 'i' si 'j',
# pentru a putea compara elementele, doua cate doua 
for i in range(len(lista1)):
    # in timp ce selectorul 'i' este in dreptul unui element al listei
    for j in range(len(lista1)):
        # selectorul j parcurge toate elementele listei
        
        # in acelasi timp se verifica daca elementul selectat de selectorul 'j' 
        # este mai mare decat elementul selectat de selectorul 'i'
        if lista1_sortata_crescator[j] > lista1_sortata_crescator[i]:
            # in cazul in care elementul listei selectat prin cursorul 'j'
            # este mai mare decat elementul selectat de selectorul 'i':
            
            # 1. atribuim variabilei temp valoarea selectorului 'i'
            temp = lista1_sortata_crescator[i]
            # 2. atribuim selectorului 'i' valoarea selectorului 'j'
            lista1_sortata_crescator[i] = lista1_sortata_crescator[j]
            # 3. atribuim selectorului 'j' valoarea variabilei temp
            lista1_sortata_crescator[j] = temp
            
print('Prima lista in original: ', lista1)
print('Prima lista sortata crescator: ', lista1_sortata_crescator)
print()

# sortam in ordine crescatoare lista2, folosind din nou algoritmul bubble sort, in mod identic            
temp = ''
for i in range(len(lista2)):
    for j in range(len(lista2)):
        if lista2_sortata_crescator[j] > lista2_sortata_crescator[i]:
            temp = lista2_sortata_crescator[i]
            lista2_sortata_crescator[i] = lista2_sortata_crescator[j]
            lista2_sortata_crescator[j] = temp

print('A doua lista in original: ', lista2)
print('A doua lista sortata crescator: ', lista2_sortata_crescator)
print()

# declaram variabila lista3 si ii asociem ca valoare o lista obtinuta prin 
# reuniunea elementelor din lista1_sortata_crescator si lista2_sortata_crescator
lista3 = lista1_sortata_crescator + lista2_sortata_crescator

# declaram o noua variabila pentru a stoca lista3, 
# deoarece elementele listei stocata in aceasta variabila, 
# urmeaza sa fie ordonate crescator cu ajutorul algoritmului bubble sort
lista3_sortata_crescator = [x for x in lista3]

# sortam in ordine crescatoare lista3, folosind din nou algoritmul bubble sort, in mod identic
temp = ''
for i in range(len(lista3)):
    for j in range(len(lista3)):
        if lista3_sortata_crescator[j] > lista3_sortata_crescator[i]:
            temp = lista3_sortata_crescator[i]
            lista3_sortata_crescator[i] = lista3_sortata_crescator[j]
            lista3_sortata_crescator[j] = temp

print('Lista a treia in original: ', lista3)
print('Lista a treia sortata crescator: ', lista3_sortata_crescator)